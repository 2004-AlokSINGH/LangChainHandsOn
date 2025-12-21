# from langchain_core.runnables import RunnableLambda
# from app.llm.groq_client import get_llm
# from app.prompts.debug_prompt import DEBUG_PROMPT
# from app.schemas.debug_schema import DebugResult
# from app.tools.jiracreator import create_jira_ticket

# llm = get_llm()  

# # ---- Chain definition (Prompt → Structured LLM) ----
# debug_chain = DEBUG_PROMPT | llm

# # ---- Post-processing step (side effects like Jira) ----
# def jira_enrichment(result: DebugResult) -> DebugResult:
#     if result.jira_ticket_required:
#         ticket_id = create_jira_ticket(summary=f"{result.error_type} issue detected", description=result.root_cause)

#         result.jira_ticket_id = ticket_id
#     return result



# final_chain = debug_chain | RunnableLambda(jira_enrichment)

# # ---- Public API ----
# def run_debug(log: str) -> DebugResult:
#     return final_chain.invoke({"log": log})



from langchain_core.runnables import RunnableLambda
from app.llm.groq_client import get_llm
from app.prompts.debug_prompt import DEBUG_PROMPT
from app.schemas.debug_schema import DebugResult
from app.tools.jiracreator import create_jira_ticket

llm = get_llm()

# ---- Prompt → Structured LLM ----
debug_chain = DEBUG_PROMPT | llm

# ---- Post-processing (side effects only) ----
def jira_enrichment(result: DebugResult) -> DebugResult:
    if result.jira_ticket_required:
        ticket_id = ticket_id = create_jira_ticket.invoke({
            "summary": f"{result.error_type} issue detected",
            "description": result.root_cause
        })
        result.jira_ticket_id = ticket_id
    return result

final_chain = debug_chain | RunnableLambda(jira_enrichment)

def run_debug(log: str) -> DebugResult:
    return final_chain.invoke({"log": log})
