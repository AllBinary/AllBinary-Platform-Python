# 
# AllBinary Open License Version 1 
# Copyright (c) 2019 AllBinary 
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
# package org.allbinary.android

from __future__ import annotations



class AndroidServicesUtil:
    instance: AndroidServicesUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        self.SERVICE_LIMIT_MAX: int = 1000
        self.IS_SERVICE_RUNNING: str = "isServiceRunning"
        self.SERVICE_NOT_FOUND_RUNNING: str = "Service not found Running: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AndroidServicesUtil:
        return AndroidServicesUtil.instance
    

    def isServiceRunning(self, name: str) -> bool:
        activityManager: ActivityManager = self.resourceUtil.getContext().getSystemService(Context.ACTIVITY_SERVICE)
        runningServicesList: List[RunningServiceInfo] = activityManager.getRunningServices(self.SERVICE_LIMIT_MAX)
        runningServiceInfo: RunningServiceInfo = None
        serviceComponent: ComponentName = None
        serviceName: str = None
        size: int = runningServicesList.size()
        for index in range(0, size):
            runningServiceInfo = runningServicesList.get(index)
            serviceComponent = runningServiceInfo.service
            serviceName = str(serviceComponent)
            if serviceName.find(name) >= 0:
                return True
        self.logUtil.putF(self.SERVICE_NOT_FOUND_RUNNING + name, self, self.IS_SERVICE_RUNNING)
        return False
# from java.util.List import List
from android.app.ActivityManager import ActivityManager
from android.app.ActivityManager.RunningServiceInfo import RunningServiceInfo
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


AndroidServicesUtil.instance = AndroidServicesUtil()

