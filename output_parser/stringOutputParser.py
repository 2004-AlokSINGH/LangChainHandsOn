from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0', # can use other open source model
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        # max_new_tokens=500
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

template1=PromptTemplate(
    template="Write a detailed report on following topic {topic}",
    input_variables=['topic']
)


template2=PromptTemplate(
    template="Write a 5 line summary on following text \n {text}",
    input_variables=['text']
)

parser=StrOutputParser()
chain= template1 | model | parser | template2 | model | parser
res=chain.invoke({'topic': 'India Gate'})

print(res)

