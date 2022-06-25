import speech_recognition as sr
import pyaudio
import wave
print("The Recording has started\nPress CTLR+C when done...")
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1,rate = 44100,input = True,frames_per_buffer=1024)
frames = []
try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass
stream.stop_stream()
stream.close()
audio.terminate()

sound_file = wave.open("voice notes.wav","wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()
r = sr.Recognizer()

file_audio = sr.AudioFile('voice notes.wav')

with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))
f = open("TEXT NOTES.txt", "w")
f.write(r.recognize_google(audio_text))
f.close()