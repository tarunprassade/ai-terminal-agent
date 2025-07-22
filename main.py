from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

# Load your environment variables
load_dotenv()

def main():
    print("KEY:", os.getenv("OPENROUTER_API_KEY")[:10] + "...")

    # Use ChatOpenAI with OpenRouter setup
    model = ChatOpenAI(
        temperature=0,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_BASE_URL"),
        model_name=os.getenv("OPENROUTER_MODEL")
    )

    tools = []
    agent_excutor = create_react_agent(model, tools)
    print("welcome to my first hands-on \"AI\" project!!!!!!")
    print("try some calculations out or lets just chat")

    while True:
        user_input = input("\n you: ").strip()
        if user_input.lower() == "quit":
            break
        print("\n Assistant:", end="")
        for chunk in agent_excutor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
