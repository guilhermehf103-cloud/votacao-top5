import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Votação Brainstorming", layout="centered")

st.title("🗳️ Votação: Escolha suas 5 ideias favoritas")
st.write("Selecione exatamente 5 ideias do brainstorming abaixo. As mais votadas aparecerão no final!")

# Lista de ideias
ideias = [
    "ERP/API para integração",
    "BI e IA para previsão de demanda",
    "IoT para rastreamento logístico",
    "Automação de compras",
    "Parcerias estratégicas com fornecedores",
    "MRP para planejamento de produção",
    "Dashboard de KPIs em tempo real",
    "App mobile para supervisores",
    "Simulador de cenários logísticos",
    "Treinamento e cultura de dados"
]

# Seleção do usuário
selecionadas = st.multiselect("Escolha 5 ideias:", ideias)

# Validação
if len(selecionadas) > 5:
    st.warning("Você só pode escolher 5 ideias.")
elif len(selecionadas) < 5:
    st.info("Selecione exatamente 5 ideias para votar.")
else:
    if st.button("✅ Confirmar Voto"):
        # Salvar votos
        arquivo = "votos.csv"
        if os.path.exists(arquivo):
            df = pd.read_csv(arquivo)
        else:
            df = pd.DataFrame(columns=["Ideia"])

        novo_voto = pd.DataFrame({"Ideia": selecionadas})
        df = pd.concat([df, novo_voto], ignore_index=True)
        df.to_csv(arquivo, index=False)

        st.success("Voto registrado com sucesso!")

# Mostrar resultados acumulados
if os.path.exists("votos.csv"):
    st.subheader("🏆 Top 5 ideias mais votadas até agora:")
    df = pd.read_csv("votos.csv")
    contagem = df["Ideia"].value_counts().head(5)
    st.table(contagem)
