from crewai import Task
from tools import tool
from agents import climate_researcher, climate_writer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in climate change mitigation."
    "Focus on the technological advancements, their pros and cons,"
    "and the overall impact on the environment and society."
    "Your final report should clearly articulate the key innovations,"
    "market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3-paragraph report on the latest trends in climate change mitigation technologies.',
  tools=[tool],
  agent=climate_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on climate change innovations."
    "Focus on the latest advancements and their positive impact on the environment."
    "This article should be easy to understand, engaging, and optimistic."
  ),
  expected_output='A 4-paragraph article on climate change advancements formatted as markdown.',
  tools=[tool],
  agent=climate_writer,
  async_execution=False,
  output_file='climate-change-article.md'  # Example of output customization
)
