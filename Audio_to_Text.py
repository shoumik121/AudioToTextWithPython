print("Bangla Voice To Text and Text to Binary using Python")
print(50*'-')
import os
import time
from playsound import playsound
import speech_recognition as sr
import binascii
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

reco = sr.Recognizer()
voice = 'audiobangla.wav'
with sr.AudioFile(voice) as source:
    print("Listening the Bengali audio file....")
    playsound('audiobangla.wav')
    audio = reco.listen(source)
    text = reco.recognize_google(audio, language = 'bn-BD')
    print (text)
    print("")
    print("Binarry Represntation : ")
    print("")
    print(' '.join(format(ord(a), 'b') for a in text))
    
print(50*'=')
print("English Voice To Text and Text to Binary using Python")

voice = 'audio.wav'
with sr.AudioFile(voice) as source:
    print("Listening the English audio file....")
    playsound('audio.wav')
    audio = reco.listen(source)
    text = reco.recognize_google(audio)
    print (text)
    print("")
    print("Binarry Represntation :")
    print("")
    print(' '.join(format(ord(a), 'b') for a in text))


#SHOW WAVE FORM OF AUDIO 1
spf = wave.open('audiobangla.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
if spf.getnchannels() == 1:
    print 'Just mono files'
    sys.exit(0)

plt.figure(1)
plt.title('Bangla Voice Analog Wave...')
plt.plot(signal)




#SHOW WAVE FORM OF AUDIO 2
spf = wave.open('audio.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
if spf.getnchannels() == 1:
    print 'Just mono files'
    sys.exit(0)

plt.figure(2)
plt.title('English Audio Analog Wave...')
plt.plot(signal)
time.sleep(3)
plt.show()



