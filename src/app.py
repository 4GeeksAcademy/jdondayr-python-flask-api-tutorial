from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Get all todos
@app.route("/todos")
def get_todos():
    return jsonify(todos)

# Post a todo
@app.route("/todos", methods=["POST"])
def post_a_todo():
    body = request.get_json()
    new_todo = {
        "label": body["label"],
        "done": body["done"]
    }
    todos.append(new_todo)
    return jsonify(todos)

# Delete a todo
@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_a_todo(position):
    if position >= len(todos): # user can't use positions that doesn't exist
        return jsonify("Position doesn't exist"), 400
    todo_to_delete = todos[position]
    todos.remove(todo_to_delete)
    return jsonify(f"todo in position {position} deleted successfully")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
