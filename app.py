from distutils.log import debug
from email import message
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

from chat import get_response

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    # app.run()
    app.run(debug=True)

    
