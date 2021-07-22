# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/13

import time
from celery import Celery
from devops import celeryconfig
# from devops.celery import app
from celery import shared_task

# celery_app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')
# celery_app = app


# celery_app.config_from_object(celeryconfig)
# celery_app.conf.task_default_queue = 'work_queue'

# this is a function about need many time
# @celery_app.task()
@shared_task()
def add(a, b):
    time.sleep(5)
    return a + b
