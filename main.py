import requests
from speech_utils import listen, say

API_URL = "http://localhost:3000/api/v1/prediction/21a6d574-cd2d-4ef9-9b77-ff58c38b8169"
greeting = "Hello, this is Elron's customer service. How can I help you?"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
say(greeting)
while True:
    question = listen()
    say("One second, I'll check the answer for you!")
    output = query({
        "question": question,
    })
    say(output)
    
