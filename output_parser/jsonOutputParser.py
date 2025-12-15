from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StructuredOutputParser


llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama\TinyLlama-1.1B-Chat-v1.0', # can use other open source model
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        # max_new_tokens=500
    )
)
model = ChatHuggingFace(llm=llm)
parser=JsonOutputParser()

template1=PromptTemplate(
    template="give me name, age and city of fictional person \n {format}",
    input_variables=[],
    partial_variables={'format':parser.get_format_instructions()}
)

# prompt=template1.format()
# result=model.invoke(prompt)
# print(result)
# final_res=parser.parse(result.content)
# print(final_res)



chain = template1 | model | parser
result=chain.invoke({})
print(result)


# problem -- it does not enforce any json schema.
# for that we need strutcuredOutputParser