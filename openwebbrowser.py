import webbrowser
import pywhatkit

while True:
    query=input("Me:")
    if "hello" in query:
        print("hello dear")

    elif"name" in query:
        print("I am Bot")

    elif "exit" in query:
        print("ok i am going offline")
        exit()

    elif "open google" in query:
        print("Ok Opening google")
        print("what should i search on google")
        search=input("Me:")
        pywhatkit.search(search)

    elif "open instagram" in query:
        print("Ok Opening instagram")
        webbrowser.open("http://wwww.instagram.com")

    elif "open youtube" in query:
        print("Ok Opening youtube")
        print("Ok opening youtube")
        print("what should i search on youtube")
        search=input("Me:")
        pywhatkit.playonyt(search)