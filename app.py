#importing libraries
from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import gradio as gr
from groq import RateLimitError
from dotenv import load_dotenv
import time

import os

#loading the api key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
# Debugging the API key
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not set or loaded. Check your .env file.")

#creating the finance agent
finance_agent = Agent(
    name = "Finance Agent",
    model = Groq(
        id ="llama-3.3-70b-versatile"
    ),
    tools = [YFinanceTools(stock_price= True, analyst_recommendations= True, stock_fundamentals = True)],
    show_tool_calls = True,
    markdown = True,
    instructions = ["use tables to display data"],
)

#initializing the websearch_agent
web_agent = Agent(
    name = "Web Agent",
    model = Groq(
        id ="llama-3.3-70b-versatile"
    ),
    tools = [DuckDuckGo()],
    show_tool_calls = True,
    markdown = True,
    instructions = ["always include sources"],
)

#initializing the team agent
agent_team = Agent(
    team = [finance_agent, web_agent],
    model = Groq(
        id ="llama-3.3-70b-versatile"
    ),
    show_tool_calls = True,
    markdown = True,
    instructions = ["use tables to display data" , "always include sources"],
)

#getting the stock comparisons
def stock_input(stock1, stock2):
    try:
        agent_team.print_response(f"Summarize and compare analyst recommendations & fundamentals for {stock1} and {stock2}. Make the summary short.")
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}. Retrying after a delay...")
        time.sleep(7 * 60 + 41)  # Wait for the specified time
    #agent_team.print_response(f"Summerize and compare analyst recommendations & fundamentals for {stock1} and {stock2}.")

#Build the Gradio interface
interface = gr.Interface(
    fn=stock_input,
    theme='Yntec/HaleyCH_Theme_Orange_Green',
    inputs=[
        gr.Textbox(label="Enter the first stock"),
        gr.Textbox(label="Enter the second stock"),
    ],
    outputs=gr.Textbox(label="Generated comparison"),
    title="Stock comparisons",
    description="Enter two stocks you want to compare."
)

#Launch the Gradio application
interface.launch()