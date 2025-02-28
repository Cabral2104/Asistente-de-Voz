#Install SpeachRecognition with pip install SpeachRecognition
#Install pyttsx3 with pip install pyttsx3

#https://www.amazon.es/s?k=
#https://www.mercadolibre.com.mx/

import speech_recognition as sr
import webbrowser
import pyttsx3
import difflib

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    with sr.Microphone() as source:
       print("Te escucho...")
       audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f'Has dicho: {text}')
        return text.lower()
    except sr.UnknownValueError:
        print("No entendí lo que dijiste.")
        return ""
    except sr.RequestError:
        print("Hubo un error con el reconocimiento de voz.")
        return ""

def search_store(service_name, url):
    engine.runAndWait()
    query = talk()
    
    if query:
        webbrowser.open(url.format(query=query))

#Lista de tiendas disponibles
services = {
    "amazon": "https://www.amazon.es/s?k={query}",
    "mercado libre": "https://www.mercadolibre.com.mx/jm/search?as_word={query}",
    "ebay": "https://www.ebay.com/sch/i.html?_nkw={query}",
    "aliexpress": "https://www.aliexpress.com/wholesale?SearchText={query}",
    "walmart": "https://www.walmart.com.mx/search?q={query}",
    "temu": "https://www.temu.com/search?q={query}",
    "youtube": "https://www.youtube.com/results?search_query={query}"

}

#Capturar el texto hablado
text = talk()

#Buscar coincidencias con las tiendas disponibles
match = difflib.get_close_matches(text, services.keys(), n=1, cutoff=0.6)

if match:
    service_name = match[0]
    search_store(service_name, services[service_name])
else:
    print(f"No se reconoció la tienda: {text}")
    engine.say("No reconocí la tienda, intenta de nuevo.")
    engine.runAndWait()