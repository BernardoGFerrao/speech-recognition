import speech_recognition as sr
import time

def tratar_audio(rec, audio):
    global acabou
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
        if "encerrar gravação" in texto:
            acabou = True
    except sr.UnknownValueError:
        print("Não entendi o que você disse")
    except sr.RequestError as e:
        print(f"Erro ao requisitar resultados do serviço Google Speech Recognition; {e}")

acabou = False

rec = sr.Recognizer()

with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    rec.pause_threshold = 0.8
    print("Pode começar a falar:")

    # Iniciar a escuta em segundo plano
    parar_ouvir = rec.listen_in_background(microfone, tratar_audio)

    # Loop principal
    while not acabou:
        time.sleep(0.1)

    # Parar a escuta em segundo plano
    parar_ouvir(wait_for_stop=False)
