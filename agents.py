from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

climate_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover groundbreaking technologies in climate change mitigation',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by a passion for the environment, you're dedicated to exploring"
        "innovative solutions that can combat climate change and make a positive"
        "impact on the planet."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

climate_writer = Agent(
  role='Writer',
  goal='Narrate compelling stories about climate change innovations',
  verbose=True,
  memory=True,
  backstory=(
    "With a talent for translating complex environmental science into"
    "engaging content, you create narratives that inspire action and"
    "raise awareness about critical climate issues."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
