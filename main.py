import speech_recognition as sr
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(aud):
    print(f"SPEAK: {aud}")
    engine.say(aud)
    engine.runAndWait()

def takeAud():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # NEW: adjust mic sensitivity
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=7)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            speak("Sorry, I couldn't hear anything.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Please speak clearly.")
            return None
        except Exception as e:
            speak(f"Something went wrong: {str(e)}")
            return None

def get_response(prompt):
    while True:
        speak(prompt)
        response = takeAud()
        if response:
            return response
        else:
            speak("Please say that again.")

def wishme():
    speak("I am Robo 2.0, created by the great Asha.")

    first_name = get_response("What's your first name?")
    last_name = get_response("What's your last name?")
    speak(f"Hi {first_name} {last_name}, I hope you are feeling good today.")

    address = get_response("Please say your residence address.")
    blood_group = get_response("Please say your blood group.")
    company = get_response("What is your company name?")

    speak("Your identity card is ready for the printing process.")
    confirm = get_response("Would you like to listen to your confirmed details? Say yes or no.")

    if "yes" in confirm.lower():
        speak("Here are your details:")
        speak(f"Name: {first_name} {last_name}")
        speak(f"Address: {address}")
        speak(f"Blood Group: {blood_group}")
        speak(f"Company Name: {company}")
        speak("Your identity card is now in the printing process.")
    else:
        speak("Thank you.")
        speak("Your identity card is now in the printing process.")
       
# Start the conversation
wishme()
