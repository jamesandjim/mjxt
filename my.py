#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-11 17:49
# @Author  : James
# @Site    : 
# @File    : my.py
# @Software: PyCharm
import time

import requests

time.sleep(8)
r = requests.get("http://127.0.0.1:8000")
r.status_code




