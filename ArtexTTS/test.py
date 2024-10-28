import pyttsx3

def speak_text(text, rate=150, volume=0.9, voice_index=0):
    engine = pyttsx3.init()
    
    # Set speech rate
    engine.setProperty('rate', rate)
    
    # Set volume (0.0 to 1.0)
    engine.setProperty('volume', volume)
    
    # Set voice by index
    voices = engine.getProperty('voices')
    if voices and 0 <= voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Example usage
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=0)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=1)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=2)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=3)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=4)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=5)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=6)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=7)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=8)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=9)
speak_text("Hello, how are you?", rate=170, volume=1, voice_index=10)