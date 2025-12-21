from langchain.tools import tool

@tool
def classify_error(log: str) -> str:
    """Classify error as DATABASE, API, AUTH, INFRA, LOGIC"""
    if "timeout" in log.lower():
        return "INFRA"
    if "sql" in log.lower():
        return "DATABASE"
    return "APPLICATION"
