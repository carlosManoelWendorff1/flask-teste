from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def my_endpoint():
    # Extract data from the POST request
    data = request.get_json()
    name = data['name']
    age = data['age']

    # Process the data (for example, store it in a database)
    # ...

    # Return a JSON response
    response = {
        'message': f'Hello, {name}! You are {age} years old.',
        'status': 'success'
    }
    return jsonify(response)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    print("\n Rodando aplicação ...")
    app.run()
    print("Aplicação rodo")
    print("\n\n\n\n  👌👌👌👌👌👌👌👌👌")