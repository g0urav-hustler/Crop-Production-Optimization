
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
$ git clone https://github.com/g0urav-hustler/Crop-Production-Optimization.git
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
Now your setup has been completed, you can run this app by
```
python app.py
```
----------------------------
## Dockerization and Deployment
The app has deploy on heroku platform using a docker container.

Pre-requisite: Docker and Heroku intalled on your computer.

To install Docker, see [Reference](https://runnable.com/docker/getting-started/)

To install Heroku see [Reference](https://devcenter.heroku.com/articles/heroku-cli)

Docker command to build the docker container
```
$ docker build -t [your-app-name]:latest .
 ```
To run the docker container
``` 
$ docker run -p80:8000 [your-app-name]
```
To see docker container 
```
$ docker images
```
Login to your heroku account
```
$ heroku container:login
```
Create a web app on heroku
```
$ heroku create [your-app-name]
```
Tag your docker container as heroku web app
```
$ docker tag [your-app-name]:latest registry.heroku.com/[your-app-name]/web
```
Pushing the docker container on the web
```
$ docker push registry.heroku.com/[your-app-name]/web
```
Releasing the web app
```
$ heroku container:release web -a [your-app-name]
```

----------------------------
## Repository Overview
```
├── data
│   └──agricultural_data.csv
├── models
│   └──model.pkl
├── notebooks
│   └──Crops Prediction.ipynb
├── readme resources
│   └──web image.png
├── static 
│   └──style.css
├── templates
│   └── index.html
├── Dockerfile
├── README.md
├── app.py
└── requirements.txt
```

----------------------------
## License
MIT License

Copyright (c) 2021 Gourav Chouhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

----------------------------
### If you like this repo and it is useful, please don't forget to give a ⭐.