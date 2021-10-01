# Google NLP
By using Google NLP, we can train the model to do sentiment analysis which reflects people's feeling towards the ideas containing the key word **'NBA'**.
Also, some tweets we have extracted from twitter using twitter API can be connected to Google NLP and help us be more familiar with NLP.  
## 1. Getting the Credential
Before building the project, we should visit the Google Cloud website to register for a new account. Then, we can training the model within the Google Cloud.  
We utilize the data extracted by Twitter API which we do practices in previous part. While we get authorization of the Twitter API, it still need us [get authentication](https://cloud.google.com/docs/authentication/getting-started#linux-or-macos) to Google NLP.  
![image](https://user-images.githubusercontent.com/90479627/135560251-d1222c82-dcb7-4619-9404-cbe165d255a4.png)
## 2. Installing the google.cloud AND Initialization
After getting the authentication to Google API, below is the syntax I used to initialize the API.
![image](https://user-images.githubusercontent.com/90479627/135560485-0dce09c0-3447-4536-b0fc-0d76892104a7.png)
![image](https://user-images.githubusercontent.com/90479627/135560668-59727c9f-5ba2-46dd-93e4-6d3093be9c1b.png)  
## 3. Processing on Twitter Data
The Twitter Data extracted from the phase(a) can be used in this phase(b).  
![}UHL09AH38T`JHSTT(Q{X8I](https://user-images.githubusercontent.com/90479627/135564605-480fe7c8-0dce-4bf0-aced-95ccc4718611.png)

We store the data in DataFrame format by using [panda package](https://pandas.pydata.org/).  
![image](https://user-images.githubusercontent.com/90479627/135562914-c19e7ef3-6092-4f28-833a-df401998a6bc.png)  

The next step we should do is to process the tweets like removing the special symbol within the text, switch all the uppercase to the lowercase, etc. In this case, we use [the re package](https://docs.python.org/3/library/re.html) in python. Some details can be referred in this link:https://docs.python.org/3/library/re.html.
![image](https://user-images.githubusercontent.com/90479627/135562995-c881370c-b0a4-41f9-b22c-bb1b9c86e3f8.png)
## 4. Doing the analysis
After the above steps have been done, we can use Google API and the result of training model in Cloud to do sentiment analysis. It will generate the score to reflect the people's sentiment.  
Therefore, the sentiment can be defined by the range of score. For example, I define the person who get the score between -0.5 and -1 is **Clearly Negative** or person who score from 0.5 to 1.0 is **Clearly Positive**.  
![image](https://user-images.githubusercontent.com/90479627/135563507-7d18b0f8-0bc8-421f-ae5a-41f4c1709cd8.png)  
Then,by computing the result gotten from the sentiment analysis, we can count the number of people in each group and their percentages. And the specific result is shown below:  
![SRFB@Y%3 3_50 XGNW_IPSV](https://user-images.githubusercontent.com/90479627/135564784-b7b46a05-fe3b-4b71-b051-fd8692254c3c.png)
 
## Conclusions
In this phase, we have the experience using Google NLP and data from Twitter API to do sentiment analysis. And I know how to build the project in Google Cloud and train my own model.  
In order to get deeper in Google NLP, I can do more practice that utilizing Twitter API to extract the data I need and connecting them with Google API to analyze the data within more situations. 
