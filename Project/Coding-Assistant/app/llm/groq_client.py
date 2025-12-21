from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY
from app.schemas import debug_schema

def get_llm():
    model= ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=GROQ_API_KEY # type: ignore
    )
    return model.with_structured_output(debug_schema.DebugResult)
