from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ---------------- LANGUAGE DETECTION ----------------
def detect_language(code):
    code_lower = code.lower()

    if "#include" in code_lower or "cout" in code_lower or "unordered_map" in code_lower:
        return "C++"

    if "def " in code_lower and ":" in code_lower:
        return "Python"

    if "public class" in code_lower:
        return "Java"

    return "General"


# ---------------- ALGORITHM DETECTION ----------------
def detect_algorithm(code):
    if "priority_queue" in code:
        return [
            "// Algorithm: Dijkstra's Shortest Path",
            "// Approach: Greedy + Min Heap",
            "// Time Complexity: O(E log V)\n"
        ]

    if "cloneGraph" in code or "neighbors" in code:
        return [
            "// Algorithm: Graph Cloning (DFS + Recursion)",
            "// Approach: Depth First Search + HashMap",
            "// Time Complexity: O(V + E)\n"
        ]

    return ["// Algorithm: General Problem\n"]


# ---------------- COMMENT GENERATOR ----------------
def generate_comments(code, language, mode="short"):
    lines = code.split("\n")
    output = []

    # Header
    if mode == "detailed":
        output.append(f"// Language: {language}")
        output.extend(detect_algorithm(code))

    for line in lines:
        stripped = line.strip()
        comment = ""

        # SHORT MODE
        if mode == "short":

            if "#include" in stripped:
                comment = "// Libraries"

            elif "while" in stripped:
                comment = "// Loop"

            elif "for" in stripped:
                comment = "// Loop"

            elif "if" in stripped:
                comment = "// Condition"

            elif "return" in stripped:
                comment = "// Return"

        # DETAILED MODE
        else:

            if "#include" in stripped:
                comment = "// Standard libraries"

            elif "priority_queue" in stripped:
                comment = "// Min heap for shortest path"

            elif "unordered_map" in stripped:
                comment = "// HashMap for visited nodes"

            elif "pq.push" in stripped:
                comment = "// Push into priority queue"

            elif "while (!pq.empty())" in stripped:
                comment = "// Process all nodes"

            elif "if (d > dist[u])" in stripped:
                comment = "// Skip outdated path"

            elif "for (auto" in stripped:
                comment = "// Traverse neighbors"

            elif "cloneGraph" in stripped:
                comment = "// DFS graph cloning"

            elif "new Node" in stripped:
                comment = "// Create cloned node"

            elif "return" in stripped:
                comment = "// Return result"

        if comment:
            output.append(comment)

        output.append(line)

    return "\n".join(output)


# ---------------- API ----------------
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

    return jsonify({"comment": result})


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)