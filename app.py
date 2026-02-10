# AI Disclosure: Google Gemini was used to explain some one-line code and debug


# Import necessary modules from Flask
# Flask: the core framework for the web app
# jsonify: to convert Python dictionaries to JSON responses
# request: to access incoming request data (e.g., POST data)
# abort: to handle errors and send error status codes
from flask import Flask, jsonify, request, abort
from flask_cors import CORS  # Enable Cross-Origin Resource Sharing for client apps

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS so the HTML client can connect from a browser
# This allows requests from different origins (e.g., file:// or another port)
CORS(app)

# In-memory "database" of users
# This list holds a set of user dictionaries. 
# In a real-world application, this would be replaced by a database such as MySQL, PostgreSQL, or MongoDB.
users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
]

tasks = [
    {"id": 1, "title": "Learn REST", "description": "Study REST principles", "user_id": 1, "completed": True},
    {"id": 2, "title": "Build API", "description": "Complete the assignment", "user_id": 2, "completed": False},
]

# Define route to handle requests to the root URL ('/')
@app.route('/')
def index():
    return "Welcome to Flask REST API Demo! Try accessing /users to see all users."

# Health check route (GET)
# This endpoint returns a 200 OK status and a JSON response to confirm that the service is running.
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200  # Return HTTP status 200 OK

# Task resource
# Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Retrieve a single task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for task in tasks:
        if task['id'] == id:
            return jsonify(task), 200
    abort(404)

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    user_exists = False
    if not data or 'title' not in data or 'user_id' not in data:
        abort(400)
    for user in users:
        if data['user_id'] == user['id']:
            user_exists = True
            break
    if not user_exists:
        abort(400)
    if tasks:
        new_id = tasks[-1]['id'] + 1
    else:
        new_id = 1
    new_task = {
        "id": new_id,
        "title": data['title'],
        "description": data.get('description', ""),
        "user_id": data['user_id'],
        "completed": data.get('completed', False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Update an existing task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    target_task = None
    data = request.get_json()
    for task in tasks:
        if task['id'] == id:
            target_task = task
            break
    if target_task is None:
        abort(404)
    if data is None:
        abort(400)
    target_task['title'] = data.get('title', target_task['title'])
    target_task['description'] = data.get('description', target_task['description'])
    target_task['completed'] = data.get('completed', target_task['completed'])

    return jsonify(target_task), 200

# Delete a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    updated_tasks = []
    for task in tasks:
        if task['id'] != id:
            updated_tasks.append(task)
    tasks = updated_tasks
    return '', 204

# Route to retrieve all users (GET request)
# When the client sends a GET request to /users, this function will return a JSON list of all users.
# The @ symbol in Python represents a decorator. 
# In this case, @app.route is a Flask route decorator.
# It is used to map a specific URL (route) to a function in your Flask application.
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200  # 200 is the HTTP status code for 'OK'

# Route to retrieve a single user by their ID (GET request)
# When the client sends a GET request to /users/<id>, this function will return the user with the specified ID.
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Using a list comprehension to find the user by ID
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)  # If the user is not found, return a 404 error (Not Found)
    return jsonify(user), 200  # Return the user as a JSON object with a 200 status code (OK)

# Route to create a new user (POST request)
# When the client sends a POST request to /users with user data, this function will add the new user to the list.
@app.route('/users', methods=['POST'])
def create_user():
    # If the request body is not in JSON format or if the 'name' field is missing, return a 400 error (Bad Request)
    if not request.json or not 'name' in request.json:
        abort(400)
    
    # Create a new user dictionary. Assign the next available ID by incrementing the highest current ID.
    # If no users exist, the new ID will be 1.
    new_user = {
        'id': users[-1]['id'] + 1 if users else 1,
        'name': request.json['name'],  # The name is provided in the POST request body
        'age': request.json.get('age', 0)  # The age is optional; default is 0 if not provided
    }
    # Add the new user to the users list
    users.append(new_user)
    return jsonify(new_user), 201  # 201 is the HTTP status code for 'Created'

# Route to update an existing user (PUT request)
# When the client sends a PUT request to /users/<id> with updated user data, this function will update the user.
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Find the user by their ID
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)  # If the user is not found, return a 404 error (Not Found)
    
    # If the request body is missing or not in JSON format, return a 400 error (Bad Request)
    if not request.json:
        abort(400)
    
    # Update the user's data based on the request body
    # If a field is not provided in the request, keep the existing value
    user['name'] = request.json.get('name', user['name'])
    user['age'] = request.json.get('age', user['age'])
    return jsonify(user), 200  # Return the updated user data with a 200 status code (OK)

# Route to delete a user (DELETE request)
# When the client sends a DELETE request to /users/<id>, this function will remove the user with that ID.
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users  # Reference the global users list
    # Rebuild the users list, excluding the user with the specified ID
    users = [user for user in users if user['id'] != user_id]
    return '', 204  # 204 is the HTTP status code for 'No Content', indicating the deletion was successful

# Add a User-Tasks Endpoint
# Add an endpoint to retrieve all tasks assigned to a specific user:
@app.route('/users/<int:user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id):
    user_exists = False
    tasks_list = []
    for user in users:
        if user['id'] == user_id:
            user_exists = True
            break
    if not user_exists:
        abort(404)
    for task in tasks:
        if task['user_id'] == user_id:
            tasks_list.append(task)
    return jsonify(tasks_list), 200

# Entry point for running the Flask app
# The app will run on host 0.0.0.0 (accessible on all network interfaces) and port 8000.
# Debug mode is disabled (set to False).
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)