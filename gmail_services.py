from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch
from langchain_community.tools.gmail.utils import(
    build_resource_service,
    get_gmail_credentials
)


crendentials=get_gmail_credentials(
    token_file="token.json",
     scopes=["https://mail.google.com/"],
     client_secrets_file="credentials.json",
)

api_resource = build_resource_service(crendentials=crendentials)

search = GmailSearch(api_resource=api_resource)

emails = search("in:inbox")

mails=[]

for email in emails:
    mails.append({
        "id":email["id"],
        "threadid":email["threadId"],
        "snippet":email["snippet"],
        "sender":email["sender"]

    })

    print(mails)