import requests
import time
from speech_utils.speech_to_text import listen
from speech_utils.text_to_speech import say

API_URL = "http://localhost:3000/api/v1/prediction/21a6d574-cd2d-4ef9-9b77-ff58c38b8169"
greeting = "Hello, this is Elron's customer service. How can I help you?"
show_latency = True

def query(payload):
    start_time = time.time()
    response = requests.post(API_URL, json=payload)

    if show_latency:
        print(f"Latency: {time.time() - start_time} seconds")

    return response.json()
    
say(greeting)
while True:
    question = listen()
    say("One second, I'll check the answer for you!")
    
    output = query({
        "question": question,
    })
    say(output)
    
