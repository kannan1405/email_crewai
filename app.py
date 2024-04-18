from agent import Agent
from task import Task

 #create filter agent
filter_agent = Agent.email_filter_agent()


#create filter task
email=...
filter_task=Task.filter_emails_task(filter_agent,[])