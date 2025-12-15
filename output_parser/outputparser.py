from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

from langchain_core.prompts import PromptTemplate


llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
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

pr1= template1.invoke({'topic': 'Sunil Gavaskar'})
res=model.invoke(pr1)
pr2=template2.invoke({'text':res.content})
res2=model.invoke(pr2)
print(res2.content)


