## Predict the Game Rating

### Description

Exploring the BoardGameGeek dataset from Kaggle and predicting the rating of the game.

Link to the dataset : https://www.kaggle.com/jvanelteren/boardgamegeek-reviews#2019-05-02.csv.</br>

### Prerequisites

1.  Installing Python 3
2.  Installing pip 3
3.  Installing the required python libraries using pip
4.  Install Jupyter Notebook

### Implementation

1.  Analyzing the data.
2.  Cleaning the data.
      * Removing non alpha-numeric characters.
      * Removing empty rows.
3.  Sampling the data for train and test.
4.  Training the model.
      * Vectorizing the data - TFIDF, hyperparameter tuning max_features.
      * Training the model.
5.  Testing the model.
6.  Comparing Classification vs Regression results.
7.  Building the final model with the best feature count.
8.  Displaying a sample result

### Executing Files

1.  Download the notebook from this repository.
2.  Launch the notebook on Jupyter.
3.  Execute the notebook. All the cells will be executed in the sequence of their definiton.

### Demo Video

https://youtu.be/5jMqRtH3BtA

### Improvements and Contribution

This implementation includes sampling from a large dataset and then training a model to predict rating, given the review. Training data has been vectorized using varying max_features as a criteria (hyperparameter) which is a new thing implemented.

The existing implementations only implement classifiers. Comparison the performance of a Regressor and Classifiers for predicting the rating has been done in this implementation.

Instead of counting accuracy as a parameter, RMSE has been used to compare model performances. Accuracies did not tell much about the performance model and it was almost similar for the three models.

From the implementation it was observed that the Linear SVR performed better than the Multinomial Naive Bayes Classifier and Linear SVC. SVR and SVC are both support vector machines but SVC was much slower than the SVC.

### Challenges

Analyzing the dataset to decide which parameters to use to predict the rating was an important decision made.

Reading a large data set was one of the challenges which was overcome by using random sampling. 10% of the cleaned and processed dataset was used for training the models.

There were about 3000+ distinct values for rating. Rounding the rating to multiples of 0.5 for Regressor and nearest integer for Classifier was done to overcome this challenge.

Picking a metric to measure the performance of the models was another challenge since the accuracy for almost same for all models and it was quiet low. It was observed that RMSE was a better metric to measure performance of the model than Accuray, since accuracy takes into considering the exactness which is not the case in RMSE.

### References

https://www.codementor.io/@guidotournois/4-strategies-to-deal-with-large-datasets-using-pandas-qdw3an95k for picking random sample from training data

https://stackoverflow.com/questions/24838629/round-off-float-to-nearest-0-5-in-python for rounding rating

https://stackoverflow.com/questions/47917943/how-to-select-several-rows-when-reading-a-csv-file-using-pandas for skipping rows while reading from a csv

https://stackoverflow.com/questions/29523254/python-remove-stop-words-from-pandas-dataframe for removing stopwords

https://www.developintelligence.com/blog/2017/03/predicting-yelp-star-ratings-review-text-python/ as a reference

https://towardsdatascience.com/review-rating-prediction-a-combined-approach-538c617c495c as a reference
