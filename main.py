from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables d'environnement depuis .env

api_key = os.getenv("OPENAI_API_KEY")

print("Clé API chargée :", api_key)  # Juste pour vérifier, à supprimer ensuite


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Docker + FastAPI!"}
