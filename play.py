import os
import json

from flask import Flask, request, jsonify
app = Flask(__name__)

code_to_audio = {}
code_to_audio['08436332'] = 'ma'
code_to_audio['08146369'] = 'mi'
code_to_audio['08146355'] = 'ta'


@app.route('/')
def hello():
    os.system("afplay ma.mp3")
    return "Hello World!"

@app.route('/play', methods=['POST'])
def play():
    message = request.json
    code = message["code"]
    os.system("afplay " + code_to_audio[code] + ".mp3")
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
