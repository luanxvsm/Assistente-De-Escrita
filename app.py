# app.py

import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DA PÁGINA ---
# Define o título da aba do navegador, o ícone e o layout da página
st.set_page_config(
    page_title="Assistente de Escrita",
    page_icon="✍️",
    layout="centered",
)


# --- CONFIGURAÇÃO DA API E DO MODELO GEMINI ---
# Função para carregar o modelo de forma segura, usando o cache do Streamlit
@st.cache_resource
def load_gemini_model():
    """Carrega e configura o modelo Gemini a partir da chave de API nos segredos."""
    try:
        # Carrega a chave da API a partir do arquivo secrets.toml
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        return model
    except Exception as e:
        # Exibe um erro se a chave não for encontrada ou for inválida
        st.error(f"Erro ao configurar a API do Gemini: {e}")
        st.error(
            "Por favor, certifique-se de que sua chave de API está configurada corretamente no arquivo .streamlit/secrets.toml")
        return None


# Carrega o modelo
model = load_gemini_model()

# --- DEFINIÇÃO DOS PROMPTS ---
# Dicionário com os prompts para cada tipo de ação
# Isso organiza o código e facilita a adição de novas funcionalidades
PROMPTS = {
    "Correção Gramatical": "Corrija a gramática e a ortografia do seguinte texto. Preserve o estilo e o significado original. Apresente apenas o texto corrigido, sem adicionar comentários.",
    "Tornar Mais Amigável": "Reescreva o seguinte texto para que soe mais amigável, caloroso e pessoal. Use uma linguagem mais fluida e natural, como se estivesse conversando com um amigo, mas mantendo a mensagem principal intacta.",
    "Tornar Mais Profissional": "Refine o seguinte texto para um contexto de negócios formal. Torne-o mais claro, conciso, objetivo e profissional. Remova gírias e informalidades, garantindo que a mensagem seja polida e direta.",
    "Tornar Mais Persuasivo": "Transforme o seguinte texto em uma mensagem mais persuasiva e cativante. Use técnicas de copywriting para aumentar o impacto, destacar os benefícios e criar um senso de urgência ou importância."
}

# --- INTERFACE DO USUÁRIO (UI) ---

st.title("Assistente de Escrita com IA ✍️")
st.markdown("Corrija, refine e humanize seus textos com o poder do Gemini.")
st.divider()

# Área para o usuário inserir o texto
original_text = st.text_area("Cole seu texto original aqui:", height=200, placeholder="Escreva ou cole seu texto...")

# Menu de seleção para a ação desejada
chosen_action = st.selectbox(
    "Qual aprimoramento você deseja?",
    options=list(PROMPTS.keys())  # As opções são as chaves do nosso dicionário de prompts
)

# Botão para iniciar o processo
if st.button("✨ Aprimorar Texto"):
    # Verifica se o modelo foi carregado e se há texto para processar
    if model and original_text:
        with st.spinner("A IA está refinando seu texto... Por favor, aguarde."):
            # Seleciona o prompt correto com base na escolha do usuário
            prompt_template = PROMPTS[chosen_action]

            # Monta o prompt final
            final_prompt = f"{prompt_template}\n\n--- TEXTO ORIGINAL ---\n{original_text}"

            try:
                # Gera a resposta com o modelo Gemini
                response = model.generate_content(final_prompt)
                enhanced_text = response.text

                # Exibe os resultados lado a lado
                st.divider()
                st.subheader("Resultados")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### Texto Original")
                    st.info(original_text)
                with col2:
                    st.markdown("#### Texto Aprimorado")
                    st.success(enhanced_text)

            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a resposta: {e}")

    elif not original_text:
        st.warning("Por favor, insira um texto para ser aprimorado.")
    else:
        # Mensagem caso o modelo não tenha sido carregado
        st.error("O modelo de IA não pôde ser carregado. Verifique a configuração da API.")