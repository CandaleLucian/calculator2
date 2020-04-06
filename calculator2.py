import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('volume', 1)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= 'en-us')
            print(f"user said: {query}\n")
            
        except Exception:
            print("Say that again please")
            speak('Say that again please')
            continue
                  
        return query

operation_sign = None
first_num = None
second_num = None
r = None

def results(first_num, operation_sign, second_num):
    if operation_sign == 'plus':
        return float(first_num) + float(second_num)
    elif operation_sign == 'minus':
        return float(first_num) - float(second_num)
    elif operation_sign == 'multiply':
        return float(first_num) * float(second_num)
    elif operation_sign == 'divide':
        return float(first_num) / float(second_num)


speak("Let's start calculating")
query = takeCommand()

def itisnumber(checker):
    try:
        float(checker)
        print("Checked")
        return True
    except ValueError:
        return False

while 'stop' not in query:
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 200)

    if itisnumber(query):
        if first_num == None:
            first_num = query
            print(str(first_num))
            speak("Number 1")
            speak(first_num)
        elif first_num != None:
            second_num = query
            print(str(second_num))
            speak('Number 2')
            speak(second_num)

    elif 'plus' in query.lower():
        operation_sign = 'plus'
        print('+')
        speak('plus')

    elif 'minus' in query.lower():
        operation_sign = 'minus'
        print('-')
        speak('minus')

    elif 'multiply' in query.lower():
        operation_sign = 'multiply'
        print('*')
        speak('multiply')

    elif 'divide' in query.lower():
        operation_sign = 'divide'
        print('/')
        speak('divide')

    elif 'equal' in query.lower():
        r = round(results(first_num, operation_sign, second_num), 4)
        print('Calculating')
        speak('Calculating')
        print(r)
        speak(r)
        first_num = r
        second_num = None

    elif "clear" in query.lower():
        first_num = None
        second_num = None

    else:
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 300)
        speak(f'I dont find any command for {query}')

    query = takeCommand()


        




