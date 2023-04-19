import pandas as pd
import plotly.express as px

df = pd.read_csv("egressos.csv")
# print(df)

edition_column = df["Edicao"]
# edition_column = list(df["Edicao"])
# edition_column.sort()
# print(edition_column)

pie_graph = px.pie(edition_column, color_discrete_sequence=px.colors.sequential.RdBu)


pie_graph.show()
