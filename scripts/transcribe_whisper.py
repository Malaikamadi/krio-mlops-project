# scripts/transcript_whisper.py
import whisper
import os

def transcribe(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path, language="kr")
    print("Transcription:", result["text"])
    return result

if __name__ == "__main__":
    transcript = transcribe("data/raw_audio/krio_sample.wav")
    with open("data/transcripts/krio_transcript.txt", "w") as f:
        f.write(transcript["text"])
