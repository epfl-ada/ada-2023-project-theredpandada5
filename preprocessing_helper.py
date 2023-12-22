import matplotlib.pyplot as plt

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

def plot_gpt_answers_pie_charts(df, q_names):
    """
    Plots pie charts representing the percentage of 0's, 1's, and 2's for each question contained 
    in the dataframe (20 questions)

    Parameters
    ----------
    df : the dataframe containing the answers to the binary questions
    q_names : names of each question to use as a title for each subplots
    """
    fig, ax = plt.subplots(nrows = 4, ncols = 5, figsize = (12,10))

    for r in range(4):
        for c in range(5):
            counts = df[f'q_{r*5+c}'].value_counts()
            ax[r,c].pie([counts[0], counts[1], counts[2]],
                        labels = [0, 1, 2],
                        autopct=lambda p: '{:.1f}%'.format(p),
                        startangle=90, shadow=False)
            ax[r,c].set_title(q_names[r*5+c])
    
    fig.suptitle('Pie charts of percentage of answers (0, 1, and 2) for each question', y=1.01, fontsize=15)
    fig.tight_layout()
    plt.show()