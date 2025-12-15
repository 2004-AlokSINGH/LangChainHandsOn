from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Load small open-source model
llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceTB/smol-llm2-360m-instruct",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200,
    }
)

model = ChatHuggingFace(llm=llm)

# Schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="Return sentiment of the review")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

# IMPORTANT: enforce strict JSON mode for small models
structured_model = model.with_structured_output(Review, strict=True)

# Run
result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse...
Review by Nitish Singh
""")

print(result)
