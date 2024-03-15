# Story 1: wrong target

When I did my first interview out of college with Capital one in 1999, the first exercise was to build a model to predict weather (whether it would rain). Granted the question was vague because it did not clearly specify prediting when. 
The data set was given as a few years worth of daily temperature, visibility, humidity, pressure, precipipation, wind. It looked something like this: 
```
date temp visib humidi pressure wind presp
1/1/1998 70 20 62 30 6 0.05
...
12/31/1999 65 40 75 31 10 0
```

So I quickly set up a regression model by defining y = (Presp>0) and the rest of columns other than date as X like following:
> X
```
temp visib humid pressure wind
70 20 62 30 6
...
65 40 75 31 10
```
> y
```
rain
1
...
0
```

After setting and fitting the model y~f(x), I can use hte model to predict whether it was raining for a given day. 

> However there was a major flaw!

I failed the exercise because there was no point of predicting current day's weather. It would be more practical to look out the window to see the weather. The model had no predictive power for future days' weather. For example, it would be more interesting to know tomorrow, the day after tomorrow and next week same day's weather. So it is obvious that a proper model set up (specially proper target) is super important for a model to be useful: good predictive power.

# Story 2: lack of practical and theoritical foundation
Once a collegue built a response model at a credit card company, the model was to find which prospect customer would be replying a snail mail solicitation. Data signals available were customers' credit bureau profiles such as fico score, payment history, line of credit, outstanding balance, inquries, etc. And we had some historical mail campaigns where a response label was available. Again, it was a superviced model exercise. 
A logistic model was built to give the propobality of a prospect customer's replying the the offer mail: p_t+1 = f(x_t). Note the timing of target and predictor. Feature will be used interchangebly with predictor. 
The model had really good performance metrics such as R-square, KS, AUC and recall/precision etc. (We will go over these terms in detail later.) R-squre of 90% was too good to be true in real life practices. When the model was presented, the immiediate response from client was that there was something wrong. The modeler was lacking of experience by simply relying on the model outcome. 
There is usually weak signal in data and a lot of noise in data. So real time R-squre of 30% or 40% was usual. Anything beyond 70% would be questionable. It turned out the model had leakage: some future was leaked back to history as signal. One of more of the features was highly correlated with p_t+1. It is common to define a target y in a wrong way to predict y_t+1 = f(y_t).
So beyond setting up the model properly, it is also super important to understand the model parameters and performance metrics in real life. 

# Story 3: missing reference t
Many times, there is a data set with features and target vaiable defined. For example, the kaggle data set creditcard.csv for fraud detection. it was chosen and built as a snapshot of history. 
In reality, data will have a different view and a reference time was needed to build that snapshot for modeling building. reference time (ref_t) or reference date (ref_d) are essential to understand how to validate model, build and deploy the models. 
For example, can a model using data as of January be applied in July? the answer is yes if there is no seaonality or model has treatment of seasonality. 
Another example, why can we use a model built on half of the sample and apply it to the other half? there is assumption of all entities in sample has identital independent distribution of some sort. In reality, this assumption is not true. As a result, ML and data science might approach the model fitting slightly differently. 

