# Clickbait

Clickbait is a project where I will recommend trending YouTube videos to a user. I plan to use a bit of NLP to play around with content-based recommenders, microservices, Docker, and CI/CD.

## Technology Overview

It utilizes the following technologies:

-   Web
    -   VueJS
    -   NuxtJS
-   Recommender
    -   Python
    -   Flask
    -   SciKit Learn
-   User
    -   TypeScript
    -   NodeJS + Express
    -   PassportJS

All code in this repository is constructed using Vue, Python, and TypeScript with a simple microservice architecture. They are built using Docker, so you will need Docker to run Clickbait. It is also composed together using Nginx.

## Prerequisites

### Setup

DISCLAIMER: Make sure you're on Node v12.20.0 and Python 3.8+

Upgrade/Downgrade Node

```
npm i -g n
```

THEN

```
n 12.20.0
```

(You can skip the first step if you have n installed already)

Set Up Virtual Environment

```
cd recommender
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

Download Data

Please download the `USvideos.csv` from [this link](https://www.kaggle.com/datasnaek/youtube-new?select=USvideos.csv). Rename this file to `raw.csv` and place it in `/recommender/data`

Preprocess Data

```
yarn preprocess

OR

Run preprocess.ipynb in recommender/data
```

## Commands

### Web

Run Web (Developer Mode)

```
yarn web
```

### Recommender

Run Recommender

```
yarn recommender
```

Runs on localhost:5002

Stop Recommender

When you run the previous command, the last line (before the `✨ Done in xy.zzs.` line) will be a docker_id.

```
docker stop [docker_id]
```

### Server Maintainance

Run the following commands in the server directory

Install New Dependencies

```
source env/bin/activate
pip install [dependency]
pip freeze > requirements.txt
```

Install All Dependencies

```
pip install -r requirements.txt
```

Deactivate Python Environment (if active)

```
deactivate
```

NOTE: You probably want to run web and recommender in seperate terminals. They use hot reloading.

## Contributors

-   **Advaith Nair**

    -   _Full Stack Developer_
    -   [Website](https://advaithnair.com)
