from crewai import Task
from textwrap import dedent

class Task():
    def filter_emails_task(agent,emails):
        return Task(descroption=dedent(f"""\
            Analyze a batch of emails and filter out 
            non-essential ones such as newsletters ,promotional content and notifications.
            
            use your experties in email content analysis to distinguish
            import emails from the rest,pay attention to the sender and avoind emails.
                                       
            Make sure to filter for the messages actually directed at the user and avoid notification .
             
            EMAIL
             _______________________________________________________
                                       {emails}                                                                                          
              your final answer Must be a the releva nt thread_ids and the sender ,use bullet points.                                       """),
              agent=agent)
