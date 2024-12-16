import cohere
import os
import time
import speech_recognition as sr
from gtts import gTTS
import pygame

# Configuração do cliente Cohere
co = cohere.Client('ESCREVER A CHAVE AQUI')

def obter_resposta(pergunta):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=f"Responda de forma resumida e direta em português do Brasil à seguinte pergunta: {pergunta}",
        max_tokens=500,
        temperature=0.7,
        stop_sequences=[".", "?", "!"]
    )
    return response.generations[0].text.strip()

def reconhecer_voz():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Aguarde... Estou ouvindo.")
        reconhecedor.adjust_for_ambient_noise(fonte)
        audio = reconhecedor.listen(fonte)
        
        try:
            frase = reconhecedor.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {frase}")
            return frase
        except sr.UnknownValueError:
            print("Desculpe, não consegui entender.")
            return None
        except sr.RequestError:
            print("Erro ao conectar ao serviço de reconhecimento de voz.")
            return None
        
        

def reproduzir_resposta(resposta):
    arquivo_audio = "resposta.mp3"
    
    if os.path.exists(arquivo_audio):
        os.remove(arquivo_audio)

    tts = gTTS(text=resposta, lang='pt')
    tts.save(arquivo_audio)
    
    pygame.mixer.init()
    pygame.mixer.music.load(arquivo_audio)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    os.remove(arquivo_audio)



def continuarPerguntas(confirma):
    if confirma and confirma.lower() == 'sim':
        print(f"Sua resposta foi {confirma}")
        reproduzir_resposta(f"Sua resposta foi {confirma}")
        
        time.sleep(1)
        strPergunta = "O que você deseja?"
        print(f"Assistente: {strPergunta}")
        reproduzir_resposta(strPergunta)
        
        strPedido = reconhecer_voz()
        if strPedido:
            strResposta = obter_resposta(strPedido)
            print(f"Assistente: {strResposta}")
            reproduzir_resposta(strResposta)
        
            time.sleep(1)
            strOutraPergunta = 'Deseja fazer outra pergunta?'
            reproduzir_resposta(strOutraPergunta)
            
            respostaOutraPergunta = reconhecer_voz()
            continuarPerguntas(respostaOutraPergunta)
    elif confirma and confirma.lower() == "não":
        print(f"Sua resposta foi {confirma}")
        reproduzir_resposta("Ok, encerrando a conversa.")
        return



def main():
    while True:
        print("Diga 'luna' para começar...")
        ativacao = reconhecer_voz()
        
        if ativacao and ativacao.lower() == 'luna':
            print("Assistente: Eu sou a Luna, sua assistente virtual. Precisa de alguma ajuda?")
            reproduzir_resposta("Eu sou a Luna, sua assistente virtual. Precisa de alguma ajuda?")
            
            confirma = reconhecer_voz()
            if confirma:
                continuarPerguntas(confirma)
            
        elif ativacao and "parar" in ativacao.lower():
            print("Encerrando a aplicação...")
            reproduzir_resposta("Encerrando a aplicação.")
            break

if __name__ == "__main__":
    main()
