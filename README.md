# TheRedPandADA5

## Romance movies: The recipe that goes straight to the heart

### Abstract

Movies are filled with clichés, recurring actions and persona archetypes, however these vary greatly amongst different genres. From the CMU dataset we have information on the movies, some of their characters and the plot summaries. For this study, we focus on romantic movies as many movies independent of genre contain at least one romantic subplot. Users can rate movies on IMDB only since 1990, we therefore get a more modern perspective on the older movies. We want to analyze what makes specific romantic movies more liked by larger audiences. To achieve this, the GPT-3.5 API is queried using binary questions to obtain answers about plot elements and "Learning Latent Personas of Film Characters" is used to extract a persona type for characters in specific movies. We can then analyze the ratings of romantic movies, as well as movies with some popular genres paired up with romance, over time.

### Research Questions
1. How do romantic movies evolve over time (ratings, personas, tropes)? 
2. What movie personas are most common? Which ones correlate most with higher ratings?
3. Which tropes are most common? How do they affect the ratings?
4. With what type of movie genres do romantic movies obtain the highest IMDB ratings? 

### How to read our pipeline: 

- `Data preprocessing.ipynb`: Here are the steps and explanations for our data preprocessing. The IMDB ratings are added to the movies dataframe and a persona type is associated to each character in the characters dataframe. In this project we then work with the preprocessed dataframes which are saved into tsv files at the end of this notebook (`movie.metadata.augmented.tsv` and `preprocessed_characters.tsv`).

- `Statistics Pipeline.ipynb`: This is the main pipeline notebook. We start off with exploratory analysis about the overall dataset. Then we have a closer look at romance and ratings related topics. We then have a look at personas, as well as their interactions with genres and romance movies.

- `preprocessing_helper.py`: Contains helper functions used in both notebooks. 

- `gpt_methods.ipynb`: Contains the code used to get the answer to the questions asked to GPT-3.5 about the romance tropes.

### Proposed additional datasets: 
- IMDB movie ratings: The IMDB ratings give us a measure of how movies are rated by current audiences. The dataset is constructed from IMDB users since 1990 and overlap with ca. 55'000 movies from the CMU dataset (against 8000 box office revenue values in the CMU dataset). The dataset used to obtain the ratings is IMDB's data dump. Information about it can be found on https://developer.imdb.com/non-commercial-datasets/ : `imdb_ratings.tsv` is used to obtain the number of votes and the ratings for each movie. After preprocessing `movie.metadata.augmented.tsv` contains the movies merged with their ratings.

- Binary Query for plot elements: The binary questions asked can be found in `./Data/trope_questions.txt`.

    The following websites were used in addition to our own imagination for the questions: 
    - https://movieweb.com/romance-movies-cliches/
    - https://reelrundown.com/movies/Top-Romantic-Comedy-Movie-Cliches
    - https://brightside.me/articles/12-cliches-from-romantic-movies-that-make-more-sense-than-we-care-to-admit-806011/


- Personas Dataset: In [Bamman, O'Connor and Smith, "Learning Latent Personas of Film Characters" (ACL 2013)](http://aclweb.org/anthology/P/P13/P13-1035.pdf) a model was developed that manages to extract persona types from movies summaries. Each persona type is characterized by as set of topics. The information on personas was obtained by running the code from https://github.com/dbamman/ACL2013_Personas. 

### Methods: 

#### Data collection and preprocessing: 

**Step 1: Loading, cleaning and dealing with duplicates or missing values:** 

The movie and character datasets are loaded. The missing and incorrect values, duplicates and outliers are handled appropriately. Irrelevant columns are removed.

**Step 2: Complete movies dataset with IMDB ratings:** 

From the IMDB dataset the ratings are loaded. After cleaning, the ratings are integrated to the movies dataset. 

**Step 3: Personas preprocessing:** 

The code from [Bamman, O'Connor and Smith, "Learning Latent Personas of Film Characters" (ACL 2013)](http://aclweb.org/anthology/P/P13/P13-1035.pdf) assigns a probability distribution of persona types, each containing a corresponding list of topics, to what it recognizes as movie characters from the plot summaries. Only the movie characters corresponding to our dataset must be extracted. The persona with the highest probability is then assigned to the character. The personas are integrated into the characters dataset.

**Step 4: Plot analysis preprocessing - Binary search on romantic movies with GPT-3.5:**

Elements from movie plots are extracted by asking the GPT-3.5 API binary questions about the movie tropes in our dataset. GPT-3.5 then must output 0 for False, 1 for True and 2 for unknown. The questions must allow for no interpretation, else the results might vary according to previously asked questions.

#### Visualization and Analysis: 

**Step 5: Data Visualization and statistical analysis:**

We visualize the data using boxplots for the data distribution, (stacked) histograms (for various distributions), lineplots for evolution over the years and panels to compare different movie genre ratings by year or plot agents, patients and modifiees, scatterplots to visualize interactions between features. We perform ttests and calculate (Pearson's) correlation coefficients.

**Step 6: Analysis:**

For the first research question, we use the results of the other research questions to find correlations between the ratings and combinations of personas and tropes to find out which of them work well together (have higher ratings) and how they evolve over time.
For the second and third research questions, we find out which personas and tropes are most used in romance movies and further analyse correlations between ratings and types of personas/tropes using analysis tools. We can try to cluster similar tropes and/or personas based on their similarities (if some often appear together for example) and see if they have similar ratings.
For the fourth research question, we filter the dataframes to contain movies with "Romance" and one other genre and plot their average ratings over time in order to compare the evolution of the combination of "Romance" with other genres. We also compare their general statistics, as well how often certain combinations occur.


### Proposed timeline and Internal Milestones


The internal milestones are discussed every Tuesday and Friday until the project deadline

03/11/2023: First proposal of project choice, identify roadblocks. 

07/11/2023: Perform initial data analysis with project choice in mind to find more detailed research questions. Find appropriate dataset to measure success (I.e. ratings). Think about alternatives that do not require the use of GPT-3.5 for the binary questions. 

10/11/2023: Load IMDB ratings, discuss the output of the CMU personas paper code, split up work, define binary questions to query on for movie tropes 

14/11/2023: Combine individual work (preprocessing and initial statistics), flesh out new angle (focus only on romance movies) because the old ideas were not implementable. Assign personas to movie characters and analyze in which genres the different personas are present. 

**17/11/2023: Deadline Milestone P2**

24/11/2023: Perform analysis on the results of GPT-3.5 to the binary questions asked and link them to personas

**01/12/2023: Deadline Homework 2**

05/12/2023: Implement P2 feedback 

08/12/2023: Perform final analysis and draw conclusions and plan visualizations

12/12/2023: Write data story draft

15/12/2023: Finalize code and visualizations

19/12/2023: Proofread the datastory, notebook and Readme. Finish website.

**22/12/2023: Deadline Milestone P3**

### Organization within the team: (A list of internal milestones up until project Milestone P3)

| Team Member     | Tasks |
| ----------- | ----------- |
| Robinson   | Integrating IMBD dataset, run code from CMU personas paper, questions on romance tropes for GPT, GPT API binary search |
| Sophie   | Exploratory data analysis, data preprocessing, initial data analysis      |
| Eva | Exploratory data analysis, personas-genres assignment, statistics on ratings |
| Florence | Exploratory data analysis, questions on general tropes for GPT, personas-genres statistical measures|
| Laetitia | Exploratory data analysis, find datasets, team coordination, ReadMe |



### Questions for TAs 
- We ran the personas model on all movie summaries, we are wondering whether we should rerun it only on romance movies?
- Are there more appropriate statistical analysis that seem relevant for our questions?