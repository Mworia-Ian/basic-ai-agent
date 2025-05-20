# 💬 LangChain React Agent CLI Assistant

This is a simple command-line AI assistant built with [LangChain](https://www.langchain.com/), using the **React Agent** architecture to integrate an LLM (DeepSeek Chat) and a custom tool (a calculator). The assistant can perform basic arithmetic and engage in natural language conversation.

---

## 🛠 Features

- 💡 Uses `deepseek-chat` as the language model via OpenAI-compatible API.
- 🧮 Includes a custom `calculator` tool for basic arithmetic operations.
- ⚙️ Uses LangChain's `create_react_agent` to automatically invoke tools.
- 🖥️ Interactive command-line interface for chatting with the agent.

---

## 📦 Requirements

- Python 3.8+
- Dependencies:
  - `langchain-core`
  - `langchain-openai`
  - `langchain`
  - `langgraph`
  - `python-dotenv` (optional, for loading environment variables)

### Install dependencies

```bash
pip install langchain-core langchain-openai langchain langgraph python-dotenv
```

- Set your DeepSeek API key in your environment:

```bash
export DEEPSEEK_API_KEY="your_deepseek_api_key"
```

## 🚀 Running the Assistant

```bash
uv run main.py
```
