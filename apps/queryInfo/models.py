# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class SfzInfo(models.Model):
    record_time = models.DateTimeField(verbose_name=u'刷卡时间', default=datetime.now)
    name = models.CharField(max_length=30, verbose_name=u'姓名')
    gender = models.CharField(max_length=2, verbose_name=u'性别')
    national = models.CharField(max_length=4, verbose_name=u'民族')
    birthday = models.CharField(max_length=16, verbose_name=u'出生日期')
    address = models.CharField(max_length=70, verbose_name=u'家庭住址')
    sfzid = models.CharField(max_length=36, verbose_name=u'身份证号码')
    maker = models.CharField(max_length=30, verbose_name=u'签发机关')
    start_date = models.CharField(max_length=8, verbose_name=u'有效期开始')
    end_date = models.CharField(max_length=8, verbose_name=u'有效期结束')
    reserved = models.CharField(max_length=36, verbose_name=u'修改信息')

    class Meta:
        verbose_name = u'进出记录查询'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.sfzid


