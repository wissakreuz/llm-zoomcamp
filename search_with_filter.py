from elasticsearch import Elasticsearch

def search_in_ml_zoomcamp():
    es = Elasticsearch("http://localhost:9200")

    query_text = "How do copy a file to a Docker container?"

    response = es.search(
        index="faq_docs",
        size=3,
        query={
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query_text,
                        "fields": ["question^4", "text"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {"course.keyword": "machine-learning-zoomcamp"}
                }
            }
        }
    )

    hits = response["hits"]["hits"]

    for i, hit in enumerate(hits, 1):
        print(f"{i}. {hit['_source']['question']}")

    print("\nQuestion numéro 3 :", hits[2]["_source"]["question"])

if __name__ == "__main__":
    search_in_ml_zoomcamp()
