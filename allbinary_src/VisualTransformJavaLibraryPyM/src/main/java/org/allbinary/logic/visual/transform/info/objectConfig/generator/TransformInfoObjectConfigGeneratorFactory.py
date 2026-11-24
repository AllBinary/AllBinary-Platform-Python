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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGeneratorFactoryInterface import TransformInfoObjectConfigGeneratorFactoryInterface


class TransformInfoObjectConfigGeneratorFactory(TransformInfoObjectConfigGeneratorFactoryInterface):
    instance: TransformInfoObjectConfigGeneratorFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> TransformInfoObjectConfigGeneratorFactory:
        return TransformInfoObjectConfigGeneratorFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getInstance_j1(self, transformInfoInterface: TransformInfoInterface) -> TransformInfoObjectConfigGenerator:
        from org.allbinary.logic.visual.transform.info.objectConfig.generator.StoreFileGenerator import StoreFileGenerator
        from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        type_: str = transformInfoInterface.getObjectConfigInterface().getOutputTypeName()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF("Generating Instance for type: " + type_, self, commonStrings.GET_INSTANCE)
        if type_ is None or ((type_ > InputOutputTypeData.getInstance().RESPONSE) - (type_ < InputOutputTypeData.getInstance().RESPONSE)) == 0 or transformInfoInterface.isChild():
            return BasicGenerator()
        elif ((type_ > InputOutputTypeData.getInstance().FILE) - (type_ < InputOutputTypeData.getInstance().FILE)) == 0:
            return StoreFileGenerator(transformInfoInterface)
        else:
            raise Exception("No Such TransformInfoObjectConfigGenerator Type")

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _TransformInfoObjectConfigGeneratorFactory_instance() -> object:
    return TransformInfoObjectConfigGeneratorFactory()

lazy_static(TransformInfoObjectConfigGeneratorFactory, "instance", _TransformInfoObjectConfigGeneratorFactory_instance)

