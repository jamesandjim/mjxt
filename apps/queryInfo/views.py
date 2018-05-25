# _*_ coding:utf-8 _*_
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import SfzInfo
from commonFun import use_device, read_identfy_info, open_door


# Create your views here.
class ReadCardView(View):
    def get(self, request):
        use_device()

        while True:
            info = SfzInfo()
            xinfo = read_identfy_info()
            if len(xinfo) > 0:
                info.name = xinfo[0]
                info.maker = xinfo[6]
                info.sfzid = xinfo[5]
                info.address = xinfo[4]
                info.national = xinfo[2]
                info.gender = xinfo[1]
                info.birthday = xinfo[3]
                info.start_date = xinfo[7]
                info.end_date = xinfo[8]

                info.save()

                open_door()

            #time.sleep(0.1)
        return HttpResponse('ok')

    def post(self, request):
        use_device()

        while True:
            info = SfzInfo()
            xinfo = read_identfy_info()
            if len(xinfo) > 0:
                info.name = xinfo[0]
                info.maker = xinfo[6]
                info.sfzid = xinfo[5]
                info.address = xinfo[4]
                info.national = xinfo[2]
                info.gender = xinfo[1]
                info.birthday = xinfo[3]
                info.start_date = xinfo[7]
                info.end_date = xinfo[8]

                info.save()

                open_door()

            #time.sleep(0.1)
        return HttpResponse('ok')
