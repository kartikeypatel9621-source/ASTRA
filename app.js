const form = document.getElementById("hello-form");
const nameInput = document.getElementById("name");
const messageEl = document.getElementById("message");
const metaEl = document.getElementById("meta");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const response = await fetch("/api/hello", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: nameInput.value }),
  });

  const data = await response.json();
  messageEl.hidden = false;
  metaEl.hidden = false;
  messageEl.textContent = data.message;
  metaEl.textContent = `Server time: ${data.serverTime}`;
});
