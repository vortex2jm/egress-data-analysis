def extract_data_and_amount(df, column):
    elements_column = list(df[column])
    elements_list = []

    for element in elements_column:
        if element not in elements_list:
            elements_list.append(element)

    elements_amount_in_vector = [0]*len(elements_list)

    for i,list_element in enumerate(elements_list):
        for column_element in elements_column:
            if list_element == column_element:
                elements_amount_in_vector[i]+=1

    return elements_list, elements_amount_in_vector, len(elements_column)

def filter_dataframe(df, index, eq_neq, compare_value):
    df_new = df
    if eq_neq:    
        for t in df_new.itertuples():
            if t[index] == compare_value:
                df_new = df_new.drop(t[0])
    else:
        for t in df_new.itertuples():
            if t[index] != compare_value:
                df_new = df_new.drop(t[0])
    return df_new
