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
# package org.allbinary.logic.java.help

from __future__ import annotations

from org.allbinary.util.BasicArrayListD import BasicArrayListD


class JavaHelpSetNotifier:
    vector: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def get() -> BasicArrayList:
        return JavaHelpSetNotifier.vector
    

    @staticmethod
    def isNotified(helpSet: HelpSet) -> bool:
        isNotified: bool = False
        url: URL = helpSet.getHelpSetURL()
        size: int = JavaHelpSetNotifier.vector.size()
        urlArray: list[object] = JavaHelpSetNotifier.vector.toArray()
        for i in range(0, size):
            nextURL: URL = urlArray[i]
            if ((str(url) > str(nextURL)) - (str(url) < str(nextURL))) == 0:
                isNotified = True
        JavaHelpSetNotifier.vector.add(url)
        return isNotified
# from java.net.URL import URL
from org.allbinary.util.BasicArrayList import BasicArrayList
# from javax.help.HelpSet import HelpSet


