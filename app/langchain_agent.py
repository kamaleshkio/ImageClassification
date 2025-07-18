from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
from classify_tool import classify_image

oil_tool = Tool(
    name="OilDropImageClassifier",
    description="Classifies uploaded oil drop image into Stage 1–5 based on quality.",
    func=classify_image
)

llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools=[oil_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    user_input = "Classify this oil drop image: input.jpg"
    print(agent.run(user_input))
