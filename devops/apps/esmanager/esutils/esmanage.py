# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/8/10

from datetime import datetime
import os
import django
import re
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")
django.setup()
from elasticsearch import Elasticsearch
from esmanager.models import Indexmanage
from esmanager.models import Escluster
from esmanager.serializers import IndexmanageSerializer

class EsClusterClass:

    def __init__(self, clustercode):
        esclusterobj = Escluster.objects.get(code__exact=clustercode)

        self.username = esclusterobj.username
        self.password = esclusterobj.password[:-5]
        self.default_save_day = esclusterobj.saveDay
        self.clusterid = esclusterobj.id
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
        for topic in topicobj:
            topicdic = {}
            topicdic['topicname'] = topic.name
            topicdic['saveday'] = topic.saveDay
            topiclist.append(topicdic)
        return topiclist

    def date_compare(self, date1, saveday, fmt='%Y.%m.%d'):
        zero = datetime.datetime.fromtimestamp(0)
        today = datetime.datetime.now()
        saveday = int(saveday)
        offset = datetime.timedelta(days=-saveday)
        date2 = (today + offset).strftime('%Y.%m.%d')

        try:
            d1 = datetime.datetime.strptime(str(date1), fmt)
        except:
            d1 = zero

        try:
            d2 = datetime.datetime.strptime(str(date2), fmt)
        except:
            d2 = zero
        return d1 < d2

    def delete_index(self):
        index_list = self.get_all_index()
        topic_list = self.get_all_topic()
        print(index_list)
        print(topic_list)
        index_del_list = []
        for topic in topic_list:
            # print(topic["saveday"])
            # print(topic['topicname'])
            for index in index_list:
                if index == '.kibana' or index == '' or re.match(re.compile(r'^\.'), index):
                    continue
                matchObj = re.match(r'(.*)-(\d{4}.\d{2}.\d{2})', index, re.M | re.I)
                if matchObj:
                    if topic['topicname'] == matchObj.group(1) and self.date_compare(
                            matchObj.group(2), topic["saveday"]):
                        index_del_list.append(index)
                        if len(index_del_list) > 19:
                            print("len big 19")
                            self.es.indices.delete(index_del_list)
                            index_del_list = []
        if len(index_del_list) > 1:
            print("len big 1 end to delete")
            print(index_del_list)
            self.es.indices.delete(index_del_list)
        else:
            print("not need to delete")

    def sync_topic(self):
        index_list = self.get_all_index()
        topic_list = self.get_all_topic()
        topic_name_list = []
        for topic in topic_list:
            topic_name_list.append(topic["topicname"])
        index_tmp_list = []
        for index in index_list:
            matchObj = re.match(r'(.*)-(\d{4}.\d{2}.\d{2})', index, re.M | re.I)
            if matchObj:
                indexname = matchObj.group(1)
                index_tmp_list.append(indexname)
        sync_list = list(set(index_tmp_list))
        for syncindex in sync_list:
            syncdict = {}
            if syncindex in topic_name_list:
                continue
            else:
                syncdict["name"] = syncindex
                syncdict["saveDay"] = self.default_save_day
                syncdict["monitorSt"] = 'false'
                syncdict["cluster"] = [self.clusterid]
                serializer = IndexmanageSerializer(data=syncdict)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)



if __name__ == '__main__':
    # EsClusterClass('t-me-elk').delete_index()
    EsClusterClass('t-me-elk').sync_topic()
    # EsClusterClass('t-me-elk').get_all_topic()

    # delindex = ['dd-app-mp-chaos-dev-info-2021.07.06', 'dd-mplopa-admin-dev-docker-info-log-2021.07.02']
    # EsClusterClass('t-me-elk').delete_test(delindex)

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