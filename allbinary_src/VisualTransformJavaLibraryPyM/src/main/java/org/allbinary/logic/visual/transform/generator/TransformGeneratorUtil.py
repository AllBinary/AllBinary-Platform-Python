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
# package org.allbinary.logic.visual.transform.generator

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class TransformGeneratorUtil:
    instance: TransformGeneratorUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> TransformGeneratorUtil:
        return TransformGeneratorUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def generate_j3_1(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, ownerTransformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
        from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.objectConfig.generator.StoreFileGenerator import StoreFileGenerator
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Generating View: " + transformInfoInterface.getName(), self, "generate()")
            componentInterface: TransformInterface = TransformFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface.getName(), ownerTransformInfoInterface)
            result: str = componentInterface.view()
            httpTransformInfoInterface: TransformInfoHttpInterface = componentInterface.getTransformInfoInterface()
            inputOutputTypeData: InputOutputTypeData = InputOutputTypeData.getInstance()
            if result.find("<HTML>") >= 0:
                httpTransformInfoInterface.getPropertiesHashMap().put(inputOutputTypeData.NAME, inputOutputTypeData.DEFAULT)
            else:
                httpTransformInfoInterface.getPropertiesHashMap().put(inputOutputTypeData.NAME, inputOutputTypeData.DEFAULT_FRAGMENT)
            StoreFileGenerator(componentInterface.getTransformInfoInterface()).process(result)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate a view", self, "generate()", e)
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def generate_j3_2(self, abeClientInformation: AbeClientInformationInterface, transformInfoDomNode: TransformInfoDomNode, ownerTransformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        self.generate(abeClientInformation, transformInfoDomNode.getTransformInfoInterface(), ownerTransformInfoInterface)

    def generate(self, *args):
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "AbeClientInformationInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[1]).__mro__)) and (args[2] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[2]).__mro__)):
            return __class__.__dict__["generate_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["generate_j3_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("generate_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().generate(*args)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
# from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.objectConfig.generator.StoreFileGenerator import StoreFileGenerator
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _TransformGeneratorUtil_instance() -> object:
    return TransformGeneratorUtil()

lazy_static(TransformGeneratorUtil, "instance", _TransformGeneratorUtil_instance)

