# scripts/record_audio.py
import sounddevice as sd
import wavio
import os

def record_audio(filename='krio_sample.wav', duration=30, samplerate=44100):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    os.makedirs("data/raw_audio", exist_ok=True)
    wavio.write(f"data/raw_audio/{filename}", recording, samplerate, sampwidth=2)
    print(f"Saved to data/raw_audio/{filename}")

if __name__ == "__main__":
    record_audio()
