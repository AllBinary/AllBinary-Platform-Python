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
# package org.allbinary.image

from __future__ import annotations



class ImageTool:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def main(args: list[str]) -> None:
        java.awt.EventQueue.invokeLater((ARunnable()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 commonStrings: CommonStrings = CommonStrings.getInstance()
#                 try:
#                     logUtil.putF(commonStrings.START, self, commonStrings.RUN)
#                     ImageToolJFrame().setVisible(True)
#                 except Exception as e:
#                     logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
))
from org.allbinary.thread.ARunnable import ARunnable
from org.allbinary.image.gui.ImageToolJFrame import ImageToolJFrame
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


