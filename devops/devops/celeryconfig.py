# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/16

CELERY_IMPORTS = (
    'celery-test.tasks',
)

# 有些情况可以防止死锁,这个参数在4版本后没有，仅记录下
# CELERYD_FORCE_EXECV = True

# 设置并发的worker数量
CELERY_WORKER_CONCURRENCY = 2

# 允许重试
CELERY_TASK_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁，可以防止内存泄漏
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间 1800秒 超过会被杀掉
CELERY_TASK_TIME_LIMIT = 30 * 60


