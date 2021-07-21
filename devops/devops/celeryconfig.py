# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/16

# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379'
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_TASK_SERIALIZER = 'json'

# CELERY_IMPORTS = (
#     'celery-test.tasks',
# )

CELERY_TASK_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'routing_key': 'beat_tasks'
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'routing_key': 'work_queue'
    }
}

CELERY_TASK_DEFAULT_QUEUE = 'work_queue'

# CELERY_TASK_ROUTES = {'celery-test-task-add': {'exchange': 'work_queue', 'exchange_type': 'direct', 'routing_key': 'work_queue'}}
CELERY_TASK_ROUTES = {'celery-test.tasks.*': {'queue': 'work_queue', 'routing_key': 'work_queue'}}

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

CELERY_TASK_TRACK_STARTED = True

CELERY_TIMEZONE = "Asia/Shanghai"

CELERY_ENABLE_UTC = False

# 使用 timezone naive 模式，不存储时区信息，只存储经过时区转换后的时间
DJANGO_CELERY_BEAT_TZ_AWARE = False
# 配置 celery 定时任务使用的调度器，使用django_celery_beat插件用来动态配置任务
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


