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
And then using the function that the Twython package provides for us to search the record within the criteria. It will return a dictionary which contains two queried results but what we need is 'statuses'.
![image](https://user-images.githubusercontent.com/90479627/134842984-07f4beef-ec49-4df0-aca4-e25436033f65.png)

