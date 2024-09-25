import speech_recognition as sr
import webbrowser
import pyttsx3
#import musiclib
import urllib.parse
import pyjokes
import pywhatkit as kit
import pyautogui
import wikipedia
from datetime import datetime
from playsound import playsound


 
 
#made a function for text to speech in female voice
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()



def process(a):
    print(a)
    a = a.lower()  # Convert to lower case once for efficiency
    
    #Open any Website
    if "open" in a:
        sliced_command = a.split(" ")
        index_of_website = sliced_command.index("open") + 1
        webbrowser.open(f"https://{sliced_command[index_of_website]}.com")
    
    #Playing any video on Youtube(music,tutorials,...etc)
    elif "play" in a:
        #Method 1:(have to make a pesonal library with link of video as key value pair and import it to use here)
        # sliced_command = a.split()

        # # Ensure there is a word after 'play'
        # if "play" in sliced_command and len(sliced_command) > sliced_command.index("play") + 1:
        #     # Extract the song name from the command
        #     song_name = sliced_command[sliced_command.index("play") + 1]
        #     link = musiclib.music[song_name]
        #     webbrowser.open(link)

        #Method 2:
        # (got this module pywhatkit it is more efficient and i can play any videos)
        start_index = a.find("play")

        # Create a new string starting from the word "am"
        if start_index != -1:
            sliced_command = a[start_index:]
            kit.playonyt(sliced_command)

    
    # Search on Google
    elif "search" in a and "wikipedia" not in a:
        index = a.find("search")
        search_query = a.replace("search", "").replace("wikipedia","").replace("for","").replace("on","").replace("google","").strip()  # Strip extra spaces
        
        # Ensure there's a search term
        if search_query:
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(search_query)}"
            speak(f"Searching for {search_query} on Google.")
            webbrowser.open(search_url)
        else:
            speak("Please provide a search term.")
        

    #Telling jokes
    elif "joke" in a:
        speak(pyjokes.get_joke(language='en', category= 'all'))

    #Taking a screenshot
    elif "screenshot" in a:
        speak("screenshot saves succesfully")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

    # searching on wikipedia
    elif "wikipedia" in a:
        query = a.replace("search", "").replace("wikipedia","").replace("for","").replace("on","").strip()
        try:
            summary = wikipedia.summary(query, sentences=2)  # Get a 2-sentence summary
            speak(summary)
        except wikipedia.DisambiguationError:
            speak("There are multiple results, please be more specific.")

    #Tells time
    elif "time" in a:
        now = datetime.now()
        speak(f"Current time is {now.strftime('%H hours %M minutes and %S seconds')}")





#VOICE RECOGNIZER:
playsound("techstart.mp3")





speak("Friday is now available")

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # using google speech recognition
            converted = r.recognize_google(audio_text)
            print("You: ",converted)
            
            #here listening if somenone said friday or not
            if(converted.lower()== "friday"):
                speak("yahh")
                with sr.Microphone() as source:
                    print("Yah,How can i help you:")
                    speak("How can i help you")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process(command)
            

        except:
            print("Sorry, I did not get that")