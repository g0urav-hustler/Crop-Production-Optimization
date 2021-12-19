
<h1 align="center" ><img src ="static/logo.jpg" width = 30 height =30> Crop Production Optimization</h1>

**Website** : [Crop Production Optimization](https://crop-production-optimize.herokuapp.com/)
## Overview
#### It is a website which predict the best crop to be grown on the field under different soil and climatic conditions.

### Web View:
![](https://github.com/g0urav-hustler/Crop-Production-Optimization/blob/master/readme%20source/web%20image.png)

----------------------------
## Problem Statement 
For farmers, agriculture is their primary source of income. They grow crops in thier fields and sold it to markets for money. The more is the crop, more is the money and profit. 

But they don't know which crop has to grown in their fields according to it's soil properties and climatic condition like nitrogen and phosphorus value of soil, temperature,humidity in that region.

----------------------------
## Goal 
To make a Machine Learning model that predicts best crops to be grown under different soil and climatic condition.

----------------------------
## Technical Aspects

#### About the dataset
```
N - Nitrogen value in soil
P - Phosphorus value in soil
K - Potassium value in soil
Temperature - Local Temperature of that area
Humidity - Humidity in nature
Rainfall - Average rainfall in that region
Ph - Acidic value of the soil
Crops - Crop that has to be Grown.
```
#### About Model
- It uses Logistic Regression model
- Accuracy of the model is 96.36%

#### About App
- App build on Flask Framework
- Uses Html and Css for frontend UI

#### About Deployment
- Buid Docker Container
- Deploy Contaier to Heroku

----------------------------
## Setup and Intallation

Open your terminal and change the directory to project folder
```
$ cd [your-project-folder]
```
Clone the repo in your exiting project folder
```
$ git clone https://github.com/g0urav-hustler/Resumer-Name-Extractor.git
```
Making virual environment 
```
$ python3 -m [your-virtual-env-name] [project-directory-path]
```
Activate virtual environment 
```
$ source [your-virtual-env-name]/bin/activate
```
Install all the requirements
```
$ pip install -r requirements.txt
```
Now your setup has been completed to run the app.
