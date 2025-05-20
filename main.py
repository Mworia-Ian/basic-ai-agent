from langchain_core.messages  import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

import os

@tool
def calculator(a: float, b: float) -> str:
    """Useful for doing basic arithmetic calculations with numbers"""
    print("Tool has been called")
    return f"the sum of {a} and {b} is {a + b}"


def main():
    model = ChatOpenAI(
        temperature=0,
        model="deepseek-chat",
        openai_api_base="https://api.deepseek.com/v1",  
        openai_api_key=os.getenv("DEEPSEEK_API_KEY")    
    )

    tools = [calculator]
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I am your Ai assistant. Type 'q' to exit")
    print("You can ask me to perform calculations or chat with me.")

    while True: 
        user_input = input("\nYou: ").strip()

        if user_input == "q":
            break

        print("\nAssistant: ", end="")

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
