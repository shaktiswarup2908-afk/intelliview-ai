// frontend/app.js

const API_BASE_URL = "https://intelliview-backend.onrender.com"

async function submitAnswer() {
  const answer = document.getElementById("answer").value

  const response = await fetch(`${API_BASE_URL}/analyze-answer`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answer })
  })

  const data = await response.json()

  document.getElementById("result").innerText =
    `Score: ${data.score}\nConfidence: ${data.confidence}`
}
