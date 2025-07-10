import time

def stream_response(response: str):
    for word in response.split():
        print(word, end=" ", flush=True)
        time.sleep(0.1)
    print()