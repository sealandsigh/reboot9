# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/27

from django.db  import models

class Cloud(models.Model):
    name = models.CharField("云厂商名称", max_length=50, help_text="云厂商名称")
    code = models.CharField("云厂商名称", max_length=50, help_text="云厂商名称")

    def __str__(self):
        return self.code

class Server(models.Model):
    cloud        = models.ForeignKey(Cloud)
    instanceId   = models.CharField("实例ID", max_length=100, db_index=True, help_text="实例ID")
    instanceType = models.CharField("实例类型", max_length=100, help_text="实例类型")
    cpu          = models.CharField("cpu", max_length=32,help_text="cpu")
    memory       = models.CharField("memory", max_length=32,help_text="memory")
    instanceName = models.CharField("实例名称", max_length=100, db_index=True, help_text="实例名称")
    createdTime  = models.DateTimeField("创建时间", db_index=True)
    expiredTime  = models.DateTimeField("到期时间", db_index=True, null=True)
    hostname     = models.CharField("主机名", max_length=100, db_index=True)

    class Meta:
        permissions = (
            ("view_server", "can view server"),
            ("change_server_status", "Can change the status of server"),
        )


class Ip(models.Model):
    ip = models.GenericIPAddressField(db_index=True)
    inner = models.ForeignKey(Server, related_name="innerIpAddress", null=True)
    public = models.ForeignKey(Server, related_name="publicIpAddress", null=True)