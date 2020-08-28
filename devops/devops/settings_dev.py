# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/18

from .settings import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django': {
            'handlers': ['reboot'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'handlers': {
        'reboot': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'formatters': {
        'simple': {
            'format': '%(name)s %(asctime)s %(levelname)s %(message)s'
        },
    },
    "root": {
        'handlers': ["reboot"],
        'level': 'DEBUG',
    }
}