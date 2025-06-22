from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Brownies Café Bot is running!"

def keep_alive():
    thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8080})
    thread.start()
