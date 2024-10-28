import pyttsx3
import asyncio
import threading
from queue import Queue

class TTSManager:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        self._is_speaking = threading.Event()  # Event to track if speaking
        self.speech_queue = Queue()  # Queue to hold text for speech
        self.thread = threading.Thread(target=self._run_speech, daemon=True)
        self.thread.start()

    def _run_speech(self):
        """Thread target function that continuously checks for new text to speak."""
        while True:
            text = self.speech_queue.get()  # Wait for text to speak
            if text is None:  # Stop signal
                break
            self._is_speaking.set()
            self.engine.say(text)
            self.engine.runAndWait()
            self._is_speaking.clear()

    def speak(self, text: str):
        """Add text to the queue to be spoken asynchronously."""
        self.speech_queue.put(text)

    def is_speaking(self) -> bool:
        """Check if the engine is currently speaking."""
        return self._is_speaking.is_set()
    
    def stop(self):
        """Stops speaking immediately."""
        self.engine.stop()
        self._is_speaking.clear()  # Clear the speaking event

    def get_available_voices(self):
        """Prints available voices."""
        try:
            voices = self.engine.getProperty('voices')
            if voices:
                for index, voice in enumerate(voices):
                    print(f"Voice {index}: {voice.name} ({voice.id})")
            else:
                print("No voices available.")
        except Exception as e:
            print(f"Error retrieving voices: {e}")
    
    def unlock_windows_voices(self):
        """Unlocks all available voices on Windows (requires admin permissions)."""
        try:
            import winreg
            key_path = r"SOFTWARE\Microsoft\SPEECH_OneCore\Voices\Tokens"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                for i in range(0, winreg.QueryInfoKey(key)[0]):
                    voice_key = winreg.EnumKey(key, i)
                    winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\SPEECH\Voices\Tokens\\" + voice_key)
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\SPEECH\Voices\Tokens\\" + voice_key, 0, winreg.KEY_WRITE) as dest_key:
                        for name, value, _ in winreg.QueryInfoKey(key):
                            winreg.SetValueEx(dest_key, name, 0, winreg.REG_SZ, value)
            print("Unlocked all voices successfully.")
        except Exception as e:
            print(f"Error unlocking voices: {e}")
    
    def remove_added_voices(self):
        """Removes all non-default voices, leaving only system default voices (requires admin permissions)."""
        try:
            import winreg
            key_path = r"SOFTWARE\Microsoft\SPEECH\Voices\Tokens"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                print(winreg.QueryInfoKey(key)[0])
                for i in range(winreg.QueryInfoKey(key)[0]):
                    voice_key = winreg.EnumKey(key, i)
                    if "TTS_MS_" not in voice_key:  # 'TTS_MS_' prefix is commonly used by default voices
                        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, f"{key_path}\\{voice_key}")
                    print(voice_key)
                    if voice_key == "TTS_MS_EN-GB_HAZEL_11.0":
                        print("deleting")
                        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, f"{key_path}\\{voice_key}")

            print("Removed all added voices, leaving only default voices.")
        except Exception as e:
            print(f"Error removing added voices: {e}")

    def close(self):
        """Stops the speech thread gracefully."""
        self.speech_queue.put(None)  # Signal the thread to exit
        self.thread.join()

# Example Usage
if __name__ == "__main__":
    import time
    tts = TTSManager()
    tts.get_available_voices()
    
    # Speak text asynchronously
    # tts.speak("Hello, I am Artex your virtual AI assistant. How can I help you?")
    
    # Stop in the middle of speaking
    # time.sleep(3)
    # if tts.is_speaking():
    #     tts.stop()
    
    # Unlock additional Windows voices (Windows only)
    # tts.unlock_windows_voices()
    # tts.get_available_voices()
    
    # Remove all non-default voices (Windows only)
    # tts.remove_added_voices()
    
    # Close the TTS manager gracefully
    # tts.close()
