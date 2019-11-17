from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
while(1):
    print("Start")
    r = sr.Recognizer()
    with sr.Microphone() as source:
         audio = r.listen(source)
    try:
        a = r.recognize_google(audio)
        print("me:" + a)
    except Exception as e:
               print(e)
    if a == "hi":
        print("my:" + a)
        mytext ="hello"
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "how are you":
        print("my:" + a)
        mytext ="i am fine"
        language = 'en'
        print("my ex:" + mytext)
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "why you leave me":
        print("my:" + a)
        mytext ="saikat you know the reason why you asking me the same qustion again and againg please don't ask me"
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "do you still love me":
        print("my:" + a)
        mytext ="i don't know"
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "do you know how much i loved you":
        print("my:" + a)
        mytext ="no you don't love me i was just your need"
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "do you know today's date":
        print("my:" + a)
        mytext ="yes i know and i also know why you asking me this qustion"
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "you hurt me":
       print("my:" + a)
       mytext ="sorry but i think i did the right thing"
       print("my ex:" + mytext)
       language = 'en'
       myobj = gTTS(text=mytext, lang=language, slow=False) 
       myobj.save("file.mp3") 
       playsound("file.mp3")
       os.remove("file.mp3")
       
    elif a == " worng  ":
       print("my:" + a)
       mytext ="i don't want to talk about this topic "
       print("my ex:" + mytext)
       language = 'en'
       myobj = gTTS(text=mytext, lang=language, slow=False) 
       myobj.save("file.mp3") 
       playsound("file.mp3")
       os.remove("file.mp3")
       
    elif a == "why":
        mytext ="stop asking me"
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "tell me the reason":
        mytext ="i told you one simple thing again and again "
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "smoking":
        mytext ="you know better"
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "tell me clearly":
        mytext ="it's your life enjoy it who am i"
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "you was my everything":
        mytext ="now thos things are valuless for me  i got someone else"
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "you just make my life hell":
        mytext ="forget me and be happy"
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "ok":
        mytext ="don't knock me againg"
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    elif a == "be happy":
        mytext ="take care by"
        print("my:" + a)
        print("my ex:" + mytext)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        
    else:
        mytext ="say it clearly"
        print("my ex :say it again")
        print("my:" + a)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("file.mp3") 
        playsound("file.mp3")
        os.remove("file.mp3")
        






   