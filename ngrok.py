from os import system

def start_ngrok():
    ngrok = system("ngrok tcp 25565")
    print(ngrok)
    return ngrok
