from langchain.llms import HuggingFacePipeline
from transformers import pipeline

pipe = pipeline("text-generation", model="gpt2")

llm = HuggingFacePipeline(pipeline=pipe)

response = llm("Explain artificial intelligence in simple words")

print(response)