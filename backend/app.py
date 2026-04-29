from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# ---------------- LANGUAGE DETECTION ----------------
def detect_language(code):
    c = code.lower()

    if "#include" in c or "std::" in c or "cout" in c:
        return "C++"
    if "def " in c or "print(" in c:
        return "Python"
    if "public class" in c:
        return "Java"

    return "General"


# ---------------- SMART ALGORITHM DETECTION (SCORING BASED) ----------------
def detect_algorithm(code):
    c = code.lower()

    scores = {
        "BFS (Graph/Grid Traversal)": 0,
        "DFS (Recursive/Backtracking)": 0,
        "Dynamic Programming": 0,
        "Dijkstra / Shortest Path": 0,
        "Binary Search": 0,
        "HashMap / Counting": 0,
        "Greedy Algorithm": 0
    }

    # BFS signals
    if "queue" in c:
        scores["BFS (Graph/Grid Traversal)"] += 2
    if "dx" in c or "dy" in c:
        scores["BFS (Graph/Grid Traversal)"] += 2
    if "grid" in c or "matrix" in c:
        scores["BFS (Graph/Grid Traversal)"] += 1

    # DFS signals
    if "dfs" in c or "recursive" in c:
        scores["DFS (Recursive/Backtracking)"] += 3

    # DP signals
    if "dp" in c or "memo" in c or "cache" in c:
        scores["Dynamic Programming"] += 3

    # Dijkstra signals
    if "priority_queue" in c or "dijkstra" in c:
        scores["Dijkstra / Shortest Path"] += 3

    # Binary search
    if "mid" in c and "low" in c and "high" in c:
        scores["Binary Search"] += 3

    # HashMap / counting
    if "unordered_map" in c or "map" in c or "dict" in c:
        scores["HashMap / Counting"] += 2

    # Greedy
    if "sort" in c and "if" in c:
        scores["Greedy Algorithm"] += 1

    # Pick best match
    best = max(scores, key=scores.get)

    # If everything is zero
    if scores[best] == 0:
        return "General Algorithm"

    return best


# ---------------- COMMENT GENERATOR ----------------
def generate_comments(code, language, mode="short"):
    lines = code.split("\n")
    output = []

    algo = detect_algorithm(code)

    # HEADER
    if mode == "detailed":
        output.append(f"// Language: {language}")
        output.append(f"// Algorithm: {algo}\n")

    for line in lines:
        s = line.strip()
        comment = ""

        # ---------------- SHORT MODE ----------------
        if mode == "short":
            if "#include" in s:
                comment = "// Import libraries"
            elif "for" in s or "while" in s:
                comment = "// Loop"
            elif "if" in s:
                comment = "// Condition"
            elif "return" in s:
                comment = "// Return"

        # ---------------- DETAILED MODE ----------------
        else:
            if "#include" in s:
                comment = "// Import required libraries"
            elif "class" in s:
                comment = "// Define class"
            elif "def " in s:
                comment = "// Function definition"
            elif "for" in s:
                comment = "// Iterate over elements"
            elif "while" in s:
                comment = "// Loop until condition fails"
            elif "if" in s:
                comment = "// Conditional check"
            elif "return" in s:
                comment = "// Return final result"
            elif "queue" in s:
                comment = "// Queue used for traversal (BFS style)"
            elif "stack" in s:
                comment = "// Stack used for DFS/backtracking"
            elif "unordered_map" in s or "map" in s:
                comment = "// HashMap for fast lookup"
            elif "vector" in s or "list" in s:
                comment = "// Data structure for storing elements"

        if comment:
            output.append(comment)

        output.append(line)

    return "\n".join(output)


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return "Backend running"


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        code = data.get("code", "")
        language = data.get("language", "")
        mode = data.get("mode", "short")

        if not language:
            language = detect_language(code)

        result = generate_comments(code, language, mode)

        return jsonify({"comment": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))