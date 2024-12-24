import plotly.express as px
import pandas as pd

# Пример данных
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

fig = px.line(df, x='x', y='y', title='Пример графика с использованием Plotly')
fig.update_traces(mode='markers+lines')
fig.show()
