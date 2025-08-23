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
python3.11 -m venv learning-env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
learning-env\Scripts\Activate.ps1
pip install -r requirements.txt
```
> **Note:**  
> If you see an error about "running scripts is disabled on this system", it means your Powershell execution policy is too restrictive.  
> To fix this, run the following command in your Powershell terminal **before activating**:
> ```
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> ```
> Then activate your environment with:
> ```
> learning-env\Scripts\Activate.ps1
> ```

### Running Test code
```
python3 ./Chapter_1_Setup/env_test.py
```