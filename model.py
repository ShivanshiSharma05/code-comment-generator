# -------------------------------
# 🔹 LINE EXPLANATION FUNCTION
# -------------------------------
def explain_line(line: str):
    line = line.strip()

    if line.startswith("def"):
        name = line.split("(")[0].replace("def", "").strip()
        return f"# Defines function '{name}'"

    elif line.startswith("for"):
        return "# Loop iterates over a sequence"

    elif line.startswith("while"):
        return "# While loop runs until condition is true"

    elif line.startswith("if"):
        return "# Checks a condition"

    elif line.startswith("elif"):
        return "# Checks another condition"

    elif line.startswith("else"):
        return "# Executes if above conditions fail"

    elif "return" in line:
        return "# Returns the result"

    elif "print" in line:
        return "# Prints output to console"

    elif "=" in line and "==" not in line:
        return "# Assigns value to a variable"

    elif "import" in line:
        return "# Imports a module"

    return "# Executes this line"


# -------------------------------
# 🔹 MAIN FUNCTION
# -------------------------------
def generate_comments_inline(code: str):
    lines = code.split("\n")
    result = []

    for line in lines:
        stripped = line.strip()

        if stripped == "":
            result.append("")
            continue

        comment = explain_line(stripped)
        result.append(comment)
        result.append(line)

    return "\n".join(result)