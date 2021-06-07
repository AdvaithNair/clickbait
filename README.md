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

All code in this repository is constructed using TypeScript (Vue) and Python.

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

Preprocess Data

`Please run preprocess.ipynb or preprocess.py to clean the data for the server`

## Commands

### Server

Run Server

```
yarn server
```

### Server Maintainance

Run the following commands in the server directory

Install Dependencies

```
pip install -r requirements.txt
```

Activate Python Environment

```
source env/bin/activate
```

Deactivate Python Environment

```
deactivate
```

Runs on localhost:5002

NOTE: You probably want to run web and server in two seperate terminals. They use hot reloading.

## Contributors

-   **Advaith Nair**

    -   _Full Stack Developer_
    -   [Website](https://advaithnair.com)
