
from flask import Flask

app = Flask(__name__)

# Route to the root Url
@app.route('/')
def hello():
    return 'Deployed Flask application on Fargate in ECS'

# Route to a custom endpoint Url
@app.route('/greet/<temp>')
def greet(temp):
    return f'{temp}--> This is flask application deployed on Fargate in ECS'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
