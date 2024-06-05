# Event-Browser
This is a project for the university, it is a simple event creator, in which user after registering can create an event, other users can declare the willingness to participate in such events
# Instalation
- Clone the git repository and enter it in the terminal with ```cd <repo>```
- Before using locally the web aplication, you need to create a new virtual environment, using ```virtual <name_of_your_virtual_environment>``` by typing the following command in the terminal.
- The virtual environment can be activated by ```Scripts/activate.bat``` command typed in the terminal, which activates our virtual environment.
- Now enter the ```pip install -r requirements.txt``` command to download every needed dependancies to be able to use the aplication.
# How to open locally
- Before using the app for the first time, while having the virtual environment active, navigate to the Event-Browser folder and you need to type the ```python manage.py makemigrations``` to create every database that the app is working on, and after that type the ``` python manage.py migrate``` command
- While being in the Event-Browser folder turn on the server with ```python manage.py runserver``` command.
- Lastly open the internet browser and type in search bar ```127.0.0.1:8000```
- Now you can use the app
# Admin panel
To have an access to the admin panel, in which you can see every registered user, their events, etc, you have to:
- Have an activated virtual environment
- use the ```python manage.py createsuperuser``` command
- add an email and password for the super user
- to open an admin panel navigate to ```127.0.0.1:8000/admin``` and use the credentials that were used to create the super user
