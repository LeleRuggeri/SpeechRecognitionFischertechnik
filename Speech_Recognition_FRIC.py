import speech_recognition as sr
from connection.client import Client

if __name__ == "__main__":
    
    # For Matlab
    global c
    c = Client("127.0.0.1", 7777)  # 172.22.32.1 192.168.6.177
    c.connect() # The software stops here in case it can't find a connection server
    c.send("Hello server!")

    # Command dictionary
commands = {
    "plpower": "shut down",
    "stop": "stop",
    "please go forward": "forward",
    "please go backwards": "backward",
    "please go up": "up",
    "please go down": "down",
    "please go left": "left",
    "please go right": "right",
    "please open": "open",
    "close": "close"
}

microphone_index = 1 

# Speech recognition function
def recognize_speech():
    
    # Creating recognizer object
    r = sr.Recognizer()
    
    # Using microphone as audio source
    with sr.Microphone(device_index=microphone_index) as source:
        
        print("Speak now...")
        
        # Setting noise floor
        r.adjust_for_ambient_noise(source)
        
        # Recording audio from source
        audio = r.listen(source)

    try:
        
        # Writing down the audio as text
        text = r.recognize_google(audio)
        
        # Returning the command based on audio recorded
        return commands.get(text.lower(), "")
    
    except sr.UnknownValueError:
        
        print("I did not understand what you said.")
        
    except sr.RequestError as e:
        
        print(f"Error in speech recognition: {e}")
        
    return ""

def recognize_number():
    
    m = sr.Recognizer()
    
    with sr.Microphone(device_index=microphone_index) as source2:
       
        print("How many times?")
        m.adjust_for_ambient_noise(source2)
        audio2 = m.listen(source2)
        
    try:
        
        cycle = m.recognize_google(audio2)
        
        number = int(cycle)
        
        return number
    
    except sr.UnknownValueError:
        
        print("I did not understand the number.")
        
    except sr.RequestError as e:
        
        print(f"Error in speech recognition: {e}")
        
    return ""
    
# Main loop
while True:
    
    command = recognize_speech()
   
    if command == "shut down":
        
        print("Disabling speech recognition.")
        break
    
    elif command:
        
        message = command
        
        number_of_cycles = recognize_number()
        print(f"Command sent: {command} x{number_of_cycles}")
        if isinstance(number_of_cycles, int):
            while number_of_cycles > 0:
                c.send(message)
                number_of_cycles=number_of_cycles-1
            
    else:
        print("Awaiting command...")