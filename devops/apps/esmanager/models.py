# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/29

from django.db import models

class Escluster(models.Model):
    name = models.CharField("集群名称", max_length=50, help_text="集群名称")
    code = models.CharField("集群code", max_length=50, help_text="集群code")
    env = models.CharField("环境名称", max_length=32, help_text="环境名称")
    clientIp = models.GenericIPAddressField("连接节点", help_text="连接节点")
    monitorIp = models.GenericIPAddressField("监控节点", help_text="监控节点")
    port = models.IntegerField("集群端口", default=9200, help_text="集群端口")
    monitorPort = models.IntegerField("集群端口", default=9109, help_text="集群端口")
    saveDay = models.CharField("索引默认保留天数", max_length=32, help_text="索引默认保留天数")


class Indexmanage(models.Model):
    cluster = models.ManyToManyField(Escluster, related_name="clusterIndex", help_text="集群")
    name = models.CharField("索引名称", max_length=50, help_text="索引名称", db_index=True)
    saveDay = models.CharField("索引保留天数", max_length=32, help_text="索引保留天数")
    createTime = models.DateTimeField("创建时间", auto_now_add=True, help_text="创建时间")
    updateTime = models.DateTimeField("更新时间", auto_now=True, help_text="更新时间")
    monitorSt = models.BooleanField("监控状态", help_text="监控状态")


