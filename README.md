# predictive Modeling Course - Statistical and data science foundations

## Intro
This course is designed to build foundations for predictive modeling. Many available resourses are either statistical/theoretical in nature or data science programming focused. After one has gone through learnings, some key questions remains:
1. how model is set up in real life use cases?
2. why a particular set up such as y=f(x) has predictive powers?
3. how to interpret predictive power metrics such as R-square, partial-R-square, KS, AUC, recall/precision, etc?
4. how to build/deploy?

In short, this course offers to close the gap between learnings and practicing. 

## chapter 1: set up
### Settting up vscode(local dev) /python / github(code repo)
tttt
### Building data set needed for modeling
tttt

## chapter 2: what's predictive modeling
### a. definition: find signal to some `future' outcome. Key is future.
tttt
### b. a time series example for a single entity such a stock ticker
tttt
### c. multiple time series (identical independent distributed entities) example
tttt
### d. what does the usual y=f(x) setup entail?
ttt
### e. t is everything: difference amongst y_t+1 = f(x_t) vs y_t =f(x_t) vs y_t = f_t(x_t) 
ttt
### f. causality vs statistical relationship. Only certain statistical relationship will be considered 'predictive'
ttt

## chapter 3: common predictive model setup --- gain intuition through penciled examples
### a. OLS
ttt
### b. simple regression
ttt
### c. logistic regression
ttt
### d. simple tree
ttt
### e. network 
ttt

## chapter 4: building models
### a. design x, y, splits (train, validation, test sets)
ttt
### b. feature engineering
ttt 
### c. feature selection
ttt
### d. model selection
ttt
### e. score cards and model objects
ttt

## chapter 5: evaluating model
### a. predictive power metrics
ttt
### b. cross time validation
ttt
### c. bias-variance tradeoff 
ttt
### d. underfitting/overfitting
ttt
### e. leaking
ttt

## chapter 6: deployment -- batch or near real time
### a. using score cards with database 
ttt
### b. using model object with python
ttt
### c. end point using sagemaker
ttt

## chapter 7: deep dive into some key issues on these predictive models
### a. skewed data in y
ttt
### b. skewed data in x
ttt
### c. boosting vs bootstrapping
ttt
### d. drifting and time travel
ttt
### e. incrementality or controlable model impact
ttt
### f. cicd 
