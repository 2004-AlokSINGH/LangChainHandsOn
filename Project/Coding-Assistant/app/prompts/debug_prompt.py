from langchain_core.prompts import PromptTemplate,ChatPromptTemplate


DEBUG_PROMPT = PromptTemplate(
    input_variables=["log"],
    template="""
You are a senior SRE.

Analyze the following log or error and:
1. Classify the error type
2. Identify root cause
3. Suggest concrete fixes
4. Decide whether a Jira ticket is required

Log:
{log}

Respond strictly in structured format.
"""
)