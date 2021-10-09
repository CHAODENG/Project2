# Project2
## Goal：
1. Understanding definition of Modular. 
2. Understanding API concepts and protocols(This includes writing test programs for third party APIs). 
3. Implementing user stories using 3rd party APIs. 

## Schedule:
Phase 1:   
(a) Twitter APIs.   
(b) Google NLP.  
Phase 2:   
(a)Build your own social media analyzer.  

# Phase2:
## User Story
As a manager to run a shop which sells specific products, I can get the feedback of the customers by using the relative information we have retrieved. Then I can improve my service by designing some novel if most of the feedback is about the style of clothing or holding some promotional activities. So we can get more profit by improving customers' experience.    
  
As a traveler or a tourist, I can use such data that relevant to the restaurant around us to judge whether a specific restaurant is popular, which dishes is the favorite for most people in the menu, what is the average consumption of each restaurant. These information can help us determine which restaurant we should go today.

As a student, I can retrieve the course information and get to know which course I can register this semester is choosed by most students in previous semester. Also through the feedback we gain from other students, I can learn some experience and realize what course is more suitable for me.  
## Minimum Value Product:
This product is designed to help those who wanna get the feedback or sentiment analysis towards specific events like others' view on specific brands, people's evaluation for the store or coffee shop or students' thought about the professor and the course content. By using such sentiment analysis to get some recommendations, people can refer to those recommendations to make judgement and do some improvement based on the analysis.  

## Modular Design:
1. All users can first input a sentence or key word they want to search for to get feedback.  
  
2. Then the code should run the API to retrieve the tweets from the Twitter. After the data have been gotten, we can put those text into Google NLP to do sentiment analysis. By doing such analysis, we output the percentage of people' sentiment towards specific events.

3. Thus, by concluding the result, we can get the choices that people are more inclined to. And multiple choices or recommendations will be shown for the users.  

4. For those recommendations, people can re-search the key word to ensure whether it has been selected by most of people and gets nice feedback.

5. After the final search, the people can narrow the selection to one or two and determine what they will choose to do.
