from flask import Flask, jsonify, request

# Create the app
app = Flask(__name__)

# Home route
# @app.route("/")
# def home():
#     return "Hello, World! Welcome to my first Flask API 😊"

@app.route("/")
def home():
    return """
        <h1>Welcome!</h1>
        <p>This is HTML coming from Flask.</p>
    """


# Simple API returning data
@app.route("/user")
def user_info():
    data = {"name": "Richard", "age": 25, "city": "Chennai"}
    return jsonify(data)

# API with URL parameter
@app.route("/hello/<name>")
def say_hello(name):
    return f"Hello {name}, welcome to the Flask API!"

# API using query parameters ( ?x=10&y=20 )
@app.route("/add")
def add_numbers():
    x = request.args.get("x", default=0, type=int)
    y = request.args.get("y", default=0, type=int)
    return jsonify({"x": x, "y": y, "result": x + y})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
