from flask import Flask
from processing.log_file_processor import LogFileProcessor

app = Flask(__name__)
process = LogFileProcessor()
response = process.start()

@app.route("/games")
def games():
    return response

@app.route("/games/<id>")
def game(id):
    return response[f'game_{id}']

if __name__ == "__main__":
    app.run()
