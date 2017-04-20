# Setting up Django

---

_Mac Only_

---
1) Install homebrew

2) Install python
```
brew install python --universal —framework
```
Add to bash if needed.
```
export PATH="/usr/local/bin:/usr/local/share/python:${PATH}"
```

3) Install virtualenv. Using this, anything you install through pip (the built-in python package manager) from now on will be installed in a new virtualenv, isolated from other environments and system-wide packages. Also, the name of the currently activated virtualenv will be displayed on the command line to help you keep track of which one you are using.
```
pip install virtualenv/Users/chesnutt/Documents/chessai2/setup2.md
```
It’s a good idea to keep all your virtualenvs in one place, for example in .virtualenvs/ in your home directory. Create it if it doesn’t exist yet:
```
mkdir ~/.virtualenvs
```
Now create the environment:
```
python3 -m venv ~/.virtualenvs/chessai
```
The final step in setting up your virtualenv is to activate it:
```
source ~/.virtualenvs/chessai/bin/activate
```
If the source command is not available, you can try using a dot instead:
```
. ~/.virtualenvs/djangodev/bin/activate
```
Now, with the env activated, install Django with:
```
pip install Django
```
