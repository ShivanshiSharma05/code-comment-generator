def detect_language(code):
    if "def " in code:
        return "Python"
    elif "#include" in code:
        return "C++"
    elif "public class" in code:
        return "Java"
    return "General"