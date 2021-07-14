# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/13

import time
from celery import Celery

celery_app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')
# this is celery settings

# this is a function about need many time
@celery_app.task
def add(a, b):
    time.sleep(5)
    return a + b
