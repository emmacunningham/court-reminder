from transcribe.transcribe import GoogleTranscriber

print("Transcribing file...")

filename = ""
transcriber = GoogleTranscriber()
transcript, transcription_status = \
    transcriber.transcribe_audio_file_path(
        filename,
    )

print(transcript)
