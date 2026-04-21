import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (runs once)
nltk.download('punkt')
nltk.download('punkt_tab')

# -------------------------------
# 🔹 NLP COMMENT GENERATOR
# -------------------------------
def generate_comments_inline(code: str):
    lines = code.split("\n")
    result = []

    for line in lines:
        stripped = line.strip()

        if stripped == "":
            result.append("")
            continue

        comment = "# "

        # FUNCTION
        if stripped.startswith("def"):
            name = stripped.split("(")[0].replace("def", "").strip()
            comment += f"Defines function '{name}'"

        # LOOP
        elif stripped.startswith("for"):
            comment += "Starts a loop to iterate over a sequence"

        elif stripped.startswith("while"):
            comment += "Starts a loop that runs while condition is true"

        # CONDITION
        elif stripped.startswith("if"):
            comment += "Checks a condition"

        elif stripped.startswith("elif"):
            comment += "Checks another condition if previous was false"

        elif stripped.startswith("else"):
            comment += "Executes when all above conditions are false"

        # RETURN
        elif "return" in stripped:
            value = stripped.replace("return", "").strip()
            comment += f"Returns value {value}"

        # PRINT
        elif "print" in stripped:
            comment += "Prints output to console"

        # ASSIGNMENT
        elif "=" in stripped and "==" not in stripped:
            var, val = stripped.split("=", 1)
            comment += f"Assigns value {val.strip()} to variable '{var.strip()}'"

        # APPEND
        elif "append" in stripped:
            comment += "Adds element to list"

        # INPUT
        elif "input" in stripped:
            comment += "Takes input from user"

        # DEFAULT
        else:
            comment += "Performs an operation"

        result.append(comment)
        result.append(line)

    return "\n".join(result)