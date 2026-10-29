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
# package org.allbinary.logic.communication.log

from __future__ import annotations



class TestRemoteLogUtil:
    PATH: str = "G:\\mnt\\bc\\mydev\\work\\allbinary_src\\licensing\\data\\"
    

    def __init__(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        Globals.getInstance().init(type(self).getClassLoader(), TestRemoteLogUtil.PATH)
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil.put(commonStrings.EXCEPTION, "Test", "TestClass", Exception("Pretend Exception"))
    

    # throws Exception
    @staticmethod
    def main(args: list[str]) -> None:
        TestRemoteLogUtil()
from org.allbinary.globals.Globals import Globals
from org.allbinary.string.CommonStrings import CommonStrings


