from flask import Flask

app = Flask(__name)

@app.route('/')
def hello():
    return "Hello, World! This is my Python web app."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
