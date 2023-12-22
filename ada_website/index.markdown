---
title: Romance movies, the recipe that goes straight to the heart
feature_text:  |
  # <span style="color: #BDC8CC;"> Romance movies, the recipe that goes <span>
  # <span style="color: #BDC8CC;"> straight to the heart <span>
  ### <span style="color: #BDC8CC;"> or how to make a romance movie that people love <span>
feature_image: assets/forest.jpg #"https://picsum.photos/1300/400?image=336"
excerpt: ""
---

Who doesn't love falling in love? Especially when you can do it over and over again, by following actors on screen? We all have seen romance movies, but the simple fact that two people fall in or out of love with each other does not equal a good quality story. Paradoxically, an unoriginal story can be exactly what we want to watch. But then, what is it? Do we love these movies or do we hate them for being predictable?

Let's get back to the basics. How do you evaluate whether a movie is liked? Obviously, box office revenue… which, in the CMU dataset, is missing for 80% of the movies. Also, using box office revenue as a metric for quality is quite biased: usually when big studios release movies, a lot of people go watch them in theaters, whether they are good or not. A much better quality metric is people’s ratings! Bingo, that's a measure of love... Isn't it? For romance movies anyways. 

Take the CMU dataset, add a pinch of IMDB ratings, and you get a dataset with around 8000 romance classified movies, along with their ratings.
We are aware that users can only rate movies on IMDB only since 1990, but that might just get us a more modern perspective on the movies that came out before the 1990s.  

With all this data, what if we could find magical ingredients that make a good romance movie? How many clichés are necessary, which archetypes make us watch, what recurring actions get us excited to finish the movie? Wouldn't you like to know? We do! Follow us along, while we try to uncover the secrets to romance by analyzing the plots and the personas individually and as a beautiful blend. 

<p><div style="text-align: center; margin: 0px;">
  <img src="./assets/logo.png" style="width: 100px;" alt="Logo">
</div></p>

#### ROMANCE, ROMANCE?
###### or the preprocessing story

CMU dataset contains information on the movies themselves, some of their characters and the plot summaries. For this study, as mentioned before, we focus on romantic movies as many movies, independent of genre, contain at least one romantic subplot. We can thus use movies containing romance in their genres. But is it enough?

Love is in the air for most movies, this is why we try to discriminate between movies containing romance, and romance movies.

The plot summaries might not contain all the necessary information about the story to answer our most burning questions. Here is where the GPT-3.5 API comes to the rescue! GPT was trained on a lot of Internet data. This likely includes valuable information about movies from our dataset. Let’s take advantage of this instead of using an approximate word detection from the summaries. 
We asked GPT boolean questions about plot elements (such as "*Is there a best friend to lovers trope?*" or "*Is there an empowered woman having regrets?*") to characterize the movies.

Is GPT trustworthy? Mostly yes, but let’s examine a concrete example.
In the romance domain, there are quite a lot of tropes that are used over and over again. For some of them, GPT3.5 simply could not answer because they were too ambiguous. We thus had to try and create questions that could be answered without having to “understand” the whole movie. But just like situationships, even the all-knowing GPT3.5 could not decide correctly. Sometimes we would disagree with GPTs answers, but then the justifications made sense?
 
For instance, let's take one of the greatest romance movies: *The Notebook*. It could contain lots of different tropes: enemies to lovers, a grand reunion, and a sad ending. But the enemies to lovers in this movie was one sided as the male protagonist Noah was immediately infatuated with Allie. From his perspective it was love at first sight, therefore answering yes or no to either question could be considered correct. 

Remember when we said that we want to differentiate between romantic subplots and romance as a protagonist? Well, let's talk about *Harry Potter*. It indeed contains a romantic subplot, but that does not make it a romance movie. In general, movies such as Harry Potter, Pirates of the Caribbeans, or Spirit, are marked by GPT as containing no romance cliché at all. For our analysis, we thus only consider movies with at least 1 positive answer over the 20 questions.

 Let's visualize the results of the proportion of answers, with 0 being a *no* answer and 1 a *yes* answer to the binary question.
<!-- interactive plot inserted directly in the html file -->
<iframe src="./assets/pie_charts.html" width="800" height="600"></iframe>

Now that we have the tropes, let’s see whether we can find personas!  What if we could extract the common archetypes for the characters in the movies from the summaries? For example, is there a best friend with no purpose beside providing advice on the romantic life of the protagonist? What about the emotionally unavailable character, hiding a soft heart underneath many layers of deception?
Let's get some help here. Luckily, this has been done in [Bamman, O'Connor and Smith, "Learning Latent Personas of Film Characters" (ACL 2013)](http://aclweb.org/anthology/P/P13/P13-1035.pdf).

The technique is called Latent Dirichlet Allocation, or LDA in short. This is a common unsupervised learning technique used over text data. In essence, its task is to extract the most important "topics" over a corpus. Topics can thus be represented as distributions over the vocabulary. The technique is again applied on the topics, yielding "personas", ie. distributions over the topics! The topics, which were classified with chat GPT and our imagination, are presented in the table below. 

| Topic    |   Theme                                 |   Words                                             |
|-------|---------------------------------------|---------------------------------------------------|
| 0     | Mystery Drama                        | son, able, dead, detective, director, alive, former, agent, suspicious, about |
| 1     | Communication and Relationships      | tell, love, see, ask, give, meet, confront, invite, call, talk |
| 2     | Supernatural Adventure               | child, judge, fiancé, pirate, soul, human, spirit, teenager, waitress |
| 3     | Family Dynamics                      | mother, wife, son, baby, aunt, grandmother, president, single, pregnant, dead |
| 4     | Identity and Diversity               | man, young, boss, old, soldier, other, guest, gay, angel, client |
| 5     | Action and Investigation             | kill, tell, save, find, arrest, name, bring, force, warn, release |
| 6     | Emotional Relationships              | tell, go, ask, say, love, want, give, get, come, walk |
| 7     | Life Choices and Actions             | leave, take, see, be, find, run, have, know, make, look |
| 8     | Relationship Milestones              | get, make, break, introduce, go, propose, end, spend, sleep, pick |
| 9     | Giving and Receiving                 | give, take, reveal, show, convince, offer, help, inform, keep, hire |
| 10    | Life's Crossroads                    | die, give, want, come, refuse, leave, suffer, make, commit, welcome |
| 11    | Emotions and States                  | that, pregnant, one, angry, unable, happy, able, about |
| 12    | Family Members                       | husband, brother, kid, grandfather, younger, priest, twin, artist, older |
| 13    | Romantic Connections                 | marry, meet, fall, attract, send, name, engage, involve, reunite, find |
| 14    | Decisions and Actions                | tell, have, try, arrive, offer, invite, send, arrange, believe, ask |
| 15    | Family Business Drama                | father, parent, maya, phane, villa, own, late, dead, conservative, businessman |
| 16    | Struggle and Fight                   | capture, kill, send, take, rescue, lead, defeat, attack, return, free |
| 17    | Life Changes                         | have, live, visit, raise, name, care, leave, kill, move, reconcile |
| 18    | Artistic Pursuits                    | perform, play, sing, arrive, offer, conclude, quit, win, confide, dance |
| 19    | Social Roles                         | officer, uncle, owner, police, lady, bride, servant, new, vampire |
| 20    | School Life and Relationships        | friend, student, best, boyfriend, old, school, teacher, girlfriend, character, high |
| 21    | Love and Relationships               | marry, love, fall, leave, arrange, write, visit, propose, reject, inform |
| 22    | Discovery and Revelation             | find, try, fall, manage, arrive, discover, attempt, refuse, die, learn |
| 23    | Diverse Female Characters            | woman, daughter, young, beautiful, girl, lover, neighbor, cousin, wife, wealthy |
| 24    | Diverse Male Characters              | boy, doctor, princess, worker, dad, villager, young, stranger, gay, Christian |
| 25    | Life's Journeys                      | have, meet, decide, be, try, begin, want, find, realize, get |
| 26    | Criminal Activities                  | kill, shoot, confront, steal, beat, inform, drive, escape, attack, send |
| 27    | Royal Intrigue                       | king, de, son, captain, soldier, guard, master, prince, thug, dead |
| 28    | Historical Context                   | girl, sister, king, prostitute, little, musketeer, diner, older, native, younger |
| 29    | Life's Movements                     | go, meet, return, come, live, arrive, join, stay, work, visit |

We also make a distinction between agents, patients and modifiee : an *agent* is something the persona does, a *patient* is what is done to the persona, and a *modifiee* are adjectives associated with the persona. For example, if we look at the most common topics in the agents of the personas, we can see that "Life's crossroads" is very rarely used among all 20 personas. In contrast, a lot of personas seem to be greatly characterized by “Life’s journeys” topics!

To give a better idea, we provide an example of agents distributions over the most common topics.
<iframe src="./assets/topic_distrib_agents.html" width="800" height="600"></iframe>

A more concrete exemple, would be persona 12.
- The common agents are *tell, ask, love, give, meet*. 
- The common patients are *tell, love, call, talk, ask*
- The common modifiees are *best, friend, student*. 

This persona, with a bit of imagination, could be described as the **Talkative Best Friend**. Compared to other personas, they do not endure life-changing topics in any of their appearances. Nonetheless, they are important as they help the main protagonist succeed in their love life!

We can try and see which personas appear the most among the different characters.

<iframe src="./assets/prop_characters_by_personas.html" width="800" height="600"></iframe>

What stands out? It appears that the most common characters are 12 and 8. The least common character is 9. Only a few characters are well represented overall. 80% of the characters are associated with a persona within {2, 4, 8, 12, 15, 19}.


Now that we know the common personas, we can, with the methodology used for the **Talkative Best Friend**, assign a type to the most used personas, as you can see in the table below.

| Persona | Representation | Agents | Patients | Modifiee |
|---------|--------------------------|-------------------------------------|------------------------------------|--------------------------------------|
| 2       | Adventurer    | 7, 22, 25, 6 | 5, 9, 26, 1 | 0, 11, 20, 4 |
| 4       | Drama Woman             | 22, 25, 21, 29 | 13, 21, 9, 1 | 11, 23, 0, 20 |
| 8       | Attractive Newcomer  | 25, 7, 22, 29 | 9, 13, 8, 1 | 11, 0, 23, 20 |
| 12      | Talkative Best Friend        | 6, 25, 7, 29 | 1, 7, 8, 13 | 11, 20, 23, 0 |
| 13      | Woman Detective   | 29, 22, 25, 7 | 5, 9, 7, 13 | 23, 11, 0, 20 |
| 15      | Engaged Heart  | 25, 7, 6, 29 | 13, 7, 1, 9 | 23, 11, 0, 20 |
| 19      | Action Hero   | 22, 16, 7, 29 | 5, 16, 9, 29 | 27, 0, 11, 4 |



#### TIME PASSES, BUT LOVE STAYS FOREVER
###### or the impact of time on romance movies

Audiences change  over time, and so does their taste. Let us have a look at the evolution of the plots and persona over time. Is there a specific year in which some tropes or personas  are more popular? If we plot the average positive answers over time, we can observe that besides before the years 1930 -- where there are not enough movies to have a significant average -- the average positive answers are quite stable over time. Interrupted weddings, despite being significantly correlated with lower ratings, is still the most common trope throughout time.

<!-- interactive plot inserted directly in the html file -->
<iframe src="./assets/average_answer_over_time.html" width="800" height="600"></iframe>

What about the personas  evolution? The following plot illustrates the distribution of the most common persona over time, from the year 1930 as prior to that year the movies are not numerous enough for relevant statistics. We choose the six most common personas, {2, 4, 8, 12, 15, 19}, which represent roughly  80% of the characters. Note how some tendencies revert: persona 2 which was predominant in the 40s-50s seems to leave more space to persona 12 over time. Is this a hint at WWII? Note how persona 2 is associated with a need for mystery drama, discovery and criminal activities.

<iframe src="./assets/common_personas_over_time_normalize.html" width="800" height="600"></iframe>


#### HOW MUCH DO YOU LOVE ME?
###### or how to predict the ratings (or not)

Overall, what makes specific romantic movies more liked by larger audiences? To answer this difficult question, there are several angles that we can take. We choose to describe a movie through  a combination of plot elements and personas.

The script contains specific plot elements that we can partly unwrap using the questions fed to GPT3.5.  The characters, or specifically the character types, can also give us hints about what happens in a movie. Lets take for instance the presence of a heartthrob bad boy. Does that make us like the movies more? 
Of course, we have no information about the visual aspects or the actors' performance. But it still might be that some specific personas or clichés have a significant importance on the ratings. 

Turns out, there are! Have a closer look at the *interrupted wedding*, *enemies to lover*, *social status* and *serious illness* tropes. The confidence interval of the ratings when GPT's answer is yes or no is non-overlapping. People do not seem to like interrupted weddings. Maybe it's too dramatic? Or perhaps there’s another reason, since they seem to like impossible romance due to social status, and Romeo and Juliet are proof that it can be just as dramatic!

<iframe src="./assets/average_rating_conf_int_questions.html" width="800" height="600"></iframe>

Similarly, we can compute these averages for the personas : 
<iframe src="./assets/ratings_conf_int_personas.html" width="800" height="600"></iframe>

However, is it everything? No! Recall the main antagonist of ADA, the *mean monkey*. If we learned one thing in the course, it certainly is not to trust averages. We can now dive deeper into the data.

Let’s start unraveling! What is the influence of tropes on the ratings? What about the personas present in the movies? And what about the two of them as a couple (wink)? A linear model might do the trick. Starting with a simple model, we include only the movie revenue, runtime, number of votes and release date. The results are tragic, a weak score of R<span class="superscript">2</span> score of 26.4%.  When we include our tropes results (GPT), it’s even worse. We overfit.  Not even a random forest can help. No simple model seems to be enough to explain love based on our questions! So predicting  the rating based on the trope is an unreachable dream…

| Model                | R<span class="superscript">2</span>   |
|----------------------|-------|
| Simple model         | 0.264 |
| Questions only       | 0.027 |
| Personas only      | 0.05 |
| Personas + simple model       | 0.213 |
| Personas + questions | 0.063 |
| Personas + questions + simple model | 0.249 |

As a take home message, the explained variance is not very high. Good news, we are not robots and do not just rate movies according to some flow diagram! There are probably a lot of factors other than the personas present in a movie and whether or not 20 selected tropes are present that determine whether we like movies or not, like the actors, the filming, the music and countless others.

However, the following variables were significant at the 5% level:   
- The **number of votes**, positively correlated with the rating.
- **Questions 0, 3, 18**, with respectively a negative, positive and positive correlation (although low for each question).
- The **release date** of the movie, which negatively correlates with the ratings.
- The **runtime** of the movie, also positively correlated with the rating.
- **Persona 4, 8, 12, 13** with respectively positive, negative, negative and positive correlation (although low for each persona).

We can at least draw one conclusion from this: the number of votes seems to significantly explain some variance in the ratings. For instance, as the following plot shows, movies with weddings stopped at the altar have a considerably lower number of votes, and they also have a lower score… That may be a problem! Or not? 

<iframe src="./assets/nb_votes_conf_int_questions.html" width="800" height="600"></iframe>


#### AND THAT’S A MATCH
###### or how to reduce the impact of observed covariates

We have previously observed some statistically significant correlations. However, this remains an observational study, and movies have many confounders and a lot of variance. In order to get some conclusions out of this study, we are gonna make movies fall in love with their matches, following the principle of “*what belongs together comes together*”.

What kind of confounders are we looking at? The tropes can influence each other. Also, as seen in the previous regression, the number of votes is positively correlated with the rating.
To reduce these confounders, let's marry off our movies based on their most relevant clichés. To ensure ultimate happiness in their couplings, we also match them approximately on their respective number of votes. 

Stopping a wedding and creating a heartthrob romance movie do not mingle well. The ratings are significantly worse (p-value of **0.0001**!). As for the other tropes, you might be more free to choose. The coefficients in the table indicate the impact of the trope on the rating, its value being by how much the average rating increases or decreases when the condition is present or not.
We can observe that seven clichés actually influence our opinion on romance movies statistically (at a 95% CI-level)! (Although let’s not get ahead of ourselves, the coefficients are low for all  of them)

| Question | Question Theme | Number of Pairs | SMD Votes | SMD Year | Coefficient | P-Value|
|----------|----------------------------------|--------------|-----------|----------|-------------|-----------|
| 0        |Interrupted wedding          | 1852         | 0.0093    | 0.0033   | -0.1198     | 0.0001    |
| 2        | Enemies to lovers                | 1194         | 0.0691    | 0.2486   | -0.0826     | 0.0241    |
| 3        | Social status                    | 1237         | 0.0923    | 0.0572   | 0.0986      | 0.0063    |
| 6        | Meet-cute                        | 1674         | 0.1094    | 0.0442   | 0.0736      | 0.0189    |
| 15       | Fake dating		 | 639          | 0.0569    | 0.0668   | 0.1324      | 0.0088    |
| 18       | Regretful empowered woman | 1512         | 0.0198    | 0.0612   | 0.1356 | 0.0 |
| 19       | Reunion                          | 1092         | 0.065     | 0.0119   | 0.0814      | 0.0321    |

Maybe our love language is not acts of service or giving presents but rather spending quality time with our favorite characters? We can use the same methodology as before, but now on the personas. 
Recall the previous plot : it seemed like some personas actually have an impact on the ratings, right?

Let’s make sure of it! With the same methods used on the clichés, we this time test the effect of presence for each persona by matching on the most common personas.

As shown in the plot below, we can observe that some personas do have a causal impact on the ratings! The “woman detectives” would on average increase the overall rating of the movie. Better luck next time to the “Attractive Newcomer”! It is also interesting that people would prefer the drama queen, as it’s a rather standard archetype.

| Persona | Persona Name| Number of Pairs| SMD Votes | SMD Year | Coefficient | P-Value |
|-----------|--------------------------------|--------------|-----------|----------|-------------|-----------|
| 4 | Drama Woman |279          | 0.0725    | 0.2533   | 0.3168      | 0.0       |
| 8 | Attractive Newcomer |911          | 0.0323    | 0.1427   | -0.1613     | 0.0001    |
| 12 | Talkative Best Friend |1004         | 0.0726    | 0.1575   | -0.1672     | 0.0001    |
| 13 | Detective Woman |148          | 0.0511    | 0.134    | 0.3182      | 0.0027    |

One could wonder: why not try a matched study on both personas and genres? This could maybe lead to new incredible findings! Well, it turns out to give the exact same results. The same personas and the same questions remain relevant. So, for the sake of conciseness, we omit this table! 


#### MIRROR, MIRROR ON THE WALL, WHO IS THE MOST ACCURATE OF ALL?
###### or why using GPT 3.5 may be a bad idea

By considering ethics in our project, we aim to highlight ethical dilemmas and recognize the limitations, implications, and biases in our use of data. Love might not conquer all after all! First, considering the fairness of our study, we can critique film databases, emphasizing flaws such as sexism and a lack of ethnic diversity. Sexism can be explained by the fact that most producers, writers, cinematographers, and editors are men, leading to sometimes caricatural representations of women. Similarly, the lack of diversity results in an overrepresentation of western and white individuals. This correlation is evident not only on screen but also among those who participate in the film evaluation process through voting. In the article "Gender, writing and ranking in review forums: a case study of the IMDb" (Otterbacher, 2013), significant gender-based differences in critics' activity become apparent. Male critics show a stronger involvement compared to their female counterparts (with an average five times higher for men), and male comments are more appreciated by users. IMDb thus appears as a platform demonstrating a distinctly masculine orientation. 

A second critical point in our data concerns the use of GPT. GPT provided us with results of highly variable quality for the films we were able to verify. A significant portion of the responses is indeed subject for debate because some movies focus on multiple love stories or only have romance as a subplot. Some responses are not necessarily incorrect but simply up for debate. The answers are allowed only to consist of yes or no, instead some responses are context dependent.  Thus, our answers may be considered inconsistent and unreliable for drawing real conclusions. An additional point to add to our ethical considerations is that our GPT-based responses required the use of servers and thus the consumption of resources. The last point is that since our project is about movies, if we were to keep up with more recent data (the data collection was stopped in 2012), it would pose a sustainability issue as the dataset and research would constantly need to be updated.


#### HOW CAN WE MAKE THE PERFECT ROMANCE MOVIE?
###### or turns out, it's not that easy

We all know romance movies and their clichés. We like them to be what we expect, but maybe not always. Maybe it isn't enough to know the tropes, the archetypes for the personas, the timing, the associated genres…

Predicting the ending of a movie is easier than predicting its success! Even if we explain at best 26% of the variance of the ratings, we can't explain it all. Maybe the last bit is explained by magic or maybe there is simply  no universal perfect love story. Everyone loves a different plot at a different time, and that's not  actually so surprising! People and their tastes are difficult to anticipate, and that doesn’t mean that what we’ve found is unfruitful!

As for the results, a small summary seems necessary : 
- Love triangles and weddings stopped at the altar tend to annoy the audience. They are very common, and perhaps became boring? 
- The audience seems to really enjoy impossible romances. Is it because of fate? Do we take pleasure in seeing lovers torn apart by this cruel world?
- The classic Drama Woman persona is positively correlated with the ratings. We surely all enjoy seeing a drama queen fall in love! 
- The Attractive Newcomer persona has a bad influence on the ratings. Maybe is it an incentive to never move out? 
- The Talkative Bestfriend persona also tends to be bad for the movies. And for sure, we all hate this annoying and awkward friend that often breaks the romance with their unfunny jokes.
- The Woman Detective persona has a lot of success! Who would object? We love gruesome murders and we love intense romance. What could possibly go wrong when mixing these two?

Do not forget that these are only small findings. They might influence slightly how much we like a romance movie, but none of our factors ended up being a huge impacting factor (at best a +0.3 difference in ratings). Maybe you would like to find out further why that is? 
We have a new suspect: people pleasing in the votes. Is our opinion scaled on that of others? 

