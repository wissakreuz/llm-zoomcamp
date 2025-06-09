from elasticsearch import Elasticsearch

# Connexion à Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Requête Elasticsearch - prendre 3 résultats
response = es.search(
    index="faq_docs",
    size=3,
    query={
        "multi_match": {
            "query": "How do execute a command on a Kubernetes pod?",
            "fields": ["question^4", "text"],
            "type": "best_fields"
        }
    }
)

# Template pour chaque entrée de contexte
context_template = """
Q: {question}
A: {text}
""".strip()

# Construire le contexte avec les résultats
context_entries = []
for hit in response["hits"]["hits"]:
    question = hit["_source"]["question"]
    text = hit["_source"]["text"]
    context_entries.append(context_template.format(question=question, text=text))

context = "\n\n".join(context_entries)

# Template pour le prompt complet
prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

# Question finale
question = "How do I execute a command in a running docker container?"

# Construire le prompt final
prompt = prompt_template.format(question=question, context=context)

# Afficher la longueur du prompt
print(prompt)
print("Prompt length:", len(prompt))

