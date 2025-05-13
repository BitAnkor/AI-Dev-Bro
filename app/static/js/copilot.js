// app/static/js/copilot.js

const copilotBtn = document.getElementById('copilotBtn');
const copilotModal = document.getElementById('copilotModal');
const closeBtn = document.getElementById('closeCopilot');
const chatBox = document.getElementById('chatBox');
const form = document.getElementById('copilotForm');
const input = document.getElementById('copilotInput');

copilotBtn.onclick = () => copilotModal.classList.remove('hidden');
closeBtn.onclick = () => copilotModal.classList.add('hidden');

function addMessage(role, content) {
  const msg = document.createElement('div');
  msg.className = role === 'user' ? 'text-right' : 'text-left';
  msg.innerHTML = `<div class="inline-block px-4 py-2 rounded-lg ${role === 'user' ? 'bg-accent-500 text-white' : 'bg-white/10 text-gray-200'}">${content}</div>`;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

form.onsubmit = async (e) => {
  e.preventDefault();
  const question = input.value;
  input.value = '';
  addMessage('user', question);
  addMessage('assistant', '⏳ Pensando...');

  const response = await fetch("/api/copilot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  });

  const data = await response.json();
  const assistantMsg = data.choices?.[0]?.message?.content || "⚠️ Error de respuesta";
  chatBox.lastChild.remove();
  addMessage('assistant', assistantMsg);
};
