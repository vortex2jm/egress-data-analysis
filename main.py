import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import plotly.graph_objects as go

# ================================================ #
df = pd.read_csv("egressos.csv")
courses_column = list(df['Curso UFES 2023/1'])
courses_column.sort()
courses_list = []

for course in courses_column:
    if course not in courses_list:
        courses_list.append(course)

students_amount_per_course = [0]*len(courses_list)

for i,list_course in enumerate(courses_list):
    for column_course in courses_column:
        if list_course == column_course:
            students_amount_per_course[i]+=1

# ================================================ #
year_graph = px.pie(df, values='Edicao', names='Edicao' , color_discrete_sequence=px.colors.sequential.RdBu)
course_graph = go.Figure(data=[go.Pie(labels= courses_list, values=students_amount_per_course)])

# Instanciating server #
app = Dash(__name__)
app.title = 'Introcomp'

colors = {
    'background': '#020220',
    'text': '#FFFFFF'
}
# ==========================================#
# Editando as cores dos gráficos
year_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
course_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# Criando dashboard web============================================================== #
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Introcomp - Análise de egressos',
    style={
      'textAlign': 'center',
      'color': colors['text']
    }),
    html.H3(children='''
        Egressos por edição
    ''',
    style={
      'textAlign': 'center',
      'color': colors['text']
    }),
    dcc.Graph(
        id='yg',
        figure=year_graph
    ),
    html.H3(children='''
        Egressos por curso
    ''',
    style={
      'textAlign': 'center',
      'color': colors['text']
    }),
    dcc.Graph(
        id='cg',
        figure=course_graph
    ),
])

if __name__ == '__main__':
    app.run_server()
    # print(df)
    # print("oi")
