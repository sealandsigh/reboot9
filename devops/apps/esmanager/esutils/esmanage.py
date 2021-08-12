# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/8/10

from datetime import datetime
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")
django.setup()
from elasticsearch import Elasticsearch
from esmanager.models import Indexmanage
from esmanager.models import Escluster

class EsClusterClass:

    def __init__(self, clustercode):
        esclusterobj = Escluster.objects.get(code__exact=clustercode)

        self.username = esclusterobj.username
        self.password = esclusterobj.password[:-5]
        self.clustercode = clustercode
        self.clientIp = esclusterobj.clientIp
        self.port = esclusterobj.port
        self.auth = eval('("{}", "{}")'.format(self.username, self.password))
        self.hosts = '{}:{}'.format(self.clientIp, self.port)
        self.es = Elasticsearch(hosts=self.hosts,
                   http_auth=self.auth,
                   timeout=120,
                   max_retries=10,
                   retry_on_timeout=True,
                   sniff_on_start=True,
                   sniff_on_connection_fail=True,
                   sniffer_timeout=60
                   )

    def get_all_index(self):
        indices = self.es.cat.indices(format='json')
        index_list = []
        for i in indices:
            i = i.get('index')
            index_list.append(i)
        return index_list

    def get_all_topic(self):
        topicobj = Indexmanage.objects.filter(
            cluster=Escluster.objects.get(code=self.clustercode)
        )
        topiclist = []
        topicdic = {}
        for topic in topicobj:
            topicdic["topicname"] = topic.name
            topicdic["saveday"] = topic.saveDay
            topiclist.append(topicdic)
        return topiclist

    def delete_index(self):
        index_list = self.get_all_index()
        topic_list = self.get_all_topic()
        print(index_list)
        print(topic_list)


if __name__ == '__main__':
    EsClusterClass('t-me-elk').delete_index()
    # es = Elasticsearch(hosts='10.139.39.209:9200',
    #                    http_auth=('elastic', 'tmeelk'),
    #                    timeout=120,
    #                    max_retries=10,
    #                    retry_on_timeout=True,
    #                    sniff_on_start=True,
    #                    sniff_on_connection_fail=True,
    #                    sniffer_timeout=60
    #                    )
    # eshealth = es.cat.health(format='json')
    # print(eshealth)