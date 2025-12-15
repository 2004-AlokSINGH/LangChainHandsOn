from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
    )
)

model = ChatHuggingFace(llm=llm)

# schema = [
#     ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
#     ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
#     ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
# ]

# parser = StructuredOutputParser.from_response_schemas(schema)


# for this
# pip uninstall -y langchain langchain-core
# pip install "langchain==0.1.20" "langchain-core==0.1.52"




template = PromptTemplate(
    template="Give 3 fact about {topic}\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)
