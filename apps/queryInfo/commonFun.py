#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-07 10:53
# @Author  : James
# @Site    : 
# @File    : commonFun.py
# @Software: PyCharm
from ctypes import *
import os
import time
import RPi.GPIO as GPIO

from mjxt.settings import BASE_DIR


# 定义公共常量
usb = 0xff
so = cdll.LoadLibrary(os.path.join(BASE_DIR, 'extra_so/libs/libzkident.so'))


# 定义身份证信息的结构体
class Info(Structure):
    _fields_ = [
        ('name', c_ubyte*30),
        ('gender', c_ubyte*2),
        ('national', c_ubyte*4),
        ('birthday', c_ubyte*16),
        ('address', c_ubyte*70),
        ('id', c_ubyte*36),
        ('maker', c_ubyte*30),
        ('start_date', c_ubyte*16),
        ('end_date', c_ubyte*16),
        ('reserved', c_ubyte*36)
    ]


# 根据返回代码转报人员的性别
def getGender(genderCode):
    if genderCode == 1:
        return '男'
    else:
        return '女'


# 根据返回的代码转换相应的民族名称
def getNational(nationCode):
    if nationCode == 1:
        return '汉'
    elif nationCode == 2:
        return '蒙古'
    elif nationCode == 3:
        return '回'
    elif nationCode == 4:
        return '藏'
    elif nationCode == 5:
        return '维吾尔'
    elif nationCode == 6:
        return '苗'
    elif nationCode == 7:
        return '彝'
    elif nationCode == 8:
        return '壮'
    elif nationCode == 9:
        return '布依'
    elif nationCode == 10:
        return '朝鲜'
    elif nationCode == 11:
        return '满'
    elif nationCode == 12:
        return '侗'
    elif nationCode == 13:
        return '瑶'
    elif nationCode == 14:
        return '白'
    elif nationCode == 15:
        return '土家'
    elif nationCode == 16:
        return '哈尼'
    elif nationCode == 17:
        return '哈萨克'
    elif nationCode == 18:
        return '傣'
    elif nationCode == 19:
        return '黎'
    elif nationCode == 20:
        return '傈僳'
    elif nationCode == 21:
        return '佤'
    elif nationCode == 22:
        return '畲'
    elif nationCode == 23:
        return '高山'
    elif nationCode == 24:
        return '拉祜'
    elif nationCode == 25:
        return '水'
    elif nationCode == 26:
        return '东乡'
    elif nationCode == 27:
        return '纳西'
    elif nationCode == 28:
        return '景颇'
    elif nationCode == 29:
        return '柯尔克孜'
    elif nationCode == 30:
        return '土'
    elif nationCode == 31:
        return '达斡尔'
    elif nationCode == 32:
        return '仫佬'
    elif nationCode == 33:
        return '羌'
    elif nationCode == 34:
        return '布朗'
    elif nationCode == 35:
        return '撒拉'
    elif nationCode == 36:
        return '毛南'
    elif nationCode == 37:
        return '仡佬'
    elif nationCode == 38:
        return '锡伯'
    elif nationCode == 39:
        return '阿昌'
    elif nationCode == 40:
        return '普米'
    elif nationCode == 41:
        return '塔吉克'
    elif nationCode == 42:
        return '怒'
    elif nationCode == 43:
        return '乌孜别克'
    elif nationCode == 44:
        return '俄罗斯'
    elif nationCode == 45:
        return '鄂温克'
    elif nationCode == 46:
        return '德昂'
    elif nationCode == 47:
        return '保安族'
    elif nationCode == 48:
        return '裕固'
    elif nationCode == 49:
        return '京'
    elif nationCode == 50:
        return '塔塔尔'
    elif nationCode == 51:
        return '独龙'
    elif nationCode == 52:
        return '鄂伦春'
    elif nationCode == 53:
        return '赫哲'
    elif nationCode == 54:
        return '门巴'
    elif nationCode == 55:
        return '珞巴'
    elif nationCode == 56:
        return '基诺'
    else:
        return '未知'


# 发送开门信号
def open_door():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()




#读取身份证信息并解析
def read_identfy_info():
    usb = 0xff
    ucIIN = c_ubyte*4
    ucSN = c_ubyte*8
    info_len = c_int
    photo = 0
    photo_len = 0
    oinfo = Info()
    oinfo_len = info_len()
    oucIIN = ucIIN()
    oucSN = ucSN()

    ret = so.ZKID_StartFindIDCard(usb, byref(oucIIN), 0)
    if ret < 0:
        pass

    ret = so.ZKID_SelectIDCard(usb, byref(oucSN), 0)
    if ret < 0:
        pass

    ret = so.ZKID_ReadBaseMsg(usb, byref(oinfo), byref(oinfo_len), photo, photo_len, 0)
    if ret >= 0:


        name = oinfo.name[:]
        gender = oinfo.gender[:]
        national = oinfo.national[:]
        birthday = oinfo.birthday[:]
        address = oinfo.address[:]
        id = oinfo.id[:]
        maker = oinfo.maker[:]
        start_date = oinfo.start_date[:]
        end_date = oinfo.end_date[:]

        s_name = bytearray(name).decode('utf-16')
        s_gender = getGender(int(bytearray(gender).decode('utf-16')))
        s_national = getNational(int(bytearray(national).decode('utf-16')))
        s_birthday = bytearray(birthday).decode('utf-16')
        s_address = bytearray(address).decode('utf-16')
        s_id = bytearray(id).decode('utf-16')
        #print s_id
        s_maker = bytearray(maker).decode('utf-16')
        s_start_date = bytearray(start_date).decode('utf-16')
        s_end_date = bytearray(end_date).decode('utf-16')
        #so.ZKID_Beep(2)
        return s_name, s_gender, s_national, s_birthday, s_address, s_id, s_maker, s_start_date, s_end_date
    else:
        t = ()
        return t


# 读取身份证信息的全流程
def use_device():
    ret = so.ZKID_OpenPort(usb)
    if ret < 0:
        print '打开设备失败！'

    if so.ZKID_GetSAMStatus(usb, 0) < 0:
        print '读取设备状态失败！'
