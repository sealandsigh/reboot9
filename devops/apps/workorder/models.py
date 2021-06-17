# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/17

from django.db import models
from users.models import User

class WorkOrder(models.Model):
    TYPE = (
        (0, '数据库'),
        (1, 'WEB任务'),
        (2, '计划任务'),
        (3, '配置文件'),
        (4, '其它'),
    )
    STATUS = (
        (0, '申请'),
        (1, '处理中'),
        (2, '完成'),
        (3, '失败'),
    )
    title = models.CharField(max_length=100, verbose_name='工单标题')
    type = models.IntegerField(choices=TYPE, default=0, verbose_name='工单类型')
    order_contents = models.TextField(verbose_name='工单内容')
    applicant = models.ForeignKey(User, verbose_name='申请人', related_name='work_order_applicant')
    assign_to = models.ForeignKey(User, verbose_name='指派给')
    final_processor = models.ForeignKey(User, null=True, blank=True, verbose_name='最终处理人', related_name='final_processor')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='工单状态')
    result_desc = models.TextField(verbose_name='处理结果', null=True, blank=True)
    apply_time = models.DateField(auto_now_add=True, verbose_name='申请时间')
    complete_time = models.DateField(auto_now=True, verbose_name='处理完成时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '工单'
        verbose_name_plural = verbose_name
        ordering = ['-complete_time']
