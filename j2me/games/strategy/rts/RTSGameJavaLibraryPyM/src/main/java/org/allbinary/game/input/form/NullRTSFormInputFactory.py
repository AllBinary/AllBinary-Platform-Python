# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.input.form

from __future__ import annotations

from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput


class NullRTSFormInputFactory:
    SINGLETON: RTSFormInput = RTSFormInput(BasicGroupFactory.getInstance().NONE_ARRAY)
    

    @staticmethod
    def getInstance() -> RTSFormInput:
        return NullRTSFormInputFactory.SINGLETON


