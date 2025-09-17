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

Now look at the refactored version with less `print()` statements 


###### Issues 
1. 

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

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
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
    messages.append({"role": "assistant", "content": ai_reply})
```