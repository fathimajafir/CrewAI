from crewai import Crew,Process
from task import research_task,write_task
from agents import climate_researcher, climate_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[climate_researcher,climate_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Carbon Capture and Storage (CCS) Technologies'})
print(result)