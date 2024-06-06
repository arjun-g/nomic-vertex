import ollama
from flask import Flask, request, jsonify

app = Flask(__name__)

ollama.pull("nomic-embed-text")

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        instances = request.get_json()["instances"]
        embeddings = []
        for instance in instances:
            embedding = ollama.embeddings(model="nomic-embed-text", prompt=instance["text"])
            embeddings.append(embedding)
        return {"predictions": embeddings}
    except Exception as e:
        return str(e)

@app.route('/healthz')
def healthz():
    return "OK"

if __name__=='__main__':
    app.run(host='0.0.0.0')