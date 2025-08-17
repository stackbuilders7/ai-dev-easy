## Introduction

Welcome to StackBuilder! 
In this chapter we will learn setting up python environment for your development.

## Setup

### Python version

Python 3.11 or later works well for AI development, specifically with Langchain.
```
python3 --version
```

### Clone repo
```
git clone https://github.com/stackbuilders7/ai-dev-easy.git
cd Chapter_1_Setup
```

### Create an environment and install dependencies
In below using `python3.11` to specifically using 3.11, you can instead use just python3 also.
```
python3.11 -m venv learning-env
source learning-env/bin/activate
pip install -r requirements.txt
```
#### Windows Powershell
```
python3 -m venv learning-env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
learning-env\scripts\activate
pip install -r requirements.txt
```

### Running Test code
```
python3 ./Chapter_1_Setup/env_test.py
```