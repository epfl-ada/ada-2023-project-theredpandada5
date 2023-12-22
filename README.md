# TheRedPandADA5

## Romance movies: The recipe that goes straight to the heart

### Data Story

You can find our data story [here](https://epfl-ada.github.io/ada-2023-project-theredpandada5/ada_website/)


### Abstract

What makes us like romance movies? Hopeless romantics might argue that they can watch any romance movie out there, but even they have to admit that the simple fact of two people falling in or out of love with each other does not equal a good quality story.
Do we like their predictability, that they are filled with particular clichés, recurring actions or persona archetypes?
We cannot analyze the likability of actors, but we can match on the written layers of movie making and use IMDB movie ratings as a metric for how much movies are liked.
The CMU dataset gives us details about the movies and specific characters. We then complete this data by asking GPT3.5 binary questions about movie tropes to uncover the secrets in plots. Lastly, to uncover even more, we assign persona types to the characters using the “Learning Latent Personas of Film Characters”  model.

 

### Research Questions
How do movie personas and tropes evolve over time?
 What movie personas are most common? Which ones correlate most with higher ratings?
Which tropes are most common? How are they correlated with the ratings?
Which tropes and personas in particular significantly impact the ratings, and how (methodology: matched study)?

### How to read our pipeline: 

- `Data preprocessing.ipynb`: Here are the steps and explanations for our data preprocessing. The IMDB ratings are added to the movies dataframe and a persona type is associated to each character in the characters dataframe.  Romance films are extracted from the movies dataframe. For the GPT questions, there is a dataframe related to the questions and another related to the answers with the romance films associates. In this project we then work with the preprocessed dataframes which are saved into tsv files at the end of this notebook (and can be found in the folder ./Data/Preprocessed/).

- `Statistics Pipeline.ipynb`: This is the main pipeline notebook completed from milestone 2. The first part contains exploratory data analysis. We start off the Milestone 3 part with exploratory analysis about the GPT data. Then we have a closer look at the interaction between GPT and the ratings as well as the personas and the ratings, and finally all three aspects, using regressions. Lastly, we complete our analysis with a matched study to analyze the effect of specific questions and/or personas on the movie ratings. 

- `preprocessing_helper.py`: Contains helper functions used in both notebooks. 

- `gpt_methods.ipynb`: Contains the code that calls GPT3.5 and was used to obtain the answers for the binary search about the romance tropes. It explains how the requests are made and the results stored.

### Proposed additional datasets: 
- IMDB movie ratings: The IMDB ratings give us a measure of how movies are rated by current audiences. The dataset is constructed from IMDB users since 1990 and overlaps with ca. 55'000 movies from the CMU dataset (against 8000 box office revenue values in the CMU dataset). The dataset used to obtain the ratings is IMDB's data dump. Information about it can be found on https://developer.imdb.com/non-commercial-datasets/ : `imdb_ratings.tsv` is used to obtain the number of votes and the ratings for each movie. After preprocessing `movie.metadata.augmented.tsv` contains the movies merged with their ratings.

- Binary Query for plot elements: The binary questions asked can be found in `./Data/trope_questions.txt`.

    The following websites were used in addition to our own imagination for the questions: 
    - https://movieweb.com/romance-movies-cliches/
    - https://reelrundown.com/movies/Top-Romantic-Comedy-Movie-Cliches
    - https://brightside.me/articles/12-cliches-from-romantic-movies-that-make-more-sense-than-we-care-to-admit-806011/


- Personas Dataset: In [Bamman, O'Connor and Smith, "Learning Latent Personas of Film Characters" (ACL 2013)](http://aclweb.org/anthology/P/P13/P13-1035.pdf) a model was developed that manages to extract persona types from movies summaries. Each persona type is characterized by a set of topics. The information on personas was obtained by running the code from https://github.com/dbamman/ACL2013_Personas. 

### Methods: 

#### Data collection and preprocessing: 

**Step 1: Loading, cleaning and dealing with duplicates or missing values:** 

The movie and character datasets are loaded. The missing and incorrect values, duplicates and outliers are handled appropriately. Irrelevant columns are removed.

**Step 2: Complete movies dataset with IMDB ratings:** 

From the IMDB dataset the ratings are loaded. After cleaning, the ratings are integrated to the movies dataset. 

**Step 3: Personas preprocessing:** 

The code from [Bamman, O'Connor and Smith, "Learning Latent Personas of Film Characters" (ACL 2013)](http://aclweb.org/anthology/P/P13/P13-1035.pdf) assigns a probability distribution of persona types, each containing a corresponding list of topics, to what it recognizes as movie characters from the plot summaries. Only the movie characters corresponding to our dataset must be extracted. The persona with the highest probability is then assigned to the character. The personas are integrated into the characters dataset.

**Step 4: Plot analysis preprocessing - Binary search on romantic movies with GPT-3.5:**

Elements from movie plots are extracted by asking the GPT-3.5 API binary questions about the movie tropes in our dataset. GPT-3.5 then must output 0 for False, 1 for True and 2 for unknown. We obtain around 6000 movies that we can analyze, using the binary answers.


#### Visualization and Analysis: 

**Step 5: Data Visualization and statistical analysis:**

We used Matplotlib and Seaborn to visually represent the relevant data. Line graphs mainly for basic statistics and temporal analysis. Box plots and histograms to examine overall distributions, and box plots (with confidence intervals)  to compare distributions between categories (genres, questions).
To deepen the analysis by persona, we incorporated heat maps, bar charts and stacked plots (with or without genres). Persona characteristics were described using line and radar diagrams.
To analyze the GPT answers, we used pie charts and bar charts, as well as line plots to examine the evolution of ratings and average answers over time.


**Step 6: Analysis:**

For the first three research questions, we find out which personas and tropes are most used in romance movies. To determine if tropes and persona types have an impact on the ratings, we use several regression models and decision trees.  
Then we further analyze correlations between ratings and types of personas/tropes by building a matched study. We have a look at intercorrelations between similar tropes and/ or personas to see which have higher ratings and how they evolve over time.





### Organization within the team: (A list of internal milestones up until project Milestone P3)

| Team Member     | Tasks |
| ----------- | ----------- |
| Robinson   | Integrating IMDB dataset, run code from CMU personas paper, questions on romance tropes for GPT, GPT API binary search, matched study |
| Sophie   | Exploratory data analysis, data preprocessing, initial data analysis, milestone 3 notebook, data story plots |
| Eva | Exploratory data analysis, personas-genres assignment, statistics on ratings, regressions on personas, read me|
| Florence | Exploratory data analysis, questions on general tropes for GPT, personas-genres statistical measures, website, data story|
| Laetitia | Exploratory data analysis, find datasets, team coordination, ReadMe, feature selection and regressions on binary questions, data story|



