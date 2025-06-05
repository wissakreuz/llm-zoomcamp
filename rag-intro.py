#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('curl -k -O https://raw.githubusercontent.com/alexeygrigorev/minsearch/main/minsearch.py')


# In[8]:


import minsearch


# In[9]:


import json


# In[10]:


with open('documents.json', 'rt') as f_in:
    docs_raw = json.load(f_in)


# In[11]:


documents = []

for course_dict in docs_raw:
    for doc in course_dict['documents']:
        doc['course'] = course_dict['course']
        documents.append(doc)


# In[12]:


documents[0]


# In[18]:


index = minsearch.Index(text_fields=["question", "text", "section"],
        keyword_fields = ["course"]
)


# In[19]:


#SELECT * WHERE course = 'data-engineering-zoomcamp';


# In[20]:


q = 'the course has already started, can I still enroll?' 


# In[21]:


index.fit(documents)


# In[24]:


boost = {'question': 3.0, 'section': 0.5}

results = index.search(
    query=q,
    filter_dict={'course': 'data-engineering-zoomcamp'}, 
    boost_dict=boost,
    num_results=5

)


# In[25]:


results


# In[ ]:




