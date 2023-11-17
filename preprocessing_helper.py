def get_values_occurrences(dataframe, column_name):
    """
    Computes and returns a dictionary of each value and its number of occurences
    in the given column of the given dataframe, where the column of the dataframe
    contains dictionaries mapping something (freebase id in practice) to the value

    Parameters
    ----------
    dataframe : the dataframe containing the dictionaries
    column_name : the name of the column in the dataframe containing the dictionaries

    Returns
    ------
    A dictionary mapping value to number of times it occurs
    """
    movies_df_column = dataframe[column_name].map(lambda dictionary : (set(dictionary.values())))

    values_occurrences = {}
    for column in movies_df_column:
        for value in column:
            values_occurrences[value.lower()] = values_occurrences.get(value.lower(), 0)+1

    return values_occurrences