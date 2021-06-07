# Clickbait

Clickbait is a project where I will recommend trending YouTube videos to a user. I plan to use a bit of NLP to play around with content-based recommenders.

## Technology Overview

It utilizes the following technologies:

-   Web
    -   VueJS
    -   NuxtJS
-   Server
    -   Python
    -   Flask
    -   SciKit Learn

All code in this repository is constructed using TypeScript (Vue) and Python. Both are built using Docker, so you will need Docker to run Clickbait.

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

Download Data

Please download the `USvideos.csv` from [this link](https://www.kaggle.com/datasnaek/youtube-new?select=USvideos.csv). Rename this file to `raw.csv` and place it in `/server/data`

Preprocess Data

```
Please run preprocess.ipynb or preprocess.py to clean the data for the server
```

## Commands

### Server

Run Server

```
yarn server
```

Runs on localhost:5002

Stop Server

When you run the previous command, the last line (before the `✨ Done in xy.zzs.` line) will be a docker_id.

```
docker stop [docker_id]
```

### Server Maintainance

Run the following commands in the server directory

Install Dependencies

```
pip install -r requirements.txt
```

Deactivate Python Environment (if active)

```
deactivate
```

NOTE: You probably want to run web and server in two seperate terminals. They use hot reloading.

## Contributors

-   **Advaith Nair**

    -   _Full Stack Developer_
    -   [Website](https://advaithnair.com)
