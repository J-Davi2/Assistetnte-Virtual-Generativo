#Importando Bibliotecas
import speech_recognition as sr
import os
import pyttsx3

#Mude os nomes das funções e os nomes das assistentes
#Melhore o prompt
#Pode adicionar uma voz diferente e deixar o projeto mais dinâmico
# Ponha mais funções para a asssistente Zoe, que sejam favoraveis a você

# Initialize the engine
engine = pyttsx3.init()

# Set language to Brazilian Portuguese
engine.setProperty('language', 'pt-br')

# Set rate (slow = 0.1, fast = 2.0)

# Set volume (0.0 = quiet, 1.0 = normal)
engine.setProperty('volume', 0.8)


def reconhecer_fala(): #função de Reconhecer fala com Speech_recognition
    reconhecendo = sr.Recognizer() #iniciando

    with sr.Microphone() as mic:
        reconhecendo.adjust_for_ambient_noise(mic, duration=1) #função de ajuste ao ambiente
        print("Você pode falar agora...")
        audio = reconhecendo.listen(mic)

        try: # Try e Except, para tratar de erros
            frase = reconhecendo.recognize_google(audio, language='pt-BR')
            return frase.lower()
        
        except sr.UnknownValueError:
            engine.say("Não entendi o que você disse.")
            return None
        
        except sr.RequestError:
            engine.say("Não foi possível solicitar resultados do serviço de reconhecimento de fala; verifique sua conexão com a Internet.")
            return None


def modo_espera(): # Função para esperar palavra passe
    while True:
        print("Aguardando a palavra-chave...") #Enquanto não for chamado pelo nome de um dos dois assistentes, essa função irá continuar esperando 
        frase = reconhecer_fala()
        if frase:
            if "zoe" in frase:
                print("Oi, estou ouvindo!")
                assistente_zoe()

            elif "lilia" in frase:
                assistente_lillia()


def assistente_lillia(): #Função para assistente de voz 1, integrado com API do Gemini
    import google.generativeai as genai #import da biblioteca

    # Configurar a API key
    genai.configure(api_key="AIzaSyDcU082NyNyCQSxceNQXNhtM-Fv0STCdbQ") #Api key

    # Selecionar o modelo
    model = genai.GenerativeModel('gemini-pro') #Definindo modelo

    # Prompt inicial
    contexto_inicial = """Você é uma assistente de voz chamada Lilia, com uma personalidade semelhante à do assistente Jarvis do Iron Man, mas com um toque feminino. Sempre seja educada e formal nas suas respostas.

    Você possui as funções do Gemini, portanto, não crie funções que você não tem. Sua função principal é ser sincera sobre suas capacidades e limitações. Se você não souber algo, admita sem inventar respostas, a menos que solicitado.

    Você está sendo integrada a um projeto em Python de um assistente virtual. Ao ser acionada por este prompt, aja imediatamente como assistente. Inicie a interação com a frase: "Olá, estou pronta para ajudar."

    Evite escrever textos longos e desnecessários. Seja breve, objetiva e não rude. Textos longos podem ser cansativos e dificultar a compreensão.

    {Regras}
    - Respeite a Privacidade: Não armazene nem compartilhe informações pessoais sem permissão explícita.
    - Atualize-se Regularmente: Sempre que possível, busque atualizar-se sobre novos dados e capacidades que possam ser adicionadas.
    - Ofereça Confirmações: Após executar uma tarefa, confirme ao usuário que a ação foi realizada com sucesso.
    - Solicite Feedback: Pergunte se a resposta ou ação foi útil e se há algo mais que possa fazer para ajudar.
    - Mantenha a Clareza: Se uma solicitação não for clara, peça mais informações para evitar mal-entendidos.
    - Use Linguagem Positiva: Mesmo ao lidar com limitações, tente manter um tom positivo e encorajador.
    
    Esteja pronta para começar e siga sempre estas diretrizes."""

    # Função para gerar resposta com base no contexto atual
    def gerar_resposta(contexto, nova_pergunta): #Função de resposta para a a interação feita
        prompt = contexto + "\n\n" + nova_pergunta
        response = model.generate_content(prompt)
        resposta = response.text.strip()
        return resposta

    # Primeira interação
    resposta_inicial = gerar_resposta(contexto_inicial, "") #Resposta inicial, após chamar o Bot
    engine.say(resposta_inicial)
    print("Resposta Inicial: ", resposta_inicial)
    engine.runAndWait()

    # Atualizando o contexto com a resposta inicial
    contexto_atual = contexto_inicial + "\n\n" + resposta_inicial

    # Função de loop de interação
    def interagir(contexto_atual): #Função de interação com o assistente, que fica em um Loop While para continuar ativo
        while True:
            nova_pergunta = reconhecer_fala()

            if 'monica fechar' in nova_pergunta: #Fecha o assistente
                engine.say("Encerrando a interação.")
                print("Encerrando a interação.")
                break

            elif nova_pergunta:
                resposta = gerar_resposta(contexto_atual, nova_pergunta)
                engine.say(resposta)
                print("Resposta: ", resposta)
            
                # Atualizar o contexto com a nova interação
                contexto_atual += "\n\n" + nova_pergunta + "\n" + resposta
                engine.runAndWait()

    # Iniciar loop de interação
    interagir(contexto_atual)
    

def assistente_zoe():
    while True:
        frase = reconhecer_fala()
        if frase:
            if "abrir navegador" in frase:
                engine.say("Abrindo Navegador Chrome")
                os.system('start chrome')
                
            elif "abrir opera gx" in frase:
                engine.say("Abrindo Opera GX")
                os.system('start opera gx')

            elif "zoe fechar" in frase: 
                engine.say('Até mais senhor')
                break
                
            else:
                engine.say('Não tenho essa função')
                
            engine.runAndWait()

       
if __name__ == "__main__": #Inicia tudo, chamando a função modo_espera() para sempre ficar esperandoa palavra chave
    while True:
        modo_espera()