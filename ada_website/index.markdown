---
title: Romance movies, the recipe that goes straight to the heart
feature_text: |
  # Romance movies, the recipe that goes
  # straight to the heart
  ### or how to make a romance movie that people love
feature_image: assets/forest.jpg #"https://picsum.photos/1300/400?image=336"
excerpt: ""
---

Who doesn't love falling in love? Especially when you can do it over and over again, by following actors on screen? But if everyone watches romantic movies, it is common knowledge that they are not all equals in terms of quality and plot. We love them for it, we hate them for it. 

But what if we could find magical ingredients that makes a good romance movie? How many clichés, which archetypes, what recurring actions? Wouldn't you like to know? Because we do, and here's in consecutive parts the story of romance movies.... 
Starting with [steps]

<!-- ![Logo](assets/logo.png) -->
<!-- <p><div style="text-align: center; margin: 0px;">
  <img src="./assets/logo.png" style="width: 300px;" alt="Logo">
</div></p> -->

## ROMANCE, ROMANCE?
### or the preprocessing story

From the CMU dataset we have information on the movies themselves, some of their characters and the plot summaries. For this study, we focus on romantic movies as many movies independent of genre contain at least one romantic subplot. We can thus use movies containing romance in their genres. But is it enough?
It is then hard to analyse which movie really is about love, and which only contains a masochist hero that somehow gets a girl by the end of it. 

That's where the GPT-3.5 API comes in! Using queries, we ask binary questions about the plot elements (such as "Is there a best friend to lovers trope ?" or "Is there an empowered woman having regrets ?"), tested on some famous movies such as Titanic to evaluate the performance of the model. These binary questions are then used to discard movies classified within the genre "Romance", but that do not have more than 3 positive answers to the 20 questions asked. Let's visualize the results of the proportion of answers, with O being false, 1 being true and 2 being NaN.

<!-- interactive plot inserted directly in the html file -->
<!-- <iframe src="./assets/pie_charts.html" width="800" height="600"></iframe> -->

So we have tropes. What about the personas? Let's get some help here. Extractig latent persona from the summaries, with the code from [Bamman, O'Connor and Smith, "Learning Latent Personas of Film Characters" (ACL 2013)](http://aclweb.org/anthology/P/P13/P13-1035.pdf), we therefore assign a persona type to characters. What stands out? 

[plot?]


## HOW MUCH DO YOU LOVE ME?
### or how to make a regression that (doesn't) work

Let's get back to the basics. How do you evaluate if a movie is good? Ratings, obviously! Or box office revenue... Which is missing in 80% of the movies. As the correlation between the ratings and the box office revenue is weak, we will focus on the ratings as success indicator. Take the CMU dataset, add a pinch of IMDB ratings, and you get a dataset with 11'599 movies having romance in their genre and their ratings.
Users can rate movies on IMDB only since 1990, we therefore get a more modern perspective on the older movies. Bingo, that's a measure of love... Isn't it? For love movies anyways. 

Overall, what makes specific romantic movies more liked by larger audiences? To answer this difficult question, let's use GPT-3.5 API answers about plot elements and "Learning Latent Personas of Film Characters". Everything is ready to analyze the ratings of romantic movies, as well as movies with some popular genres paired up with romance, over time!

So, let's get back to ratings analysis. 


## WHAT IF LOVE WAS ABOUT TIMING?
### or when to release a romance movie

We have seen that some movies are more liked than others, but what about the timing? Is there a specific time of the year when people are more likely to watch a romance movie?


## 
### 

