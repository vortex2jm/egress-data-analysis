import pandas as pd
import plotly.graph_objects as go
from modules.df_manage import extract_data_and_amount, filter_dataframe

# PROCESSING DATA=========================================== #
df = pd.read_csv("./data/egressos2023.csv")

years_list, students_amount_per_year, students_amount = extract_data_and_amount(df, 'Edicao')
courses_list, students_amount_per_course, x = extract_data_and_amount(df, 'Curso UFES 2023/1')

# REGISTERED================================================ #
df_registered = filter_dataframe(df, 6, True, 0)

registered_years_list, registered_students_amount_per_year, registered_students_amount = extract_data_and_amount(df_registered, 'Edicao') 
registered_courses_list, registered_students_amount_per_course, x = extract_data_and_amount(df_registered, 'Curso UFES 2023/1')

# APROVED + REGISTERED================================================ #
df_aproved = filter_dataframe(df_registered, 3, True, 0)

aproved_years_list, aproved_students_amount_per_year, aproved_students_amount = extract_data_and_amount(df_aproved, 'Edicao')
aproved_courses_list, aproved_students_amount_per_course, x = extract_data_and_amount(df_aproved, 'Curso UFES 2023/1')


# CCOMP X ENGCOMP================================================ #
df_engcomp_r = filter_dataframe(df_registered, 4, False, 'ENGENHARIA DA COMPUTAÇÃO - BACHARELADO INTEGRAL')
engcomp_years_list_r, eng_comp_amount_per_year_r, eng_comp_students_total_r = extract_data_and_amount(df_engcomp_r, 'Edicao')

df_ccomp_r = filter_dataframe(df_registered, 4, False, 'CIÊNCIA DA COMPUTAÇÃO - BACHARELADO VESPERTINO')
ccomp_years_list_r, ccomp_amount_per_year_r, ccomp_students_total_r = extract_data_and_amount(df_ccomp_r, 'Edicao')

df_engcomp_a = filter_dataframe(df_aproved, 4, False, 'ENGENHARIA DA COMPUTAÇÃO - BACHARELADO INTEGRAL')
engcomp_years_list_a, eng_comp_amount_per_year_a, eng_comp_students_total_a = extract_data_and_amount(df_engcomp_a, 'Edicao')

df_ccomp_a = filter_dataframe(df_aproved, 4, False, 'CIÊNCIA DA COMPUTAÇÃO - BACHARELADO VESPERTINO')
ccomp_years_list_a, ccomp_amount_per_year_a, ccomp_students_total_a = extract_data_and_amount(df_ccomp_a, 'Edicao')

# 2021 x 2022 x 2023 egresses=========================== #
df_2021 = pd.read_csv('./data/egressos2021.csv')
df_2022 = pd.read_csv('./data/egressos2022.csv')

egresses_amount_per_year = []
egresses_amount_per_year.append(len(df_2021.index))
egresses_amount_per_year.append(len(df_2022.index))
egresses_amount_per_year.append(len(df.index))

semesters = ['2021', '2022', '2023']

# GRAPHS================================================ #
year_graph = go.Figure(data=[go.Pie(labels= years_list, values=students_amount_per_year)])
course_graph = go.Figure(data=[go.Pie(labels= courses_list, values=students_amount_per_course)])

aproved_year_graph = go.Figure(data=[go.Pie(labels= aproved_years_list, values=aproved_students_amount_per_year)])
aproved_course_graph = go.Figure(data=[go.Pie(labels=aproved_courses_list , values=aproved_students_amount_per_course)])
comp_graph_a = go.Figure(data=[
    go.Bar(name='Engenharia da Computação', x=engcomp_years_list_a, y=eng_comp_amount_per_year_a),
    go.Bar(name='Ciência da Computação', x=ccomp_years_list_a, y=ccomp_amount_per_year_a)
])

registered_year_graph = go.Figure(data=[go.Pie(labels=registered_years_list , values=registered_students_amount_per_year)])
registered_course_graph = go.Figure(data=[go.Pie(labels=registered_courses_list , values=registered_students_amount_per_course)])
comp_graph_r = go.Figure(data=[
    go.Bar(name='Engenharia da Computação', x=engcomp_years_list_r, y=eng_comp_amount_per_year_r),
    go.Bar(name='Ciência da Computação', x=ccomp_years_list_r, y=ccomp_amount_per_year_r)
])

semesters_graph = go.Figure(data=[go.Bar(x=semesters, y=egresses_amount_per_year)])

# EDITING GRAPHS LAYOUTS================ #
colors = {
    'background': '#020220',
    'text': '#FFFFFF'
}
year_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
aproved_year_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
course_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
aproved_course_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
registered_year_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
registered_course_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
comp_graph_r.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis=dict(title='Edição')
)
comp_graph_a.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis=dict(title='Edição')
)
semesters_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    yaxis=dict(title='Alunos'),
    xaxis=dict(title='Semestre')
)
