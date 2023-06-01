import time
import serial
import speech_recognition as sr
import pyaudio
import subprocess

class VoiceCommand:
    def __init__(self):
        self._NO_VOICE = "no voice"
        self._SPEGNI = "spegnimento"
        self._VOICE_STOP = "stop"
        self._VOICE_FORWARD = "forward"
        self._VOICE_BACKWARD = "backward"
        self._VOICE_UP = "up"
        self._VOICE_DOWN = "down"
        self._VOICE_RIGHT = "right"
        self._VOICE_LEFT = "left"
        self._VOICE_OPEN = "open"
        self._VOICE_CLOSE = "close"
        self._detecting = False
        self._current_VOICE_counter = 0
        self._last_VOICE = self._NO_VOICE
        self._current_VOICE = self._NO_VOICE
        self._detected_VOICE = self._NO_VOICE
        self._VOICE_changed = True
        self._last_VOICE_time = 0
        self._recognizer = sr.Recognizer()
        self.microphone_index = 1
        
    def start_detection(self, callback):
        self._detecting = True
        self._detecting(callback)
    
    def stop_detection(self):
        self._detecting = False
    
    @staticmethod 
    def recognize_speech(self):
        
        microphone_index = 1
        
        r = sr.Recognizer()
        
        with sr.Microphone(device_index=microphone_index) as source:
            print("Parla adesso...")
            # Imposta il livello di rumore di fondo
            r.adjust_for_ambient_noise(source)
            # Registra l'audio dalla sorgente
            audio = r.listen(source)

        try:
            # Trascrivi l'audio in testo
            text = r.recognize_google(audio, language='it-IT')
            print(f"Hai detto: {text}")
            # Restituisci il comando corrispondente al testo
            return self.get(text.lower(), "")
        except sr.UnknownValueError:
            print("Non ho capito cosa hai detto.")
        except sr.RequestError as e:
            print(f"Errore nella richiesta di riconoscimento vocale: {e}")
            return
        
"""voice_command = VoiceCommand()
voice_command.start_detection(callback_function)"""
