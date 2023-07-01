import speech_recognition as sr
import openai
import pyttsx3


import requests, uuid, json



def text_to_speech(text):
    # Création d'une instance du moteur de synthèse vocale
    engine = pyttsx3.init()
    # Lecture du texte à haute voix
    engine.say(text)
    engine.runAndWait()
    
    
openai.api_key = ""




Lesmessages = []


def communicate(prompt):
   
    Lesmessages.append( {"role": "user", "content": prompt})
    # Génération d'une réponse à partir du prompt
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=Lesmessages
    )
    
    
    Lesmessages.append(res.choices[0].message)
    
    return res.choices[0].message.content

    
    
while True :
    # Création d'une instance de l'objet recognizer
    r = sr.Recognizer()

    # Utilisation du microphone comme source audio
    with sr.Microphone() as source:
        print("Je vous écoute...")
        # ajustement de la sensibilité du micro selon le bruit ambiant
        r.adjust_for_ambient_noise(source)
        # enregistrement de l'audio
        audio = r.listen(source)

    try:
        # reconnaissance de la parole
        text = r.recognize_google(audio, language="fr-FR")
        print(f"Vous avez dit : {text}")
        
        
        response = communicate(text)
        print(f"ChatGPT : {response}")
        text_to_speech(response)
        
        
    except sr.UnknownValueError or  sr.RequestError as e:
        print("Je n'ai pas compris pourriez-vous répétez ?")
   
