---
id: callout
aliases: []
tags:
  - files
  - templates
  - templater
dg-publish: true
---
# AI-Providers

>[!SUMMARY]+ Table of Contents
>- [[ai-providers#AI-Providers|AI-Providers]]
>    - [[ai-providers#Methods |Methods ]]
>        - [[ai-providers#Abstract Methods|Abstract Methods]]
>            - [[ai-providers#`ask()`|`ask()`]]
>            - [[ai-providers#`name()`|`name()`]]
>            - [[ai-providers#`_call_api()`|`_call_api()`]]
>                - [[ai-providers#Why? |Why? ]]
>                    - [[ai-providers#Explanation|Explanation]]
>                    - [[ai-providers#Issues |Issues ]]
>                    - [[ai-providers#Minor Modification |Minor Modification ]]
>    - [[ai-providers#Using AIProvider Class|Using AIProvider Class]]
>- [[ai-providers#Custom Imports|Custom Imports]]
>            - [[ai-providers#Testing|Testing]]


> [!abstract]- **Full Code**
> ```python
> 
> from abc import ABC, abstractmethod
> from enum import Enum
> from datetime import datetime
> import time
> import threading
> class AiProviderStatus(Enum):
>     IDLE = "Idle"
>     BUSY = "Busy"
>     ERROR = "Error"
>     """If its offline , create a seperate thread ans ask a demo question to check its status"""
>     OFFLINE = "Offline"
>     TIMEOUT = "Timeout"
> class AiProviderList(Enum):
>     OLLAMA = "Ollama"
>     ALEXA = "Alexa"
>     GITHUB_GPT_5 = "GitHub GPT-5"
>     COHERE = "Cohere"
>     GEMINI = "Gemini"
>    
> class QuestionAndAnswer:
>     def __init__(
>         self,
>         question: str,
>         answer: str,
>         ):
>         self.question = question
>         self.answer = answer
>         self.timestamp =  datetime.now()
>         
>     def to_dict(self) -> dict:
>         return {
>             "question": self.question,
>             "answer": self.answer,
>             "timestamp": self.timestamp.isoformat()
>         }
>     
>     def __repr__(self) -> str:
>         return f"QuestionAndAnswer(question='{self.question[:50]}...', answer='{self.answer[:50]}...', timestamp={self.timestamp})"
>     
>     def __str__(self) -> str:
>         return f"Q: {self.question}\nA: {self.answer}\nTime: {self.timestamp}"
> 
> 
>     @classmethod
>     def from_dict(cls, data: dict):
>         timestamp = datetime.fromisoformat(data["timestamp"]) if "timestamp" in data else None
>         return cls(question=data["question"], answer=data["answer"], timestamp=timestamp)
>      
> class AIProvider(ABC):
>     def __init__(self):
>         self._status = AiProviderStatus.IDLE
>         """List of responses received from the AI provider"""
>         self._responses = []
>         """List of messages in the conversation history"""
>         self._messages: list[dict[str, str]] | list = []
>         self._QandAs: list[QuestionAndAnswer] = []
>         self._question_asked_time: float = 0.0
>         self._answer_time: float = 0.0
>         self._response_time: float = 0.0
>         self._last_answer_time: float = 0.0  
>         """Request Params"""
>         self._temperature: float = 0.3
>         self._max_tokens: int = 150
>         
>         """For Threading"""
>         self._thread: threading.Thread | None = None
>         self._timeout: int = 10  # Default timeout in seconds
>         self._stop_event: threading.Event = threading.Event()  
>         self._last_result: str = ""  
>     @property
>     def QandAs(self) -> list[QuestionAndAnswer]:
>         return self._QandAs
>     @QandAs.setter
>     def QandAs(self, value: list[QuestionAndAnswer]):
>         self._QandAs = value
>     
>     def add_QandA(self, question: str, answer: str) -> None:
>         q_and_a = QuestionAndAnswer(
>             question=question,
>             answer=answer
>             )
>         self._QandAs.append(q_and_a)
> 
>     @property
>     def thread(self) -> threading.Thread | None:
>         return self._thread
>     
>     @property
>     def timeout(self) -> int:
>         return self._timeout
>     @timeout.setter
>     def timeout(self, value: int) -> None:
>         self._timeout = value
>         
>     def ask_with_timeout(self, prompt: str) -> str:
>         """Ask with timeout - kills thread if it takes too long"""
>         self._stop_event.clear()  
>         
>         # Create and start thread
>         self._thread = threading.Thread(target=self._ask_with_stop_check, args=(prompt,))
>         self._thread.daemon = True  # Make it a daemon thread
>         self._thread.start()
>         
>         self._thread.join(timeout=self._timeout)
>         if self._thread.is_alive():
>             print(f"⚠️ {self.name} request timed out after {self._timeout} seconds")
>             self._stop_event.set() 
>             self._thread.join(timeout=0.5)
>             if self._thread.is_alive():
>                 print(f"❌ {self.name} with id {self._thread.ident} did not stop")
>             self.status = AiProviderStatus.TIMEOUT
>             # return f"Request to {self.name} timed out after {self._timeout} seconds"
>             return ""
>         # Thread completed successfully
>         return getattr(self, '_last_result', '')
>     
>     def _ask_with_stop_check(self, prompt: str) -> None:
>         """Internal method that checks for stop signal during execution"""
>         try:
>             if self._stop_event.is_set():
>                 return
>             result = self.ask(prompt)
>             if not self._stop_event.is_set():
>                 self._last_result = result
>                 
>         except Exception as e:
>             if not self._stop_event.is_set():
>                 print(f"Error in thread: {e}")
>                 self._last_result = f"Error: {e}"
> 
>     @abstractmethod
>     def ask(self, prompt: str) -> str:
>         """Abstract method that must be implemented by subclasses"""
>         # Check for stop signal at the beginning
>         if hasattr(self, '_stop_event') and self._stop_event.is_set():
>             return "Request was cancelled due to timeout"
> 
>         message = {"role": "user", "content": prompt}
>         self._messages.append(message)
>         # Don't return anything - let subclasses handle the actual response
>         return ""  # Return empty string instead of None
>     
>     @abstractmethod
>     def _call_api(self, message: list[dict[str, str]] | str) -> str:
>         """Abstract method that must be implemented by subclasses to handle actual API calls"""
>         pass
>     
>     def _generic_ask(self, prompt: str) -> str:
>         """Generic ask implementation that can be used by subclasses"""
>         if not prompt or not prompt.strip():
>             print(f"{ self.name }: Prompt validation failed")
>             return "Please provide a valid prompt."
>         print("DEBUG: Prompt validation passed, proceeding...")
>         
>         try:
>             self.status = AiProviderStatus.BUSY
>             self.add_message("user", prompt)
>             
>             # Check for stop signal before API call
>             if hasattr(self, '_stop_event') and self._stop_event.is_set():
>                 self.status = AiProviderStatus.ERROR
>                 return "Request was cancelled"
>             
>             # Send full conversation history for context
>             self.answer = self._call_api(self.messages)
>             self.status = AiProviderStatus.IDLE
>             self.add_QandA(
>                 self.messages[-1]['content'], 
>                 self.answer
>             )
>             return self.answer
>         except Exception as e:
>             self.status = AiProviderStatus.ERROR
>             return f"Error communicating with {self.name}: {e}"
>     
>     @property
>     @abstractmethod
>     def name(self) -> str:
>         """Abstract method that must be implemented by subclasses"""
>         pass
>     @property
>     def status(self) -> AiProviderStatus:
>         """Property getter for status"""
>         return self._status
> 
>     @status.setter
>     def status(self, value: AiProviderStatus) -> None:
>         """Property setter for status"""
>         if value == AiProviderStatus.IDLE:
>             self._answer_time = time.time()  
>         elif value == AiProviderStatus.BUSY:
>             self._question_asked_time = time.time()  
>         elif value == AiProviderStatus.ERROR:
>             if self._question_asked_time > 0:
>                 self._answer_time = time.time()
>         self._status = value
>     
>     @property
>     def answer_time(self) -> float:
>         """Property getter for answer_time"""
>         return self._answer_time
>     
>     @property
>     def question_asked_time(self) -> float:
>         """Property getter for question_asked_time"""
>         return self._question_asked_time
>         
>     @property
>     def messages(self) -> list[dict[str, str]]:
>         """Property getter for messages"""
>         return self._messages
> 
>     @messages.setter
>     def messages(self, value: list[dict[str, str]]) -> None:
>         """Property setter for messages"""
>         """ For getting question response time """
>         self._question_asked_time = time.time()
>         self._messages = value
>     
>     def add_message(self, role: str, content: str) -> None:
>         """Method to add a message to the messages list"""
>         self._messages.append({"role": role, "content": content})
>     
>     def clear_messages(self) -> None:
>         """Method to clear the messages list"""
>         self._messages = []
>         print("Conversation history cleared")
> 
>     """HACK: Refactor this. to smaller methods"""
>     def show_conversation_history(self) -> None:
>         """Display the current conversation history"""
>         print(f"\n📝 Conversation History ({len(self.messages)} messages):")
>         for i, msg in enumerate(self.messages):
>             print(f"  {i+1}. {msg['role'].upper()}: {msg['content'][:100]}{'...' if len(msg['content']) > 100 else ''}")
>         print()
> 
>     def get_conversation_stats(self) -> dict:
>         """Get statistics about the current conversation"""
>         user_messages = [msg for msg in self.messages if msg['role'] == 'user']
>         assistant_messages = [msg for msg in self.messages if msg['role'] == 'assistant']
> 
>         total_chars = sum(len(msg['content']) for msg in self.messages)
> 
>         return {
>             'total_messages': len(self.messages),
>             'user_messages': len(user_messages),
>             'assistant_messages': len(assistant_messages),
>             'total_characters': total_chars,
>             'avg_message_length': total_chars / len(self.messages) if self.messages else 0
>         }
>     def test_timeout(self) -> None:
>         """Test the timeout functionality"""
>         print(f"🧪 Testing {self.name} timeout (set to {self._timeout} seconds)")
>         
>         # Test with a prompt that should complete quickly
>         result = self.ask_with_timeout("Hello, how are you?")
>         print(f"✅ Quick response: {result[:50]}...")
>         
>         # Test with timeout by setting a very short timeout
>         original_timeout = self._timeout
>         self._timeout = 1  # Very short timeout for testing
>         
>         import time
>         start_time = time.time()
>         result = self.ask_with_timeout("Please take your time responding to this question with a long, detailed answer that will definitely exceed the timeout.")
>         end_time = time.time()
>         
>         print(f"⏱️  Timeout test took: {end_time - start_time:.2f} seconds")
>         print(f"📝 Result: {result}")
>         
>         # Restore original timeout
>         self._timeout = original_timeout 
>     @property 
>     def response_time(self) -> float:
>         """Calculate and return the response time for the last interaction"""
>         if self._answer_time > 0 and self._question_asked_time > 0:
>             self._response_time = self._answer_time - self._question_asked_time
>             self._last_answer_time = self._response_time
>             return self._response_time
>         return self._last_answer_time  
> ```

## Methods 
- [[ai-providers#Abstract Methods|Abstract Methods]]
	- [[ai-providers#`ask()`|ask]]
	- [[ai-providers#`name()`|name]]
	- [[ai-providers#`_call_api()`|call_api]]
### Abstract Methods

#### `ask()`

```python
@abstractmethod
def ask(self, prompt: str) -> str:
  """Abstract method that must be implemented by subclasses"""
  # Check for stop signal at the beginning
  if hasattr(self, '_stop_event') and self._stop_event.is_set():
      return "Request was cancelled due to timeout"

  message = {"role": "user", "content": prompt}
  self._messages.append(message)
  # Don't return anything - let subclasses handle the actual response
  return ""  # Return empty string instead of None
```
- This ask automatically adds the user message to the messages list.
- 
#### `name()`

```python
@property
@abstractmethod
def name(self) -> str:
    """Abstract method that must be implemented by subclasses"""
    pass
```
- Just to get the name of your implementation
#### `_call_api()`

```python
@abstractmethod
def _call_api(self, message: list[dict[str, str]] | str) -> str:
    """Abstract method that must be implemented by subclasses to handle actual API calls"""
    pass
```
- Every ai_provider might have different API call mechanism, so you have to implement it youself so that , it can be called by the generic ask method.

##### Why? 
See below example sent by @abhayagovind 

```python
import os
import requests

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN not found.")

url = "https://models.github.ai/inference/chat/completions"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-GitHub-Api-Version": "2023-11-28"
}

messages = [
    {"role": "system", "content": "You are a helpful AI voice/text assistant"}
]

print("🤖 AI Assistant is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break


    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "meta/Llama-4-Scout-17B-16E-Instruct",
        "messages": messages,
        "max_tokens": 500,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload).json()

    ai_reply = response["choices"][0]["message"]["content"]

    print("AI:", ai_reply, "\n")


    messages.append({"role": "assistant", "content": ai_reply})
```

###### Explanation

1. She imports required modules. 
```python
import os
import requests

```
2. Obtains the `GITHUB_TOKEN` from .env file (environment variable)
```python
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN not found.")
```
3. Sets url and headers for the API request
```python
url = "https://models.github.ai/inference/chat/completions"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-GitHub-Api-Version": "2023-11-28"
}
```
4. Creates a message list for history.
```python
messages = [
    {"role": "system", "content": "You are a helpful AI voice/text assistant"}
]
```

5. Uses a while loop and continuesly asks for user input until "exit" or "quit" is typed.
```python
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "meta/Llama-4-Scout-17B-16E-Instruct",
        "messages": messages,
        "max_tokens": 500,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload).json()

    ai_reply = response["choices"][0]["message"]["content"]

    print("AI:", ai_reply, "\n")


    messages.append({"role": "assistant", "content": ai_reply})
```

Features:
1. History is maintained

###### Issues 
1. if the response is is invalid or the API server is down, it will crash.
2. I would have to run this program directly ,

like 
```bash
python llama.py
```

###### Minor Modification 

Lets look at a refactored version



```python
import os
import requests

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN not found.")

url = "https://models.github.ai/inference/chat/completions"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-GitHub-Api-Version": "2023-11-28"
}

messages = [
    {"role": "system", "content": "You are a helpful AI voice/text assistant"}
]

def ask(prompt: str, max_tokens: int = 500, temperature: float = 0.7) -> str:
    user_input = prompt
    if user_input.lower() in ["exit", "quit"]:
        return ""
    messages.append({"role": "user", "content": user_input})
    payload = {
        "model": "meta/Llama-4-Scout-17B-16E-Instruct",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    response = requests.post(url, headers=headers, json=payload).json()
    response.raise_for_status()  
    ai_reply = response["choices"][0]["message"]["content"]

    print("AI:", ai_reply, "\n")

    if len(messages) >= 10:
      messages.pop(1)
    messages.append({"role": "assistant", "content": ai_reply})
    return ai_reply
```

Now the user can import this function 

```python
from llama import ask
answer = ask("What is the capital of France?")
print(f"🤖 Llama > {answer}")
```

^5452c3

Now is simple to use in other projects.

you can customize `max_tokens` and `temperature`.

```python
from llama import ask
answer = ask("What is the capital of France?", max_tokens=1000, temperature=0.5)
print(answer)
````



## Using AIProvider Class

```python
import os
import requests
from typing import Optional

# Custom Imports
try:
    from .ai_providers import AIProvider, AiProviderList, AiProviderStatus
except ImportError:
    from ai_providers import AIProvider, AiProviderList, AiProviderStatus

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

class Llama(AIProvider):
    def __init__(self, token: Optional[str] = GITHUB_TOKEN):
        super().__init__()
        if not token:
            raise ValueError("GITHUB_TOKEN not found.")
        self.token = token
        self.model = "meta/Llama-4-Scout-17B-16E-Instruct"
        self.url = "https://models.github.ai/inference/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-GitHub-Api-Version": "2023-11-28"
        }
        self.add_message("system", "You are a helpful AI voice/text assistant")

    @property
    def name(self) -> str:
        return "GitHub Llama"

    def _call_api(self, message: list[dict[str, str]] | str) -> str:
        """Implementation of the abstract _call_api method for GitHub Llama"""
        try:
            payload = {
                "model": self.model,
                "messages": message if isinstance(message, list) else [{"role": "user", "content": message}],
                "max_tokens": self._max_tokens,
                "temperature": self._temperature
            }

            response = requests.post(self.url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()

            assistant_response = data["choices"][0]["message"]["content"]
            
            if isinstance(message, list):
                self.add_message("assistant", assistant_response)

            return assistant_response

        except requests.RequestException as e:
            self.status = AiProviderStatus.ERROR
            return f"Error communicating with GitHub Llama API: {e}"
        except KeyError as e:
            self.status = AiProviderStatus.ERROR
            return f"Unexpected response format from GitHub Llama API: {e}"

    def ask(self, prompt: str) -> str:
        """Use the generic ask implementation from base class"""
        super().ask(prompt)
        return self._generic_ask(prompt)

    def ask_llama_api(self, message: list[dict[str, str]] | str) -> str:
        """Legacy method - now delegates to _call_api"""
        return self._call_api(message)

```


#### Testing

```python
if __name__ == "__main__":
    print("🤖 Testing GitHub Llama with Memory/Context")
    print("=" * 50)

    questions = [
        "Hello! My name is Arun CS",
        "What's my name?",
    ]

    llama = Llama()

    for i, q in enumerate(questions, 1):
        print(f"\n🐸 Arun > {q}")
        answer = llama.ask(q)
        print(f"🤖 Llama > {answer}")
        print(f"⏳ Response Time {i}: {llama.response_time:.2f} seconds")

    print("\n" + "=" * 50)
    print("📚 FULL CONVERSATION HISTORY:")
    llama.show_conversation_history()

    print("\n📊 CONVERSATION STATISTICS:")
    stats = llama.get_conversation_stats()
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
```

The example below is an example code for Ollama implemented using AIProvider.

```python
if __name__ == "__main__":
    
    print(f"🤖 Testing {str(Ollama.name).capitalize()} with Memory/Context")
    print("=" * 50)

    questions = [
        "Hello! My name is Arun CS",
        "What's my name?",
    ]

    ollama = Ollama()

    for i, q in enumerate(questions, 1):
        print(f"\n🐸 Arun > {q}")
        answer = ollama.ask(q)
        print(f"🤖 Ollama > {answer}")
        print(f"⏳ Response Time {i}: {ollama.response_time:.2f} seconds")

    print("\n" + "=" * 50)
    print("📚 FULL CONVERSATION HISTORY:")
    ollama.show_conversation_history()

    print("\n📊 CONVERSATION STATISTICS:")
    stats = ollama.get_conversation_stats()
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
```

Do you see any difference 

IMPLEMENTATION: `Ollama`

```python
ollama = Ollama()
```

Implementation: `Llama`

```python
llama = Llama()
```


so to use this new implementation with minimal code is.
```python
from ai_providers.llama import Llama
question = "Hello! My name is Arun CS"
llama = Llama()
answer = llama.ask(question)
print(f"🤖 Llama > {answer}")
```


And if you compare it with the refactored version .

![[#^5452c3]]

You can see the refactored one has less code but since its a function , if you want to add more and more ai providers you would have to do this 

```python
from ai_providers.llama import ask as ask_llama
from ai_providers.ollama import ask as ask_ollama
from ai_providers.cohere import ask as ask_cohere

question = "Hello! My name is Arun CS"
answer = ask_llama(question)
print(f"🤖 Llama > {answer}")
answer = ask_ollama(question)
print(f"🤖 Ollama > {answer}")
answer = ask_cohere(question)
print(f"🤖 Cohere > {answer}")
```

and if it was done using the class based approach 

```python
from ai_providers.llama import Llama
from ai_providers.ollama import Ollama
from ai_providers.cohere import Cohere
question = "Hello! My name is Arun CS"
llama = Llama()
ollama = Ollama()
cohere = Cohere()

answer = llama.ask(question)
print(f"🤖 Llama > {answer}")
answer = ollama.ask(question)
print(f"🤖 Ollama > {answer}")
answer = cohere.ask(question)
print(f"🤖 Cohere > {answer}")
```
Both looks same but the class based approach is more extensible and maintainale, for example if you want to ask an ai_provider, randomly you can do this 

```python
import random
from ai_providers.llama import Llama
from ai_providers.ollama import Ollama
from ai_providers.cohere import Cohere

ai_providers = [Llama(), Ollama(), Cohere()]
question = "Hello! My name is Arun CS"
selected_provider = random.choice(ai_providers)
answer = selected_provider.ask(question)
print(f"🤖 {selected_provider.name} > {answer}"  )
``` 

In this way you can easily add more ai providers without changing the code structure.

