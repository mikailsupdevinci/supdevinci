from flask import Flask, jsonify, request

app = Flask(__name__)

# Données pour l'exemple
data = {
    'fruit': 'apple',
    'color': 'red',
    'count': 3
}

@app.route('/mikail', methods=['GET'])
def api():
    if request.method == 'GET':
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)