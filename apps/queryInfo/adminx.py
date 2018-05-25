#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-10 13:45
# @Author  : James
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from xadmin import views

from .models import SfzInfo



class GlobalSettings(object):
    site_title = '身份证进出查询系统'
    site_footer = '2018 SDTI'
    menu_style = 'accordion'

class SfzInfoAdmin(object):
    list_display = ['record_time', 'name', 'gender', 'national', 'birthday', 'address', 'sfzid', 'maker', 'start_date', 'end_date']
    search_fields = ['name', 'gender', 'national', 'birthday', 'address', 'sfzid', 'maker', 'start_date', 'end_date']
    list_filter = ['record_time', 'name', 'gender', 'national', 'birthday', 'address', 'sfzid', 'maker', 'start_date', 'end_date']


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(SfzInfo, SfzInfoAdmin)
