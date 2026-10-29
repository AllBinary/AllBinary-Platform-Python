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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


class CustomTransformInfo(TransformInfo, TransformInfoInterface):
    

    def __init__(self, outputTypeName: str, inputOutputTypeName: str, inputOutputTypeFile: str, name: str, objectFileName: str, objectConfigFileName: str, templateFileName: str, dataFileName: str) -> None:
        super().__init__()


