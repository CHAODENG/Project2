# Twitter APIs
By using a Python Library call twython which can access the Twitter APIs, we can analyze the popularity of the tweets at a certain time. 
Below is an example which extracts the information about user, date, specific text and its popularity about Boston celtics.
## 1. Autherization
The consumer key/secret is used to authenticate the app that is using the Twitter API, while the access token/secret authenticates the user.  For security, they should not be included in your code in plain text.  
So the first step we should do is to enter your api key, secret, access token and access access secret.
Entering all of the keys/secrets as strings and saving the credentials into a json file.
![image](https://user-images.githubusercontent.com/90479627/134840271-f628f7ad-b99a-4bde-af7d-35254b18cf12.png)  

## 2. Tool and Instantiation
In this step, we should import the library we need - json, twython, pandas. Then the credentials can be loaded from json file we exported in the previous step.
We can instantiate a object by using the key/secret record in the opening file.
![image](https://user-images.githubusercontent.com/90479627/134841218-50bf7cf8-423e-4fed-b00e-7201660ab2e8.png)  

## 3. Searching Information
After instantiation, declaring a query helps us aggreagte all the information we need in searching. For example, I want to search a key word 'Boston celtics', search type 'popular', count '30' and language 'English' in this case. So what I need to do is put them into a dictionary together.  
And then using the function that the Twython package provides for us to search the record within the searching conditions. It will return a dictionary which contains two queried results but what we need is 'statuses'.
![image](https://user-images.githubusercontent.com/90479627/134842984-07f4beef-ec49-4df0-aca4-e25436033f65.png)

## 4. Checking results
The last step is to save all datas and information in a pandas dataframe in order to manipulate it easier in a table. Below is what the information and datas we get from searching:
![image](https://user-images.githubusercontent.com/90479627/134843832-c1856a2e-ad4d-493c-a21e-49f84166e644.png)  
Then printing it into a table like this(the result was folder):  
![image](https://user-images.githubusercontent.com/90479627/134844086-3db2799c-d309-4c46-aa01-78740899fa78.png)

## Conclusion：
By using Twitter APIs to search the content I need, I get the userid information, date, popularity of content. In fact, the Twitter API is more powerful than its show up in this case. We can utilize it to do more searching about people's sentiment towards other specific ideas. And I hope I can explore more functions in future learnings.
