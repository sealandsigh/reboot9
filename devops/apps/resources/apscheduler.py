# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/9/1

from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events
from apscheduler.schedulers.background import BackgroundScheduler
from  apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from resources.qcloud.cvm import getCvmlist

# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

# @register_job(scheduler, "interval", seconds=3)
# def myjob():
#     print("myjob is run: {}".format(datetime.datetime.now()))

@register_job(scheduler, "interval", seconds=30)
def syncQcloud():
    getCvmlist()


register_events(scheduler)
