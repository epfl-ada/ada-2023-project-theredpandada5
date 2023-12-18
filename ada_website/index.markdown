---
title: Romance movies, the recipe that goes straight to the heart
feature_text: |
  # Romance movies, the recipe that goes
  # straight to the heart
  ### or how to make a romance movie that people love
feature_image: assets/forest.jpg #"https://picsum.photos/1300/400?image=336"
excerpt: ""
---
SITE WEB TEST 2

Who doesn't love falling in love? Especially when you can do it over and over again, by following actors on screen? We all have seen romance movies, but the simple fact that two people fall in or out of love with each other does not equal a good quality story. And paradoxically, an unoriginal story can be exactly what we want to watch. Then what is it? Do we love them or hate them for being predictable? 

Hence, what if we could find magical ingredients that make a good romance movie? How many clichés are necessary, which archetypes, what recurring actions? Wouldn't you like to know? We do. So there it is, the story of romance movies, through their plots, persona and genres....
We begin by preprocessing the dataframe, augmenting it for project completion. Our focus then shifts to creating a regression model to predict the success of romantic movies, followed by an analysis of their evolution over time and in the context of the other genres of the movie.

<!-- ![Logo](assets/logo.png) -->
<p><div style="text-align: center; margin: 0px;">
  <img src="./assets/logo.png" style="width: 100px;" alt="Logo">
</div></p>

### ROMANCE, ROMANCE?
### or the preprocessing story
add something about usual preprocessing?

From the CMU dataset we have information on the movies themselves, some of their characters and the plot summaries. For this study, we focus on romantic movies as many movies independent of genre contain at least one romantic subplot. We can thus use movies containing romance in their genres. But is it enough?
It is then hard to analyze which movie really is about love, and which only contains a secondary love story.

The plot summaries might not contain all the necessary information about the plots to answer our most burning questions. Here is where the GPT-3.5 API comes to the rescue. Trained on more extensive summaries, it can answer questions about the plots in a more precise manner than an approximate word detection from the summaries. 
We were then able to generate questions about plot elements (such as "*Is there a best friend to lovers trope ?*" or "*Is there an empowered woman having regrets ?*") and obtain binary answers. Is GPT trustworthy? We let it explain the reasoning behind its answers for iconics movies such as Titanic. 

[plot ? Do we have results/proof to show? should we?]

Let's quickly mention Harry Potter here. It indeed contains a romantic subplot, but that does not make it a romance movie. The same applies for other movies such as Spirit. So although these movies are great, removing them for our analysis is probably a better choice. We considered movies sufficiently romantic for our analysys when they contained more than 3 positive answers to the 20 questions asked.
 Let's visualize the results of the proportion of answers, with 0 being a *no* answer and 1 a *yes* answer to the binary question.
<!-- interactive plot inserted directly in the html file -->
<iframe src="./assets/pie_charts.html" width="800" height="600"></iframe>

So we have tropes. What about the personas? What if we could extract from the summaries the common archetypes for the characters in the movies? For example, is there a best friend that has an inexistent life beside providing advice on the romantic life of the protagonist, or the emotionally unavailable character that hides a soft heart underneath many layers of deception and no apparent feelings. Let's get some help here. Extracting latent persona from the summaries, with the code from [Bamman, O'Connor and Smith, "Learning Latent Personas of Film Characters" (ACL 2013)](http://aclweb.org/anthology/P/P13/P13-1035.pdf), we therefore assign a persona type to characters. 
The technique is called Latent Dirichlet Allocation, LDA in short, which gives a probability distribution of the documents over the topics. This unsupervised technique allowed us to extract 20 persona and assign them to the characters, represented by persona types corresponding to the maximum of the vector of probabilities of persona types for each character. This vector is defined over 30 topics – words that cluster together – on agents, patients and modifiee. An *agent* is something the persona does, a *patient* is what is done to the persona, and a *modifiee* are adjectives associated with the persona. 

What stands out?

<iframe src="./assets/prop_characters_by_personas.html" width="800" height="600"></iframe>


### HOW MUCH DO YOU LOVE ME?
### or how to make a regression that (doesn't) work

Let's get back to the basics. How do you evaluate whether a movie is liked? Ratings, obviously! Or box office revenue... Which is missing in 80% of the movies. As the correlation between the ratings and the box office revenue is weak, we will focus on the ratings as a success indicator. Bingo, that's a measure of love... Isn't it? For romance movies anyways. Take the CMU dataset, add a pinch of IMDB ratings, and you get a dataset with 11'599 movies having romance in their genre and their ratings.
We are aware that users can only rate movies on IMDB only since 1990, but that might just get us a more modern perspective on the movies that came out before the 1990s. 

Overall, what makes specific romantic movies more liked by larger audiences? To answer this difficult question, there are several angles that we can take since there are multiple layers in a movie. The script contains specific plot elements that we can unwrap partly using the GPT 3.5 API. The characters, or specifically the character types, can also give us hints about what happens in a movie. Lets take for instance the presence of a heartthrob bad boy. Does that make us like the movies more? The “Learning Latent Personas of Film Characters” might help us answer that. Of course we have no information about the visual aspects or the actors performance etc. Are there any specific questions that significantly correlate with the ratings? Turns out, there are! Have a closer look to the *interrupted wedding*, *enemies  to lover*, *social status* and *serious illness* tropes. The confidence interval of the ratings when GPT's answer is yes or no is not overlapping. People do not seem to like interrupted weddings. Maybe it's too dramatic? Instead they seem to like impossible love due to social status. 
<!-- interactive plot inserted directly in the html file -->
<iframe src="./assets/average_rating_conf_int_questions.html" width="800" height="600"></iframe>

Everything is ready now to begin unraveling possible secrets!  


Regression doesn't seem to work that well. Maybe it is because the audience changes over time, and so does their taste? Let us have a look at the evolution of the ratings over time. 

### WHAT IF LOVE WAS ABOUT TIMING?
### or when to release a romance movie

We have seen that some movies are more liked than others, but what about the timing? Is there a specific time of the year when people are more likely to watch a romance movie? A specific year in which some trope or persona is more popular? If we plot the average positive answers over time, we can observe that besides before the years 1920 -- where there are not enough movies to have a significant average -- the average positive answers are quite stable over time. Interrupted weddings, despite being significantly correlated with lower ratings, is still the most common throughout time over time.

<!-- interactive plot inserted directly in the html file -->
<iframe src="./assets/average_answer_over_time.html" width="800" height="600"></iframe>

What about persona evolution? It seems like some persona are more stable over the years than other. 
The sudden drop in all persona around the year 2010 could be due to the dataset goes only to the year 2013.

<iframe src="./assets/personas_over_time_all_together.html" width="800" height="600"></iframe>

<!-- NOTE: removed the second plot because redundant with the first. I like being able to chose but it's good to have an overvew for all -->
<!-- <iframe src="./assets/personas_over_time_dropdown_menu.html" width="800" height="600"></iframe> -->

### WHAT IF LOVE WAS ABOUT THE OTHER GENRES?
### or in which context love flourishes

Movies can also be classified as romantic alongside other genres. 

### HOW CAN WE MAKE THE PERFECT ROMANCE MOVIE?
### or turns out, it's not that easy

We all know romance movies and their clichés. We like that they are what we expect. But maybe that's not all. Maybe it isn't enough to know the trope, the archetypes for the persona, the timing, the associated genres and even a combination of all of these.
Predicting the ending of a movie is easier than predicting its success. Even if we explain at best []% of the variance of the ratings, we can't explain it all. There may be no universal perfect love story. Everyone loves a different plot at a different time, and that's actually not so surprising.

<!-- However, our journey in rom-coms has not been unfruitful. -->
