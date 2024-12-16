# luna_assistente_virtual

🪐 Luna - Assistente Virtual Inteligente
Luna é uma assistente virtual desenvolvida em Python, capaz de interagir com o usuário por meio de comandos de voz e texto. Utilizando processamento de linguagem natural (NLP) avançado com o modelo command-xlarge-nightly da Cohere, Luna proporciona uma experiência fluida e interativa.

✨ Funcionalidades
🎙️ Reconhecimento de voz: Luna ouve e interpreta comandos através do microfone.
🧠 Processamento de linguagem natural: Com o modelo avançado da Cohere, Luna compreende e responde aos comandos do usuário.
🔊 Respostas em voz: As respostas de Luna são transformadas em áudio usando a biblioteca gTTS.
🎼 Reprodução de áudio: Integração com pygame para reproduzir as respostas geradas em áudio.



Aqui está um exemplo de README para o projeto da assistente virtual Luna.

🪐 Luna - Assistente Virtual Inteligente
Luna é uma assistente virtual desenvolvida em Python, capaz de interagir com o usuário por meio de comandos de voz e texto. Utilizando processamento de linguagem natural (NLP) avançado com o modelo command-xlarge-nightly da Cohere, Luna proporciona uma experiência fluida e interativa.

✨ Funcionalidades
🎙️ Reconhecimento de voz: Luna ouve e interpreta comandos através do microfone.
🧠 Processamento de linguagem natural: Com o modelo avançado da Cohere, Luna compreende e responde aos comandos do usuário.
🔊 Respostas em voz: As respostas de Luna são transformadas em áudio usando a biblioteca gTTS.
🎼 Reprodução de áudio: Integração com pygame para reproduzir as respostas geradas em áudio.
🛠️ Tecnologias e Dependências
O projeto foi desenvolvido utilizando Python e as seguintes bibliotecas:

Dependência	Descrição
cohere -	Integração com o modelo de linguagem avançado da Cohere.
speech_recognition (sr) -	Reconhecimento de fala para capturar comandos de voz.
gTTS -	Geração de áudio a partir do texto usando o Google Text-to-Speech.
pygame	- Reprodução de arquivos de áudio.
os, time -	Gerenciamento de arquivos e controle de tempo (nativo do Python).

🔧 Instalação
1. Clone o repositório:
    git clone https://github.com/sarmanhodev/luna_assistente_virtual.git
    cd luna_assistente_virtual


2. Crie um ambiente virtual (recomendado):
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3.Instale as dependências:
   pip install -r requirements.txt


4. Configuração do API Key:
   Crie uma conta na Cohere (https://cohere.ai/)



🚀 Como usar
1. Execute o script principal:
    python testecohere.py

2. Fale diretamente no microfone após o comando iniciar.

3. A Luna responderá com um áudio gerado automaticamente.



Desenvolvido por Diego Sarmanho
