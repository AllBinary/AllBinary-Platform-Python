# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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
# package org.allbinary.logic

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


#Handle the differences in the public platform vs the raw JS build
class MEUtil:
    instance: MEUtil = None
    

    @staticmethod
    def getInstance() -> MEUtil:
        return MEUtil.instance
    

    def appendItem(self, form: CommandForm, item: Item) -> None:
        from javax.microedition.lcdui.Item import Item
        from org.allbinary.MIDPUtil import MIDPUtil
        from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm
        MIDPUtil.getInstance().appendItem(form, item)
# from javax.microedition.lcdui.Item import Item
# from org.allbinary.MIDPUtil import MIDPUtil
# from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm


def _MEUtil_instance() -> object:
    return MEUtil()

lazy_static(MEUtil, "instance", _MEUtil_instance)

