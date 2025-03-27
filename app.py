from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import os

# Defina as credenciais do Twilio (pegue no painel da Twilio)
TWILIO_ACCOUNT_SID = "ACf7f0f9a526d49c91116b0462f260d7d6"
TWILIO_AUTH_TOKEN = "8c2ca25d12f8f5380b375b58f5d07513"
TWILIO_PHONE_NUMBER = "+12679523148"

app = Flask(__name__)

@app.route("/atender", methods=["POST"])
def atender():
    resposta = VoiceResponse()

    with resposta.loop(10):  # Repete até 10 vezes (~10 minutos)
        resposta.play("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", loop=1)
        resposta.pause(length=60)  # Pausa de 1 minuto
        resposta.say("Olá! Aguarde um momento enquanto transferimos sua chamada.")

    return str(resposta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
