from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return {"status": "ok", "message": "Hello from egy_discovery!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
