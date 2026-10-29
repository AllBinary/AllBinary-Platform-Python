#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.logic.system.os.android

from __future__ import annotations

from org.allbinary.data.resource.ResourceUtil import ResourceUtil


class AndroidSystemProperties:
    SINGLETON: AndroidSystemProperties = None

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance() -> AndroidSystemProperties:
        return AndroidSystemProperties.SINGLETON
    

    def __init__(self, context: Context) -> None:
        self._init_fields()
    

    def getDeviceId(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def getDeviceSoftwareVersion(self) -> str:
        return self.commonStrings.DISABLE
    

    def getLine1Number(self) -> str:
        return self.commonStrings.DISABLE
    

    def getNetworkCountryIso(self) -> str:
        return self.commonStrings.DISABLE
    

    def getNetworkOperator(self) -> str:
        return self.commonStrings.DISABLE
    

    def getNetworkOperatorName(self) -> str:
        return self.commonStrings.DISABLE
    

    def getSimCountryIso(self) -> str:
        return self.commonStrings.DISABLE
    

    def getSimOperator(self) -> str:
        return self.commonStrings.DISABLE
    

    def getSimOperatorName(self) -> str:
        return self.commonStrings.DISABLE
    

    def getSimSerialNumber(self) -> str:
        return self.commonStrings.DISABLE
    

    def getSubscriberId(self) -> str:
        return self.commonStrings.DISABLE
    

    def getVoiceMailAlphaTag(self) -> str:
        return self.commonStrings.DISABLE
    

    def getVoiceMailNumber(self) -> str:
        return self.commonStrings.DISABLE
    

    def getNetworkType(self) -> int:
        return -1
    

    def getPhoneType(self) -> int:
        return -1
    

    def getBoard(self) -> str:
        return Build.BOARD
    

    def getBrand(self) -> str:
        return Build.BRAND
    

    def getDevice(self) -> str:
        return Build.DEVICE
    

    def getFingerprint(self) -> str:
        return Build.FINGERPRINT
    

    def getHost(self) -> str:
        return Build.HOST
    

    def getId(self) -> str:
        return Build.ID
    

    def getModel(self) -> str:
        return Build.MODEL
    

    def getProduct(self) -> str:
        return Build.PRODUCT
    

    def getTags(self) -> str:
        return Build.TAGS
    

    def getTime(self) -> int:
        return Build.TIME
    

    def getType(self) -> str:
        return Build.TYPE
    

    def getUser(self) -> str:
        return Build.USER
from android.content.Context import Context
from android.os.Build import Build
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


AndroidSystemProperties.SINGLETON = AndroidSystemProperties(ResourceUtil.getInstance().getContext())

