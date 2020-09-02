# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/9/1

from django.core.management.base import BaseCommand
from resources.apscheduler import scheduler

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("django schedule is run")
        scheduler.start()