import pyttsx3
import speech_recognition as sr

def speechRecognition():
    recognizer = sr.Recognizer()
    
    
    with sr.Microphone() as source:
        print("Hold on, we are adjusting the ambient noise...")
        
       
        recognizer.adjust_for_ambient_noise(source, duration=0.)

        print("Listening...")

        # Capture the audio
        audio_data = recognizer.listen(source, timeout=5)
          
        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print("You:", text)
            return text
        except sr.UnknownValueError:
            print("Didn't get that! my bad pookie")
            return "Didn't get that! my bad pookie"

def text_to_speech(text):
    
    engine = pyttsx3.init()

    
    engine.say(text)

   
    engine.runAndWait()
    
while True:    
    x = speechRecognition()
    text = x
    if text =="bye":
        break
    else:
        text_to_speech(text)
