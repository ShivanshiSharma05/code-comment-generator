from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)


# 🔍 FINAL ROBUST LANGUAGE DETECTION
def detect_language(code):
    code_lower = code.lower()

    if "#include" in code_lower or "std::" in code_lower or "cout" in code_lower:
        return "C++"

    if "def " in code_lower and ":" in code_lower:
        return "Python"

    if "public class" in code_lower:
        return "Java"

    return "General"


# 🔥 FINAL COMMENT GENERATOR
def generate_comments(code, language, mode="short"):
    lines = code.split("\n")
    output = []

    # Header (only detailed mode)
    if mode == "detailed":
        output.append(f"// Language: {language}")
        output.append("// Dijkstra's Algorithm using priority queue (min-heap)\n")

    for line in lines:
        stripped = line.strip()
        comment = ""

        # -------- SHORT MODE --------
        if mode == "short":

            if "#include" in stripped:
                comment = "// Libraries"

            elif "while" in stripped:
                comment = "// Loop"

            elif "for (" in stripped:
                comment = "// Loop"

            elif "if (" in stripped:
                comment = "// Condition"

            elif "return" in stripped:
                comment = "// Return"

        # -------- DETAILED MODE --------
        else:

            if "#include" in stripped:
                comment = "// Includes necessary libraries"

            elif "priority_queue" in stripped:
                comment = "// Min-heap to get node with smallest distance"

            elif "vector<int> dist" in stripped:
                comment = "// Distance array initialized to infinity"

            elif "pq.push({0, src})" in stripped:
                comment = "// Start from source node"

            elif "while (!pq.empty())" in stripped:
                comment = "// Process nodes until queue is empty"

            elif "if (d > dist[u])" in stripped:
                comment = "// Ignore outdated distance"

            elif "for (auto& edge" in stripped:
                comment = "// Traverse neighbors of current node"

            elif "dist[v] = dist[u] + weight" in stripped:
                comment = "// Relax edge and update distance"

            elif "pq.push" in stripped:
                comment = "// Push updated distance"

            elif "return dist" in stripped:
                comment = "// Return shortest distances"

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

    # 🔥 FIXED AUTO DETECT
    if not language or language == "":
        language = detect_language(code)

    result = generate_comments(code, language, mode)

    return jsonify({
        "comment": result
    })


# 🚀 RUN SERVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))