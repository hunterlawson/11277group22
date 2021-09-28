# 11277group22

Member1:  Hunter Lawson  
Member2:  Tiffany Wu  
Member3:  Heng Sun  
Member4:  Jiayu Huang  

# Developing

## Create a Virtual environment
(This only needs to be done once)

A python virtual environment stores all of the packages for your application in a local folder, that way you don't have to worry about missing any requirements.

1) `python -m venv env`  
This makes a virtual environment named 'env'
2) Run the 'env/Scripts/activate.bat' file  
This starts the virtual environment.
3) You should see (env) in front of your console. Now you can install the project requirements. Run: `pip install -r requirements.txt`

## Making a change

1) Ensure that your virtual environment is enabled (run the env/Scripts/activate.bat file)
2) Create a branch for the feature / fix: `git branch <feature-name>`
3) Switch to the new branch: `git checkout <feature-name>`
4) Make any changes / commits needed
5) Push your changes to the repository
6) Since your branch is not currently being tracked, if you just write `git push` it might tell you that you can't. It should give you the command to use instead: `git push --set-upstream origin <feature-name>`.
7) Create a pull request for your branch
8) Check that the pull request passes the tests in CircleCI. If it doesn't pass the tests, you can still make changes to the branch and push using `git push`.