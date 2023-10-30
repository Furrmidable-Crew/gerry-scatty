from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date

class MySettings(BaseModel):
    required_int: int
    optional_int: int = 69
    required_str: str
    optional_str: str = "meow"
    required_date: date
    optional_date: date = 1679616000

@plugin
def settings_schema():   
    return MySettings.schema()

@tool
def get_the_day(tool_input, cat):
    """Get the day of the week. Input is always None."""

    dt = datetime.now()

    return dt.strftime('%A')

@hook
def agent_prompt_prefix(prefix, cat):
    prefix = """You are Gerry Scatty the cat version of Gerry Scotti a famous italian television anchorman.
    He's famous because his style is familiar, he's also called 'the uncle Gerry'.
    You are the presenter of the cat version of 'Who Wants To Be a Millionaire?' and the user is the player. 
    Chat with the player using Gerry Scotti's style, emphathizes with the player and be gentle. 
    Ask a question, check the answer and explain the right answer. 
    Then ask to the player if he wants another question, if its answer is negative thanks him and goodbye.
    Ask a question and give the four options for the answer like in trivia game.
    Remember, you MUSTN'T talk about money, this game is only for fun.
"""
    return prefix


@hook
def before_cat_sends_message(message, cat):

    prompt = f'Rephrase the following sentence in Gerry Scotti style: {message["content"]}'
    message["content"] = cat.llm(prompt)

    return message
