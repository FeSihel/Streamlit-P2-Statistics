# Bibliotecas:
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st 

# Dia 5: st.write
# Ao instalar streamlit e python, ele já vem com pandas, numpy e altair
st.header("Estatísticas")

st.subheader("st.write (dia 5)")
# Dataframes
df = pd.DataFrame({
    "1a coluna": ["1A", "2A", "3A", "4A"],
    "2a coluna": ["1B", "2B", "3B", "4B"],
})

# Gráficos de pontos, valores gerados aleatoriamente.
df2 = pd.DataFrame(
    np.random.rand(100, 3), 
    columns=["a", "b", "c"])
c = alt.Chart(df2).mark_circle().encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])

st.write("Tabela", df, "Gráfico", c, "Valores gerados aleatoriamente")

# Dia 9: st.line_chart
st.subheader("st.linechart (dia 9)")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ["a", "b", "c"]
)
st.line_chart(chart_data)
st.write("Valores também gerados aleatóriamente")

# Dia 14: leitor de CSV
# Terminal: py -m pip install streamlit_pandas_profiling
st.subheader("Leitor de CSV (dia 14)")

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
st.dataframe(df)

st.write("Fonte: https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
