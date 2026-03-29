import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Laboratório de PA", layout="wide")

st.title("🔢 Desvendando a Progressão Aritmética (PA)")
st.markdown("""
Uma Progressão Aritmética é uma sequência numérica onde a diferença entre termos consecutivos é sempre a mesma. 
Essa diferença é chamada de **razão (r)**. Sabia que toda PA é, no fundo, uma função do primeiro grau?
""")

# Barra lateral para controles
st.sidebar.header("Configure sua Sequência")
a1 = st.sidebar.number_input("Primeiro termo (a1):", value=1)
r = st.sidebar.slider("Razão (r):", min_value=-10, max_value=10, value=2)
n_termos = st.sidebar.slider("Quantidade de termos (n):", min_value=5, max_value=50, value=10)

# Cálculo da PA
indices = list(range(1, n_termos + 1))
termos = [a1 + (i - 1) * r for i in indices]

# Criação do DataFrame para facilitar a manipulação
df = pd.DataFrame({'n (posição)': indices, 'an (valor)': termos})

# Criando o gráfico interativo com Plotly
fig = go.Figure()

# Linha da função (o caminho)
fig.add_trace(go.Scatter(x=df['n (posição)'], y=df['an (valor)'],
                         mode='lines',
                         name='Comportamento Linear',
                         line=dict(color='rgba(100, 100, 255, 0.3)', dash='dash')))

# Pontos da PA (os degraus)
fig.add_trace(go.Scatter(x=df['n (posição)'], y=df['an (valor)'],
                         mode='markers+text',
                         name='Termos da PA',
                         text=[f"a{i}" for i in indices],
                         textposition="top center",
                         marker=dict(size=10, color='royalblue', symbol='circle')))

fig.update_layout(
    title=f"Gráfico da PA: a1={a1} e r={r}",
    xaxis_title="Posição do termo (n)",
    yaxis_title="Valor do termo (an)",
    hovermode="x unified"
)

# Layout das colunas no Streamlit
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 Termos Gerados")
    st.dataframe(df, hide_index=True)
    
    st.subheader("💡 Fórmula da PA")
    st.latex(r"a_n = a_1 + (n - 1) \cdot r")
    st.write(f"Para esta sequência:")
    st.write(f"**a{n_termos} = {a1} + ({n_termos} - 1) * {r} = {termos[-1]}**")

with col2:
    st.subheader("📈 Visualização Geométrica")
    st.plotly_chart(fig, use_container_width=True)

# Explicação Pedagógica
st.info(f"""
### 🧐 O que observar?
1. **A Inclinação:** Quando a razão **r** é positiva, a reta sobe (crescente). Quando é negativa, a reta desce (decrescente).
2. **O Passo:** A razão é o "tamanho do passo" que você dá entre um ponto e outro no eixo Y.
3. **Função Linear:** Repare que os pontos estão perfeitamente alinhados! Isso acontece porque a PA segue a lógica de uma função: $f(n) = r \cdot n + (a_1 - r)$.
""")
