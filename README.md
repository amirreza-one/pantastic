## Question 1.  
Please check answer.py file.  
This function encrypt the input text. Here are some example of outputs:

```
Input : lookadistraction
Output : latt odri oiao kscn
---------
Input : bananaerror
Output : bnr aao ner ar
---------
Input : chillout
Output : clu hlt io
---------
```

## Question 2.  
**What kind of algorithms would you explore to solve this issue?**

There are different types of Recommendation algorithm that we can use here:  
- Content-based.  
- Collaborative filtering.  
- Neural Network.    

---
**What is your preferred model?**
Although a better and more sophisticated model for this use case is Neural Network approach for Recommendation System, the requirement that we need a reletively fast and memory efficient model makes us to choose a more simplistic approach. In this application a hybrid model of content-based filtering and collaborative filtering can be a good option, considering the fact that we have both user-items interactions, some features for users, and some features for items.  

---
**How would you compare different models, and why? Explain the pros and cons of each of these models.**

  _Collaborative filtering:_   
  - Pros:   it doesnt need domain knowledge, as a result there is no need for data engineering the features for items and users. Also it can capture more similarities between users and items with generating the latent layer, that may not be feasible for a human to engineer that, so the accuracy tends to be higher if we have enough amount of interaction.   
  - Cons:   As it is completely dependant on user interaction with the items, the cold start problem is more critical here for new users as well as new items. also it could be problematic when there is not a lot of interaction between users and items, i.e. the interaction matrix is sparse.   
  
  _Content Based:_  
  - Pros:   It can handle better when we have a few interaction for a user or an item, i.e. with sparse interaction matrix.    
  - Cons:   Domain knowledge is required and features need to be entered manually, which may take a lot of effort.   
  
  _Neural Network:_  
  - Pros: we can have advantage of both Collaborative and Content based approaches, and it tends to have a better results.   
  - Cons: it is more complex and relatively slow both in train and prediction.
   
   
---
**What are the steps/techniques you use to make sure that you are not over-fitting your model?**
   - Similar to every other ML problem, with CrossValidation and using L2 Regularization we will be able to control overfitting.  
   
**What techniques would you use to detect outliers?**
   - For removing outliers, like any other ML problem we can remove those interactions which are more than 2 or 3 times of standard deviation from mean. for example if the mean of purchasing an item is 2 times with standard deviation of 1 then maybe we need to put an upper bound of purchasing 5 = 2 + 3 x 1  times. So who every has purchased this item more than 5 times will be replaced with 5.   
   
**How would you solve the cold start problem? (i.e., how would you update the algorithm so it not only can make recommendations to the existing users in the recommender, but also to new users that have no prior activities)**
   - To solve Cold Start problem there are several things we can do:  For new user who hasnt much interaction yet we can show him a combination of most popular items and some random items to collect data from his interactions. For a new item, we can randomly show it to a group of users to collect data, also a better way could be to use a content-based recommendation system to show this item to users who liked similar items.


---
**How can we train a model which incorporates both the ratings and the Shoppers and Products attributes (age, gender, location for shoppers, type, size, color for products)? Describe your technique.**

There are two approaches that we can take.
1. we can feed both interaction and features in a neural network to predict the probability of having interaction.
2. we can design a hierarchical model in a way that for those items which doesnt have enough interaction, based on features similarities we recommend it to users who had interaction with similar items. Also for new user who doesnt have interaction, based on feature similarities of buyers we provide those items that similar users like.
otherwise if the item or the user has enough interaction we use the collaborative filtering approach which recommends just based on interactions.
