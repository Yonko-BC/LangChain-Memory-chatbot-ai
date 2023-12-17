from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

import os
def main():
    load_dotenv()
    # test api key
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
        # raise Exception("OPENAI_API_KEY is not set")
    else:
        print("OPENAI_API_KEY is set")
    
    # create chat model
    chat = ChatOpenAI(temperature=0.4)

    messages = [
        SystemMessage(content="Act like a helpful marketer"),
    ]
    
    while True:
        user_input = input("Me : ")
        messages.append(HumanMessage(content=user_input))
        ai_response = chat(messages)
        messages.append(AIMessage(content=ai_response.content))
        print("AI : ", ai_response.content)



if __name__ == "__main__":
    main()