# Assistente de Escrita com IA ✍️

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red.svg)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%20API-green.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

*Projeto final desenvolvido para a disciplina de Fundamentos de Inteligência Artificial. Esta aplicação web utiliza o poder da API Google Gemini para corrigir, refinar e "humanizar" textos, atuando como um assistente de escrita inteligente.*

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Configuração e Instalação](#configuração-e-instalação)
- [Como Executar](#como-executar)
- [Como Usar](#como-usar)
- [Autor](#autor)
- [Licença](#licença)

---

## 💡 Sobre o Projeto

O **Assistente de Escrita com IA** foi criado para resolver um problema comum: a necessidade de aprimorar a comunicação escrita. Muitas vezes, um texto pode estar gramaticalmente correto, mas seu tom pode não ser adequado para o público ou o contexto.

Esta ferramenta vai além de um simples corretor ortográfico. Ela utiliza um modelo de linguagem avançado (LLM) do Google para analisar o texto e reescrevê-lo com base no objetivo do usuário, seja para torná-lo mais profissional, amigável ou persuasivo. O projeto demonstra uma aplicação prática e interativa de IA generativa em uma interface web moderna e intuitiva construída com Streamlit.

---

## ✨ Principais Funcionalidades

-   **Correção Gramatical e Ortográfica:** Limpa o texto de erros básicos, preservando o significado original.
-   **Refinamento de Tom e Estilo:** Oferece múltiplas opções para "humanizar" o texto:
    -   **Amigável:** Ideal para comunicação informal, redes sociais e blogs.
    -   **Profissional:** Adequado para e-mails de trabalho, relatórios e contextos corporativos.
    -   **Persuasivo:** Otimizado para marketing, vendas e para convencer o leitor.
-   **Interface Intuitiva e Moderna:** A interface foi estilizada com CSS customizado para proporcionar uma experiência de usuário agradável e profissional.
-   **Comparação Lado a Lado:** Apresenta o texto original e o texto aprimorado lado a lado, facilitando a visualização das melhorias aplicadas pela IA.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

-   **Python:** Linguagem de programação principal.
-   **Streamlit:** Framework para a construção da interface web interativa.
-   **Google Generative AI (Gemini API):** API para acesso ao modelo de linguagem Gemini 1.5 Flash.

---

## ⚙️ Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_SEU_REPOSITORIO.git)
cd NOME_DO_SEU_REPOSITORIO
```

**2. Crie e ative um ambiente virtual:**
É uma forte recomendação usar um ambiente virtual para isolar as dependências do projeto.
```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate
```

**3. Instale as dependências:**
O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
```bash
pip install -r requirements.txt
```

**4. Configure a API Key do Gemini:**
- Crie uma pasta chamada `.streamlit` na raiz do projeto.
- Dentro dela, crie um arquivo chamado `secrets.toml`.
- Adicione sua chave de API ao arquivo, como no exemplo abaixo:
  ```toml
  # .streamlit/secrets.toml
  GEMINI_API_KEY = "SUA_CHAVE_DE_API_AQUI"
  ```

---

## ▶️ Como Executar

Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no seu terminal:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador padrão.

---

## 🚀 Como Usar

1.  **Cole o texto** que deseja aprimorar na área de texto principal.
2.  **Escolha a ação** desejada no menu de seleção (ex: "Tornar Mais Profissional").
3.  **Clique no botão** "✨ Aprimorar Texto".
4.  **Veja o resultado!** O texto original e a versão aprimorada pela IA aparecerão lado a lado para comparação.

---

## 👨‍💻 Autor

Feito com ❤️ por **Luan Victor Santana de Macêdo, Gabriel Figueiredo de Andrade, Murilo Henrique Gomes Fernandes, Thiago Germano do Nascimento, Caio Gomes**

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
