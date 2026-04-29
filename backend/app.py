from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app)


# 🔍 LANGUAGE DETECTION
def detect_language(code):
    code_lower = code.lower()

    if "#include" in code_lower or "std::" in code_lower or "cout" in code_lower:
        return "C++"
    if "def " in code_lower and ":" in code_lower:
        return "Python"
    if "public class" in code_lower:
        return "Java"
    return "General"


# 🧠 SMART ALGORITHM DETECTION
def detect_algorithm(code):
    code_lower = code.lower()

    if "priority_queue" in code_lower or "dijkstra" in code_lower:
        return "Graph Shortest Path (Dijkstra)"
    if "bfs" in code_lower or "queue" in code_lower:
        return "Breadth First Search (BFS)"
    if "dfs" in code_lower or "recursive" in code_lower:
        return "Depth First Search (DFS)"
    if "dp" in code_lower or "memo" in code_lower:
        return "Dynamic Programming"
    if "binary search" in code_lower:
        return "Binary Search"
    if "clonegraph" in code_lower:
        return "Graph Cloning using DFS + HashMap"

    return "General Algorithm"


# 🔥 COMMENT GENERATOR
def generate_comments(code, language, mode="short"):
    lines = code.split("\n")
    output = []

    algo_name = detect_algorithm(code)

    # Header
    if mode == "detailed":
        output.append(f"// Language: {language}")
        output.append(f"// Algorithm: {algo_name}\n")

    for line in lines:
        stripped = line.strip()
        comment = ""

        # ---------------- SHORT MODE ----------------
        if mode == "short":

            if "#include" in stripped:
                comment = "// Libraries"
            elif "while" in stripped:
                comment = "// Loop"
            elif "for (" in stripped or "for(" in stripped:
                comment = "// Loop"
            elif "if" in stripped:
                comment = "// Condition"
            elif "return" in stripped:
                comment = "// Return"

        # ---------------- DETAILED MODE ----------------
        else:

            if "#include" in stripped:
                comment = "// Import required libraries"

            elif "class" in stripped:
                comment = "// Define class structure"

            elif "def " in stripped:
                comment = "// Function definition"

            elif "priority_queue" in stripped:
                comment = "// Min-heap for efficient minimum retrieval"

            elif "queue" in stripped:
                comment = "// Queue for BFS traversal"

            elif "stack" in stripped:
                comment = "// Stack for DFS / backtracking"

            elif "unordered_map" in stripped or "map" in stripped:
                comment = "// HashMap for storing visited/mapping values"

            elif "vector" in stripped or "list" in stripped:
                comment = "// Data structure to store elements"

            elif "for" in stripped:
                comment = "// Iterate through elements"

            elif "while" in stripped:
                comment = "// Loop until condition is met"

            elif "if" in stripped:
                comment = "// Conditional check"

            elif "return" in stripped:
                comment = "// Return final result"

            elif "visited" in stripped:
                comment = "// Track visited nodes"

            elif "dist" in stripped:
                comment = "// Store distances from source"

            elif "push" in stripped:
                comment = "// Insert element into data structure"

            elif "pop" in stripped:
                comment = "// Remove element from structure"

            elif "neighbors" in stripped:
                comment = "// Traverse connected nodes"

        # Add comment + code
        if comment:
            output.append(comment)

        output.append(line)

    return "\n".join(output)


# 🌐 ROUTES
@app.route("/")
def home():
    return "Backend running"


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    code = data.get("code", "")
    language = data.get("language", "")
    mode = data.get("mode", "short")

    if not language:
        language = detect_language(code)

    result = generate_comments(code, language, mode)

    return jsonify({
        "comment": result
    })


# 🚀 RUN SERVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))