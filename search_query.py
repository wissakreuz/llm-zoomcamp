from elasticsearch import Elasticsearch

# Connexion à Elasticsearch (assure-toi que le serveur est bien en cours d'exécution)
es = Elasticsearch("http://localhost:9200")

# Requête à exécuter
query_text = "How do execute a command on a Kubernetes pod?"

# Exécution de la recherche
response = es.search(
    index="faq_docs",  # Utilise le même nom d'index que lors de l'indexation
    query={
        "multi_match": {
            "query": query_text,
            "fields": ["question^4", "text"],
            "type": "best_fields"
        }
    }
)

# Affichage du score et de la question correspondante
top_hit = response["hits"]["hits"][0]
print("Top score:", top_hit["_score"])
print("Top result question:", top_hit["_source"]["question"])
