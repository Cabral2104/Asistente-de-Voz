#Install SpeachRecognition with pip install SpeachRecognition
#Install pyttsx3 with pip install pyttsx3

#https://www.amazon.es/s?k=
#https://www.mercadolibre.com.mx/

import speech_recognition as sr
import webbrowser
import pyttsx3

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

def search_store(store_name, url):
    engine.say(f'Qué quieres buscar en {store_name}')
    engine.runAndWait()
    query = talk()

    if query:
        webbrowser.open(f'{url}{query}')

text = talk()

if 'amazon' in text:
    search_store('Amazon', 'https://www.amazon.es/s?k=')

elif 'mercadolibre' in text:
    search_store('Mercado Libre', 'https://www.mercadolibre.com.mx/jm/search?as_word=')

elif 'ebay' in text:
    search_store('eBay', 'https://www.ebay.com/sch/i.html?_nkw=')

elif 'aliexpress' in text:
    search_store('AliExpress', 'https://www.aliexpress.com/wholesale?SearchText=')

elif 'walmart' in text:
    search_store('Walmart', 'https://www.walmart.com.mx/search?q=')

else:
    engine.say("No conozco aún esa tienda, Lo siento:(")
    engine.runAndWait()