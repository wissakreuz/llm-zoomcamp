#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('curl -k -O https://raw.githubusercontent.com/alexeygrigorev/minsearch/main/minsearch.py')


# In[2]:


import minsearch


# In[3]:


import json


# In[4]:


with open('documents.json', 'rt') as f_in:
    docs_raw = json.load(f_in)


# In[5]:


documents = []

for course_dict in docs_raw:
    for doc in course_dict['documents']:
        doc['course'] = course_dict['course']
        documents.append(doc)


# In[6]:


documents[0]


# In[7]:


index = minsearch.Index(text_fields=["question", "text", "section"],
        keyword_fields = ["course"]
)


# In[8]:


#SELECT * WHERE course = 'data-engineering-zoomcamp';


# In[9]:


q = 'the course has already started, can I still enroll?' 


# In[10]:


index.fit(documents)


# In[11]:


boost = {'question': 3.0, 'section': 0.5}

results = index.search(
    query=q,
    filter_dict={'course': 'data-engineering-zoomcamp'}, 
    boost_dict=boost,
    num_results=5

)


# In[12]:


results


# In[13]:


import os
from dotenv import load_dotenv
from openai import OpenAI


# In[14]:


# Charge le fichier .env (doit être dans le même dossier que ce script)
load_dotenv()


# In[15]:


# Récupère la clé
api_key = os.getenv("OPENAI_API_KEY")


# In[16]:


# Vérifie que la clé est bien chargée
if api_key is None:
    raise ValueError("OPENAI_API_KEY is not défini. Vérifie ton fichier .env.")


# In[17]:


# Crée le client
client = OpenAI(api_key=api_key)


# In[18]:


q


# In[19]:


response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{"role": "user", "content": q}]
)

response.choices[0].message.content


# In[20]:


prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database. 
Use only the facts from the CONTEXT when answering the QUESTION.
If the CONTEXT doesn't contain the answer, output NONE

QUESTION: {question}
CONTEXT: 
{context}
""".strip()

context = ""

for doc in results:
    context += f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"

prompt = prompt_template.format(question=q, context=context).strip()


# In[24]:


response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{"role": "user", "content": prompt}]
)

response.choices[0].message.content


# In[26]:


def search(query):
    boost = {'question': 3.0, 'section': 0.5}

    results = index.search(
        query=query,
        filter_dict={'course': 'data-engineering-zoomcamp'}, 
        boost_dict=boost,
        num_results=5

    )

    return results


# In[55]:


def build_prompt(query, search_results):

    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database. 
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = ""

    for doc in search_results:
        context += f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"

    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt


# In[56]:


def llm(prompt):  
    response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{"role": "user", "content": prompt}]
)

    return response.choices[0].message.content


# In[57]:


query = 'how do I run kafka?'

def rag(query):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer


# In[60]:


rag(query)


# In[ ]:


rag('the course has already started; can I still enroll?')

