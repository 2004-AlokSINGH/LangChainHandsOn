import requests
from langchain.tools import tool
from app.config import (
    JIRA_BASE_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN,
    JIRA_PROJECT_KEY
)



@tool
def create_jira_ticket(summary: str, description: str) -> str:
    """Create a Jira ticket and return ticket key"""

    url = f"{JIRA_BASE_URL}/rest/api/2/issue"

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Bug"}
        }
    }

    response = requests.post(
        url,
        json=payload,
        auth=(JIRA_EMAIL, JIRA_API_TOKEN),  # type: ignore
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()
    return response.json()["key"]
