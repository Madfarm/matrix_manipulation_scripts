from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "I'm an API in Python!"})

if __name__ == '__main__':
    app.run(debug=True)