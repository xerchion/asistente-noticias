'use strict';

const SPEAK_TEXT = {
  'es-ES': 'Hola, soy tu asistente de noticias tecnológicas.',
  'en-US': 'Hello, I am your technology news assistant.',
};

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

const langSelect   = document.getElementById('lang-select');
const btnMic       = document.getElementById('btn-mic');
const btnSpeak     = document.getElementById('btn-speak');
const resultArea   = document.getElementById('result');
const errorBanner  = document.getElementById('error-banner');
const compatWarn   = document.getElementById('compat-warning');

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

function checkCompatibility() {
  const noSpeechRec  = !SpeechRecognition;
  const noSpeechSyn  = !window.speechSynthesis;

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
  };

  rec.onerror = (event) => {
    stopListening();
    const messages = {
      'not-allowed':     'Permiso de micrófono denegado. Permite el acceso en la barra de dirección.',
      'no-speech':       'No se detectó audio. Habla más cerca del micrófono e inténtalo de nuevo.',
      'audio-capture':   'No se encontró micrófono. Conecta uno e inténtalo de nuevo.',
      'network':         'Error de red al procesar el audio.',
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
  } else {
    startListening();
  }
});

btnSpeak.addEventListener('click', () => {
  if (!window.speechSynthesis) return;

  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(SPEAK_TEXT[langSelect.value]);
  utterance.lang  = langSelect.value;

  btnSpeak.disabled = true;
  utterance.onend = () => { btnSpeak.disabled = false; };
  utterance.onerror = () => {
    btnSpeak.disabled = false;
    showError('Error al reproducir la síntesis de voz.');
  };

  window.speechSynthesis.speak(utterance);
});

langSelect.addEventListener('change', () => {
  if (isListening) stopListening();
  clearError();
});

checkCompatibility();
