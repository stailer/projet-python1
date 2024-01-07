import requests
import json

def send_post_request(url, data, chunk_size=8192):
    try:
        response = requests.post(url, json=data, stream=True)

        if response.status_code == 200:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    yield chunk.decode('utf-8')
        else:
            print(f"Échec de la requête, statut : {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")



url = "http://host.docker.internal:11434/api/generate"
data = {
    "prompt": "donne moi une liste des 5 plus hauts sommets du monde ?",
    "model": "mistral",  
}

for content in send_post_request(url, data):
    try:
        content_obj = json.loads(content)
        response_data = content_obj.get('response', '')

        print(response_data, end='')
    except json.JSONDecodeError:
        print("Erreur lors de la conversion de la réponse en JSON")
