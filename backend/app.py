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


# ---------------- REAL-TIME ALGORITHM DETECTION ----------------
def detect_algorithm(code):
    c = code.lower()

    features = {
        "queue": len(re.findall(r'queue', c)),
        "stack": len(re.findall(r'stack', c)),
        "recursion": 1 if "return" in c and "(" in c else 0,
        "grid": 1 if "grid" in c or "matrix" in c else 0,
        "map": 1 if "map" in c or "unordered_map" in c or "dict" in c else 0,
        "dp": 1 if "dp" in c or "memo" in c else 0,
        "sort": 1 if "sort" in c else 0,
        "binary": 1 if "mid" in c and ("low" in c or "high" in c) else 0,
        "node": 1 if "node" in c or "neighbors" in c else 0
    }

    scores = {
        "BFS / Graph Traversal": features["queue"] + features["grid"] * 2,
        "DFS / Backtracking": features["stack"] + features["recursion"] * 2,
        "Dynamic Programming": features["dp"] * 3,
        "Binary Search": features["binary"] * 3,
        "Graph / Tree / Cloning": features["node"] + features["map"] * 2,
        "Sorting / Greedy": features["sort"]
    }

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return "General Algorithm"

    return best


# ---------------- MEANINGFUL COMMENT ENGINE ----------------
def generate_comments(code, language, mode="short"):
    lines = code.split("\n")
    output = []

    algo = detect_algorithm(code)

    output.append(f"// Language: {language}")

    if mode == "detailed":
        output.append(f"// Algorithm: {algo}\n")

    for line in lines:
        s = line.strip()
        comment = ""

        # ---------------- SHORT MODE ----------------
        if mode == "short":
            if "for" in s or "while" in s:
                comment = "// iterating over data"
            elif "if" in s:
                comment = "// condition check"
            elif "return" in s:
                comment = "// returning result"

        # ---------------- DETAILED MODE (MEANINGFUL LOGIC) ----------------
        else:

            if "class" in s:
                comment = "// defining data structure or object"

            elif "def " in s or "void" in s:
                comment = "// function implementing core logic"

            elif "unordered_map" in s or "map" in s:
                comment = "// storing mappings for fast lookup (memoization / visited states)"

            elif "queue" in s:
                comment = "// queue used for BFS (level order traversal)"

            elif "stack" in s:
                comment = "// stack used for DFS or backtracking"

            elif "for" in s:
                comment = "// iterating through elements or neighbors"

            elif "while" in s:
                comment = "// loop continues until condition becomes false"

            elif "grid" in s or "matrix" in s:
                comment = "// working on 2D grid structure"

            elif "visited" in s:
                comment = "// tracking visited nodes to avoid repetition"

            elif "return" in s:
                comment = "// returning computed final output"

            elif "if" in s:
                comment = "// decision making based on condition"

            elif "node" in s or "neighbors" in s:
                comment = "// graph structure representation"

        if comment:
            output.append(comment)

        output.append(line)

    return "\n".join(output)


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return "Backend running successfully"


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

        return jsonify({
            "comment": result,
            "language": language,
            "algorithm": detect_algorithm(code)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))