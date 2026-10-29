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
# package org.allbinary.input.automation.module.actions.script.condition.processors.output

from __future__ import annotations



class ImageActionScriptOutputProcessor:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    @staticmethod
    def process(imageActionScriptOutputInterface: ImageActionScriptOutputInterface, frame: int) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil.putF("Start - Processing at: " + str(imageActionScriptOutputInterface), "ImageActionScriptOutputProcessor", commonStrings.PROCESS)
        imageTypes: ImageTypes = imageActionScriptOutputInterface.getImageTypes()
        vector: BasicArrayList = imageTypes.getVector()
        size: int = vector.size()
        for index in range(0, size):
            imageType: InputImageType = vector.get(index)
            imageIOInterface: ImageIOInterface = InputImageIOInterfaceFactory.getInstance(imageType)
            imageIOInterface.save(frame)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.media.image.InputImageIOInterfaceFactory import InputImageIOInterfaceFactory
from org.allbinary.input.media.image.InputImageType import InputImageType
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.io.ImageIOInterface import ImageIOInterface
from org.allbinary.string.CommonStrings import CommonStrings


