# Sentiment Analyzer
This sentiment analyzer can export the the feedback or recommendation you get in json file. Also, it can show the quantity and percentage of each type of sentiments which help users observe the result more clearly.

## 1.Import Flask and Initializing
In order to let users search the key word they wanna get information about, this analyzer imports the Flask module as one of the core modules.  
![image](https://user-images.githubusercontent.com/90479627/136678876-dcb1ad80-1063-4ad9-8baa-3ffdfb9b3f47.png)  
Then, initializing the home page and defining the search function in the page.
![image](https://user-images.githubusercontent.com/90479627/136678977-4d497246-4290-4b19-bf47-69f72a2255a7.png)
![image](https://user-images.githubusercontent.com/90479627/136679013-c72c5361-1ec3-4534-a4bc-eafece9169b4.png)

## 2.Searching Function
We can use the function defined in the twitter API module before. After we modify it and get the authentication, the retrieve_data function can be used normally.
So the user need to run the key.py to output their secret and token as json file for the puprose of working correctly later.  
![image](https://user-images.githubusercontent.com/90479627/136679203-6e9d8baf-ce16-46be-bbea-fcaf647bc937.png)

## 3.Export the feedback
After retrieving the recommendation or feedback, we can export them in json file in order for users to refer to the result easier.  
![image](https://user-images.githubusercontent.com/90479627/136679315-6c70831c-35c8-4899-8542-7d47182e21d5.png)
## 4.Sentiment analysis
As we did before, the feedback would be put in the Google NLP API and processed by sentiment analysis.  
By computing the result gotten from the sentiment analysis, we can count the number of people in each sentiment group and their percentages. It reflects the percentage of the people's sentiment towards the specific event. And such form of data is more intuitive and can also give users a better reference. The real-time result is shown below:  
![SRFB@Y%3 3_50 XGNW_IPSV](https://user-images.githubusercontent.com/90479627/135564784-b7b46a05-fe3b-4b71-b051-fd8692254c3c.png)

## 5.Visualization
When we finish the whole module, the home page will be as shown below:
![IES{P_YWR1V}QY 6BA4C8N6](https://user-images.githubusercontent.com/90479627/136681669-ab480c6c-c28a-4509-ba80-d3d8049d0284.png)  
And now users can input the key word like restaurant name or some specific products, it will give them the information they need.  
For example:
![image](https://user-images.githubusercontent.com/90479627/136684119-bc978074-e6e4-456d-9c38-1c7d23151b59.png)
