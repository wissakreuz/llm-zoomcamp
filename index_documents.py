import requests
from elasticsearch import Elasticsearch

# Charger les documents depuis GitHub
docs_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-intro/documents.json?raw=1'
documents_raw = requests.get(docs_url).json()

documents = []
for course in documents_raw:
    course_name = course['course']
    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)

# Connexion à Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Créer l’index s’il n’existe pas
index_name = "faq_docs"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Indexer tous les documents
for i, doc in enumerate(documents):
    es.index(index=index_name, id=i, document=doc)

print(f"{len(documents)} documents indexés dans l’index '{index_name}'")
