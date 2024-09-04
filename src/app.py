from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    {
        "label": "Sample Todo 1",
        "done": True
    }
]





@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(todos), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)









