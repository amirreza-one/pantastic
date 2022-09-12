Question 1.  
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

Question 2.  
1. There are different types of Recommendation algorithm that we can use here:  
- Content-based.  
- Collaborative filtering.  
- Neural Network.    
2. Although a better and more sophisticated model for this use case is Neural Network approach for Recommendation System, the requirement that we need a reletively fast and memory efficient model makes us to choose a more simplistic approach. In this application a hybrid model of content-based filtering and collaborative filtering can be a good option, considering the fact that we have both user-items interactions, some features for users, and some features for items.  
3. Collaborative filtering:   
  -Pros:   it doesnt need domain knowledge, as a result there is no need for data engineering the features for items and users. Also it can capture more similarities between users and items with generating the latent layer, that may not be feasible for a human to engineer that, so the accuracy tends to be higher if we have enough amount of interaction.   
  -Cons:   As it is completely dependant on user interaction with the items, the cold start problem is more critical here for new users as well as new items. also it could be problematic when there is not a lot of interaction between users and items, i.e. the interaction matrix is sparse.
  Content Based:  
  -Pros:   It can handle better when we have a few interaction for a user or an item, i.e. with sparse interaction matrix.    
  -Cons:   Domain knowledge is required and features need to be entered manually, which may take a lot of effort.   
  Neural Network:  
  -Pros: we can have advantage of both Collaborative and Content based approaches, and it tends to have a better results.   
  -Cons: it is more complex and relatively slow both in train and prediction.
   
