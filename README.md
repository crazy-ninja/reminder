# SETUP PROJECT (Prerequisites : You have Postgres database in your system eg. my_database and python 3.4) <br>
Create a folder (new_folder) <br>
cd (new_folder) <br>
Now clone the project : git@github.com:crazy-ninja/reminder.git <br>
Create virtualenv and activate source <br>
cd reminder <br>
Go to reminder/settings.py and change the database setting according to you <br>
Now import the settings by running the following cmd : export DJANGO_SETTINGS_MODULE='reminder.settings' <br>
pip install requirements.txt <br>
python manage.py migrate <br>
python manage.py runserver <br>


########################################################################################################################
                                API_DETAILS
########################################################################################################################

URL : api/remind-me/ <br>
METHOD : POST <br>
PARAMS : 'email' <br>
         'mobile' <br>
         'message' <br>
         'date_time' <br>
