# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/8/10

from datetime import datetime
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")
django.setup()
from elasticsearch import Elasticsearch
from esmanager.models import Indexmanage
from esmanager.models import Escluster

class EsClusterClass:

    def __init__(self, clustercode):
        esclusterobj = Escluster.objects.get(code__exact=clustercode)

        self.clustercode = clustercode
        self.clientIp = esclusterobj.clientIp
        self.port = esclusterobj.port
        self.hosts = '{}:{}'.format(self.clientIp, self.port)
        self.es = Elasticsearch(hosts=self.hosts,
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
        print(index_list)
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
        print(topiclist)
        return topiclist

    def testtest(self):
        index_list = self.get_all_index()
        print(index_list)


if __name__ == '__main__':
    EsClusterClass('d-appsearch-elk').testtest()
