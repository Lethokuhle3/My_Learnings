python virtual environments

third party packages- pip commands


version conflicts happens when you have installed maybe Django version 3 for this project but another project doesn't use Django 3 it uses
Django4, so where that's when a conflict happens.. so the solution for all these problems is a virtual environments, separating your Python environments
A virtual environment is an isolated environment that physically lives inside a folder that contains all the packages and dependencies

I tried with "where pip" to see where its installed which pip was not working
```py
>mkdir my-python-project for creating a project
>cd my-python-project
> python3 -m venv <name_of_virtualenv>
>ls to check the list BUT you’re working in the Windows Command Pro ls is not recognised, you have to use dir and not ls
```