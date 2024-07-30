from mtranslate import translate
from time import sleep
import pyttsx3

class Speaker:
    def __init__(self, input_file_path, stop_file_path, translate=True, speak_continous=True):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty('voices')
        self.current_voice = self.voices[0].id
        self.__input_file_path = input_file_path
        self.__speak_continous = speak_continous
        self.__stop_file_path = stop_file_path
        self.__translate = translate
        self.__fine = True
        self.__previous_text = None
        if not self.__check_arguments():
              self.__fine = False

    def __check_arguments(self):
        if not isinstance(self.__speak_continous, bool):
            raise TypeError("Parameter speak_continous must be boolean")
            return False
        if not isinstance(self.__translate, bool):
            raise TypeError("Parameter translate must be boolean")
            return False
        if not isinstance(self.__input_file_path, str):
            raise TypeError("Parameter input_file_path must be string")
            return False
        if not isinstance(self.__stop_file_path, str):
            raise TypeError("Parameter stop_file_path must be string")
            return False
        if not self.__input_file_path:
            raise ValueError("Please provide the input_file_path")
            return False
        if self.__speak_continous and not self.__stop_file_path:
            raise ValueError("Please provide stop_file_paths")
            return False
        return True
        
    def __translate_to_language(self, text):
        return translate(to_translate=text, to_language="en-us")
    
    def __initiate_speak(self):
        with open(self.__stop_file_path, "w") as initiator_file:
            initiator_file.write("A")

    def quit_speak(self):
        with open(self.__stop_file_path, "w") as initiator_file:
            initiator_file.write("B")

    def populate_voices(self):
        return [{
            'ID': voice.id,
            'Name': voice.name,
            'Languages': voice.languages,
            'Gender': voice.gender,
            'Age': voice.age
        } for voice in self.voices]

    def set_voice(self, voice_name):
        for voice in self.voices:
            if voice.name == voice_name:
                self.engine.setProperty('voice', voice.id)
                self.current_voice = voice.id
                print(f"Voice set to {voice.name}")
                return
        print(f"Voice '{voice_name}' not found. Using default voice.")
        self.engine.setProperty('voice', self.voices[0].id)
        self.current_voice = self.voices[0].id

    def speak(self):
        if not self.__fine:
            return
        self.__initiate_speak()
        if self.__speak_continous:
            while True:
                with open(self.__stop_file_path, "a+") as initiator_file:
                    initiator_file.seek(0)
                    to_speak = initiator_file.read()
                    initiator_file.close()
                if not to_speak == "A" and to_speak == "B":
                    break
                with open(self.__input_file_path, "a+") as data_file:
                    data_file.seek(0)
                    data = data_file.read()
                    data_file.close()
                if self.__previous_text != data:
                    self.__previous_text = data
                    self.engine.setProperty('voice', self.current_voice)
                    lengthcode = len(data)
                    if lengthcode > 30:
                        self.engine.setProperty('rate', 180)
                    else:
                        self.engine.setProperty('rate', 170)
                    data = self.__translate_to_language(data) if self.__translate else data
                    self.engine.say(data)
                    self.engine.runAndWait()
                sleep(0.333)
        else:
            with open(self.__input_file_path, "a+") as data_file:
                data_file.seek(0)
                data = data_file.read()
                data_file.close()
            self.engine.setProperty('voice', self.current_voice)
            lengthcode = len(data)
            if lengthcode > 30:
                self.engine.setProperty('rate', 180)
            else:
                self.engine.setProperty('rate', 170)
            data = self.__translate_to_language(data) if self.__translate else data
            self.engine.say(data)
            self.engine.runAndWait()