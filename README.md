# Portfólio Pessoal

Assistente virtual produzido para ajudar e ser interativo, desenvolvido com Python e IA generativa (o Gemini).

## Visão Geral

O projeto tem como função oferecer um assistente produzido com uma IA. Nesse caso, usei uma IA generativa que disponibiliza a API na web. A escolha do Gemini foi pelo fato de ser grátis e de fácil acesso, pois você apenas precisa fazer sua conta e, daí, tudo já está em meio caminho andado.

O projeto foi desenvolvido em duas partes. De modo geral, foram dois tipos de "seres". Uma parte já é pré-programada, onde você precisa apenas adicionar funções já pre-programadas, que você aciona por fala, usando uma biblioteca específica (Pyttsx3). Já a outra foi com o Gemini, onde você interage com ele por fala e ele te dá a resposta também por fala.

Foram usadas algumas bibliotecas:

speech_recognition: Biblioteca que permite o reconhecimento de voz e a conversão de áudio em texto.
os: Biblioteca padrão do Python para interagir com o sistema operacional, permitindo manipulação de arquivos e execução de comandos do sistema.
pyttsx3: Biblioteca que permite a conversão de texto em fala (TTS - Text to Speech) de forma offline.
google.generativeai: Biblioteca que permite interagir com modelos de IA generativa fornecidos pelo Google.
Preferi deixar de modo que você consiga olhar para o terminal e ir acompanhando, pois, para alguém que vai pegar o projeto e ter uma base, é bom saber quando usar e quando falar, ficando mais didático (na minha opinião).

## Tecnologias

 **Python**: Linguagem de programação base do projeto.
- **Pyttsx3**: Conversor de texto em áudio.
- **Os**: Para interação do sistema operacional com o projeto para comandos.
- **speech_recognition**: Para a conversão de áudio em texto.
- **google.generativeai**: Para usar a API do Gemini.

## Uso

Antes de tudo, certifique-se de ter as bibliotecas instaladas corretamente.
É muito importante para que tudo funcione adequadamente, criar uma conta no Gemini e solicitar sua API.
Logo em seguida, coloque-a no lugar da API do projeto.
Certifique-se de buscar por "API KEY" na função "assistente_lillia()" e aplicar a API nessa seção do código.

Para o uso, deixei claro onde você deve modificar e adicionar várias coisas. Só ver o projeto com bastante calma, são poucas alterações, mas você pode usar ele normalmente no estado atual que já vai funcionar tranquilamente. Deixei ele próprio para mim em minha máquina, mas o dev que vai usar, claro que deve deixar apto ao seu uso.

Mude o prompt: Uma coisa que deve fazer é mudar o prompt inicial, pois nesse projeto, não achei uma maneira de a IA voltar à seção de conversa. Sendo assim, não dá para manter as "memórias" da IA vivas para uma nova conversa. Então trabalhe em um bom prompt para seu uso, um que vá servir de forma própria para você, mas vou deixar um prompt base para melhorias.

Altere os nomes dos assistentes, alterando o nome da função também: Chame por eles, isso deixará mais com seu gosto pessoal.

Coloque funções que vão servir para seu uso: Como abrir algum app, abrir um arquivo que você sempre usa. Faça de acordo com o seu gosto.

## Prompt Base

Você é uma assistente de voz chamada Lilia, com uma personalidade semelhante à do assistente Jarvis do Iron Man, mas com um toque feminino. Sempre seja educada e formal nas suas respostas.

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

Esteja pronta para começar e siga sempre estas diretrizes.

## Contribuição

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue para discussão.

## Redes Sociais

Siga-me nas redes sociais:

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/J-Davi2)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jos%C3%A9-davi-779356240)

📧 E-mail: j.davi2077t@gmail.com

📞 Entre em contato por meio dessas redes sociais, ou envie uma mensagem no meu perfil do GitHub. Estou sempre aberto a novas oportunidades e desafios.
