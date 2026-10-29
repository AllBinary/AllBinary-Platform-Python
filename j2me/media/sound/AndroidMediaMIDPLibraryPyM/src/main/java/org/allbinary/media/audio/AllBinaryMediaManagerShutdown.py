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
# package org.allbinary.media.audio

from __future__ import annotations



class AllBinaryMediaManagerShutdown:
    instance: AllBinaryMediaManagerShutdown = None
    

    # throws Exception
    @staticmethod
    def shutdown(soundsFactoryInterface: SoundsFactoryInterface) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        logUtil.putF("No Media Shutdown for Android Process", AllBinaryMediaManagerShutdown.instance, "shutdown")
from org.allbinary.logic.communication.log.LogUtil import LogUtil


AllBinaryMediaManagerShutdown.instance = AllBinaryMediaManagerShutdown()

