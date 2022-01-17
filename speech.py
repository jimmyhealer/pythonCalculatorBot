import speech_recognition as sr
import pyaudio
from gtts import gTTS
import pygame
from io import BytesIO

import os
os.system("cls")  # windows
# import tempfile


class speech_to_text:
  def __init__(self):
    self.rg = sr.Recognizer()

  def listen(self, lang='zh-tw'):
    print(f"{'listening...':>67}")
    with sr.Microphone() as source:
    # with sr.AudioFile('voice.wav') as source:
      self.rg.adjust_for_ambient_noise(source, duration=0.5)
      audioData = self.rg.listen(source)
      try:
        text = self.rg.recognize_google(audioData, language=lang)
      except:
        text = ''
    return text


class text_to_speech:
  def __init__(self):
    self.active_mp3 = 'tmp.mp3'
    pygame.mixer.init()

  def __del__(self):
    try:
      os.unlink(self.active_mp3)
    except:
      pass
    pass

  def speak(self, text, lang='zh-tw', gogoro=0):
    if not gogoro:
      tts = gTTS(text, lang=lang)
      tts.save(self.active_mp3)
      pygame.mixer.music.load(self.active_mp3)
    else:
      pygame.mixer.music.load('./gogoro.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
      continue
    pygame.mixer.music.unload()
    return
