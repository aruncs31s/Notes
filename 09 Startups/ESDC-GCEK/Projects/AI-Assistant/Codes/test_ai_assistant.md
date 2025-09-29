---
id: test_ai_assistant
aliases: []
tags: []
---

```python

def test_ai_assistant():
    assistant = AIAssistant()
    query = "What is you name?"
    response = assistant.ask(query)
    print(f"🤖 Response from {assistant.ai_provider.name} : {response} \n",
          f"⏳ Response Time: {assistant.ai_provider.response_time} seconds\n")
    print()
    assistant.ai_provider = ai.GPT_5()
    response = assistant.ask(query)
    print(f"🤖 Response from {assistant.ai_provider.name}: {response} \n",
          f"⏳ Response Time: {assistant.ai_provider.response_time} seconds")
    print()

    assistant.ai_provider = ai.CohereAPI()
    response = assistant.ask(query)
    print(f"🤖 Response from {assistant.ai_provider.name}: {response} \n",
          f"⏳ Response Time: {assistant.ai_provider.response_time} seconds")
    print()

    assistant.ai_provider = ai.Gemini()
    response = assistant.ask(query)
    print(f"🤖 Response from {assistant.ai_provider.name}: {response} \n",
          f"⏳ Response Time: {assistant.ai_provider.response_time} seconds")
    print()

if __name__ == "__main__":
    test_ai_assistant()
```
