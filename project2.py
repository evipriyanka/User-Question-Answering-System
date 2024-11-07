# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15xjflN5egbLrq-CXhAP8FF3invDXu8oz
"""

!pip install transformers torch kagglehub

import kagglehub
import os
from transformers import BertTokenizer, BertForQuestionAnswering, pipeline
import json

# Step 1: Download the dataset using kagglehub
path = kagglehub.dataset_download("stanfordu/stanford-question-answering-dataset")
print("Path to dataset files:", path)

# Load the dataset
with open(os.path.join(path, 'train-v1.1.json')) as f:
    squad_data = json.load(f)

# Step 2: Load pre-trained BERT model for Question Answering
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-large-uncased')

# Step 3: Create a question-answering pipeline
qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)

# Step 4: Function to get context based on the user's question
def get_context(user_question):
    # This function can be expanded to match the user's question to the context.
    # Here, we simply return the first context paragraph as a default.
    context = squad_data['data'][0]['paragraphs'][0]['context']
    return context

# Step 5: Get user input and answer the question
user_question = input("Please ask a question: ")
context = get_context(user_question)  # Get the context based on the question

qa_input = {
    'question': user_question,
    'context': context
}

# Step 6: Get the answer
answer = qa_pipeline(qa_input)
print(f"Answer: {answer['answer']}")