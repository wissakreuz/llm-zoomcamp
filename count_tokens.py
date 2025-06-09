import tiktoken

# Charger l'encodage du modèle GPT-4o (ou autre)
encoding = tiktoken.encoding_for_model("gpt-4o")

# Supposons que 'prompt' est ta chaîne de caractères (le prompt complet)
prompt = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: How do I execute a command in a running docker container?

CONTEXT:
Q: How do I debug a docker container?
A: Launch the container image in interactive mode and overriding the entrypoint, so that it starts a bash command.
docker run -it --entrypoint bash <image>
If the container is already running, execute a command in the specific container:
docker ps (find the container-id)
docker exec -it <container-id> bash
(Marcos MJD)

Q: Kubernetes-dashboard
A: Deploy and Access the Kubernetes Dashboard
Luke

Q: How do I copy files from a different folder into docker container’s working directory?
A: You can copy files from your local machine into a Docker container using the docker cp command. Here's how to do it:
In the Dockerfile, you can provide the folder containing the files that you want to copy over. The basic syntax is as follows:
COPY ["src/predict.py", "models/xgb_model.bin", "./"]                                                                                   Gopakumar Gopinathan
"""

# Encodage en tokens
tokens = encoding.encode(prompt)

print("Number of tokens:", len(tokens))
