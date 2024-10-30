import time
from django.urls import reverse
from django.utils.text import slugify


def upload_image_top_project(instance, filename):
    path = 'uploads/' + 'top_project/' + \
        slugify(instance.project_name, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.project_name) + '-' + filename
    return path + '/' + name
