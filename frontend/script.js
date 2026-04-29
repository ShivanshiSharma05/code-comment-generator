async function generate() {
  const code = document.getElementById("codeInput").value;
  const language = document.getElementById("language").value;
  const mode = document.getElementById("mode").value;
  const outputBox = document.getElementById("output");

  if (!code.trim()) {
    outputBox.value = "⚠️ Please enter some code!";
    return;
  }

  outputBox.value = "🤖 AI is thinking...";

  try {
    const res = await fetch("https://code-comment-backend-cjah.onrender.com/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code, language, mode }),
    });

    const data = await res.json();
    typeEffect(data.comment);

  } catch (error) {
    outputBox.value = "❌ Error connecting to backend!";
  }
}

function typeEffect(text) {
  const outputBox = document.getElementById("output");
  outputBox.value = "";
  let i = 0;

  const interval = setInterval(() => {
    outputBox.value += text.charAt(i);
    i++;
    if (i >= text.length) clearInterval(interval);
  }, 8);
}

function copyText() {
  const output = document.getElementById("output");
  output.select();
  document.execCommand("copy");
  alert("Copied to clipboard!");
}