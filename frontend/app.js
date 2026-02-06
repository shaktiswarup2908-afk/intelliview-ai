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
    JSON.stringify(data, null, 2)
}
async function loadQuestion() {
  const res = await fetch(`${API_BASE_URL}/get-question`)
  const data = await res.json()
  document.getElementById("question").innerText = data.question
}

window.onload = loadQuestion
function startSpeech() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)()
  recognition.lang = "en-US"
  recognition.start()

  recognition.onresult = function (event) {
    document.getElementById("answer").value =
      event.results[0][0].transcript
  }
}
