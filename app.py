from langchain_anthropic import ChatAnthropic

from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl

from _utils import read_markdown_file


@cl.on_chat_start
async def on_chat_start():
    # model = ChatOpenAI(streaming=True)
    model = ChatAnthropic(model='claude-3-5-sonnet-20240620', stream=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                read_markdown_file("prompt/peddesign-prompt.md"),
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)



@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Quick Start",
            message="Hi, Who are you and how do I use you?",
            icon="/public/lightbulb.svg",
            ),

        cl.Starter(
            label="Example: Chest CT",
            message="Chest CT, 5 years, BW 18 kg, First study, IV No. 22",
            icon="/public/pen.svg",
            ),
        
        cl.Starter(
            label="Example: CTWA",
            message="CTWA, 10 year, BW 30 kg, Delay 65 sec, Not first study, IV No. 22",
            icon="/public/pen.svg",
            ),
        ]
# ...


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
