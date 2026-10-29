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
# package org.allbinary.logic.visual.transform.info.objectConfig.generator

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGeneratorFactoryInterface import TransformInfoObjectConfigGeneratorFactoryInterface


class TransformInfoObjectConfigGeneratorFactory(TransformInfoObjectConfigGeneratorFactoryInterface):
    instance: TransformInfoObjectConfigGeneratorFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> TransformInfoObjectConfigGeneratorFactory:
        return TransformInfoObjectConfigGeneratorFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, transformInfoInterface: TransformInfoInterface) -> TransformInfoObjectConfigGenerator:
        from org.allbinary.logic.visual.transform.info.objectConfig.generator.StoreFileGenerator import StoreFileGenerator
        from org.allbinary.logic.visual.transform.info.objectConfig.generator.BasicGenerator import BasicGenerator
        type_: str = transformInfoInterface.getObjectConfigInterface().getOutputTypeName()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF("Generating Instance for type: " + type_, self, commonStrings.GET_INSTANCE)
        if type_ is None or ((type_ > InputOutputTypeData.getInstance().RESPONSE) - (type_ < InputOutputTypeData.getInstance().RESPONSE)) == 0 or transformInfoInterface.isChild():
            return BasicGenerator()
        elif ((type_ > InputOutputTypeData.getInstance().FILE) - (type_ < InputOutputTypeData.getInstance().FILE)) == 0:
            return StoreFileGenerator(transformInfoInterface)
        else:
            raise Exception("No Such TransformInfoObjectConfigGenerator Type")
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings


TransformInfoObjectConfigGeneratorFactory.instance = TransformInfoObjectConfigGeneratorFactory()

