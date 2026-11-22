# Dia 5: st.write
# Ao instalar streamlit e python, ele já vem com pandas, numpy e altair
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.write("Estatísticas")

# Dataframes
df = pd.DataFrame({
    "1a coluna": ["1A", "2A", "3A", "4A"],
    "2a coluna": ["1B", "2B", "3B", "4B"],
})
st.write(df)

# Gráficos de pontos, valores gerados aleatoriamente.
df2 = pd.DataFrame(
    np.random.rand(100, 3), 
    columns=["a", "b", "c"])
c = alt.Chart(df2).mark_circle().encode(
        x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
st.write(c)