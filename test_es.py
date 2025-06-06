from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

if es.ping():
    print("✅ Elasticsearch est en ligne !")
    info = es.info()
    print(info)
else:
    print("❌ Impossible de se connecter à Elasticsearch")