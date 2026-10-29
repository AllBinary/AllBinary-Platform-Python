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
        from org.allbinary.media.audio.AllBinaryMediaManager import AllBinaryMediaManager
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil.putF(commonStrings.START, AllBinaryMediaManagerShutdown.instance, "shutdown")
        AllBinaryMediaManager.shutdown(soundsFactoryInterface)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


AllBinaryMediaManagerShutdown.instance = AllBinaryMediaManagerShutdown()

