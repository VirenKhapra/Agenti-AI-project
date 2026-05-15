from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_groq import ChatGroq

from tools import email_tool, llm_tool, validator_tool

# LLM
llm = ChatGroq(
    groq_api_key="api key",
    model_name="llama-3.3-70b-versatile"
)

# Tool List
tools = [email_tool, llm_tool,validator_tool]

# ReAct Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run Agent
response = agent.run(
    "Fetch the latest financial email and extract structured transaction details."
)

print("\n FINAL OUTPUT:\n")
print(response)
