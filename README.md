# SETUP PROJECT (Prerequisites : You have Postgres database in your system eg. my_database and python 3.4)
Create a folder <new_folder>
cd <new_folder>
Now clone the project : git@github.com:crazy-ninja/reminder.git
Create virtualenv and activate source
cd reminder
Go to reminder/settings.py and change the database setting according to you
Now import the settings by running the following cmd : export DJANGO_SETTINGS_MODULE='reminder.settings'
pip install requirements.txt
python manage.py migrate
python manage.py runserver


########################################################################################################################
                                API_DETAILS
########################################################################################################################

URL : api/remind-me/
METHOD : POST
PARAMS : 'email'
         'mobile'
         'message'
         'date_time'
