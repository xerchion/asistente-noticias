'use strict';

const BACKEND_URL = 'http://localhost:8000';

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

const langSelect  = document.getElementById('lang-select');
const btnMic      = document.getElementById('btn-mic');
const btnSpeak    = document.getElementById('btn-speak');
const resultArea  = document.getElementById('result');
const errorBanner = document.getElementById('error-banner');
const compatWarn  = document.getElementById('compat-warning');
const statusBar   = document.getElementById('status-bar');

let recognition = null;
let isListening  = false;

function showError(msg) {
  errorBanner.textContent = msg;
  errorBanner.classList.add('visible');
}

function clearError() {
  errorBanner.textContent = '';
  errorBanner.classList.remove('visible');
}

function setStatus(msg) {
  statusBar.textContent = msg;
  statusBar.classList.toggle('visible', msg !== '');
}

function checkCompatibility() {
  const noSpeechRec = !SpeechRecognition;
  const noSpeechSyn = !window.speechSynthesis;

  if (noSpeechRec || noSpeechSyn) {
    compatWarn.classList.add('visible');
    const missing = [];
    if (noSpeechRec) missing.push('reconocimiento de voz');
    if (noSpeechSyn) missing.push('síntesis de voz');
    compatWarn.textContent =
      `Tu navegador no soporta: ${missing.join(', ')}. Usa Chrome 25+ para la experiencia completa.`;

    if (noSpeechRec) btnMic.disabled = true;
    if (noSpeechSyn) btnSpeak.disabled = true;
  }
}

async function sendToBackend(texto) {
  setStatus('Procesando...');
  try {
    const response = await fetch(`${BACKEND_URL}/echo`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ texto, idioma: langSelect.value }),
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const data = await response.json();
    speakText(data.texto, data.idioma);
  } catch {
    setStatus('');
    showError('No se pudo conectar con el servidor.');
  }
}

function speakText(texto, idioma) {
  if (!window.speechSynthesis) return;
  setStatus('Leyendo...');
  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(texto);
  utterance.lang = idioma;
  utterance.onend = () => setStatus('');
  utterance.onerror = () => {
    setStatus('');
    showError('Error al reproducir la síntesis de voz.');
  };
  window.speechSynthesis.speak(utterance);
}

function buildRecognition() {
  if (!SpeechRecognition) return null;

  const rec = new SpeechRecognition();
  rec.continuous     = false;
  rec.interimResults = false;
  rec.lang           = langSelect.value;

  rec.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    resultArea.value = transcript;
    clearError();
    sendToBackend(transcript);
  };

  rec.onerror = (event) => {
    stopListening();
    setStatus('');
    const messages = {
      'not-allowed':   'Permiso de micrófono denegado. Permite el acceso en la barra de dirección.',
      'no-speech':     'No se detectó audio. Habla más cerca del micrófono e inténtalo de nuevo.',
      'audio-capture': 'No se encontró micrófono. Conecta uno e inténtalo de nuevo.',
      'network':       'Error de red al procesar el audio.',
    };
    showError(messages[event.error] || `Error de reconocimiento: ${event.error}`);
  };

  rec.onend = () => {
    if (isListening) stopListening();
  };

  return rec;
}

function startListening() {
  clearError();
  recognition = buildRecognition();
  if (!recognition) return;

  recognition.lang = langSelect.value;
  recognition.start();
  isListening = true;
  btnMic.classList.add('listening');
  btnMic.textContent = '⏹ Detener';
  setStatus('Escuchando...');
}

function stopListening() {
  isListening = false;
  btnMic.classList.remove('listening');
  btnMic.textContent = '🎤 Micrófono';
  if (recognition) {
    recognition.stop();
    recognition = null;
  }
}

btnMic.addEventListener('click', () => {
  if (isListening) {
    stopListening();
    setStatus('');
  } else {
    startListening();
  }
});

btnSpeak.addEventListener('click', () => {
  const texto = resultArea.value.trim();
  if (!texto) return;
  clearError();
  speakText(texto, langSelect.value);
});

langSelect.addEventListener('change', () => {
  if (isListening) stopListening();
  clearError();
  setStatus('');
});

checkCompatibility();
