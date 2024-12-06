from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to my simple flask page!</h1><p> I am Arshdeep Kour.</p>"

if __name__ == '__main__':
    app.run(debug=True)
