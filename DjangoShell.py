import os 
os.environ.setdefault["DJANGO_SETTINGS_MODULE", "learning_log.settings"]

import django 
django.setup()

from pizzas.models import Topic 

