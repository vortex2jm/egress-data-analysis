from dash import Dash, dcc, html
import modules.graphs as gp

# INTIALIZING SERVER=================== #
app = Dash(__name__)
app.title = 'Introcomp'

text_style = {
    'textAlign': 'center',
    'color': gp.colors['text']
}

# CREATING PAGE STRUCTURE============================================================== #
app.layout = html.Div(style={'backgroundColor': gp.colors['background']}, children=[
    html.H1(children='Análise de egressos do Introcomp que foram aprovados na UFES no semestre 2023/1', style=text_style),
    html.H2(children=f'''Total de egressos: {gp.students_amount}''', style=text_style),
    html.H3(children=f'''Por edição:''', style=text_style),
    dcc.Graph(id='yg',figure=gp.year_graph),
    html.H3(children=f'''Por curso:''', style=text_style),
    dcc.Graph(id='cg',figure=gp.course_graph),
    
    html.H2(children=f'''Total de egressos matriculados na UFES: {gp.registered_students_amount}''', style=text_style),
    html.H3(children=f'''Por edição:''', style=text_style),
    dcc.Graph(id='ryg', figure=gp.registered_year_graph),
    html.H3(children=f'''Por curso:''', style=text_style),
    dcc.Graph(id='rcg', figure=gp.registered_course_graph),
    html.H3(children=f'''EngComp|Ccomp x Edição''', style=text_style),
    dcc.Graph(id='ecr', figure=gp.comp_graph_r),

    html.H2(children=f'''Total de egressos matriculados na UFES que terminaram o Introcomp: {gp.aproved_students_amount}''', style=text_style),
    html.H3(children=f'''Por edição:''', style=text_style),
    dcc.Graph(id='ayg', figure=gp.aproved_year_graph),
    html.H3(children=f'''Por curso:''', style=text_style),
    dcc.Graph(id='acg', figure=gp.aproved_course_graph),
    html.H3(children=f'''EngComp|Ccomp x Edição''', style=text_style),
    dcc.Graph(id='eca', figure=gp.comp_graph_a),

    html.H2(children=f'''Egressos do introcomp matriculados na UFES nos 3 últimos semestres''', style=text_style),
    dcc.Graph(id='eps', figure=gp.semesters_graph)
])

if __name__ == '__main__':
    app.run_server()
