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



class TransformGeneratorUtil:
    instance: TransformGeneratorUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> TransformGeneratorUtil:
        return TransformGeneratorUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def generate(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, ownerTransformInfoInterface: TransformInfoInterface) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate a view", self, "generate()", e)
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def generate(self, abeClientInformation: AbeClientInformationInterface, transformInfoDomNode: TransformInfoDomNode, ownerTransformInfoInterface: TransformInfoInterface) -> None:
        self.generate(abeClientInformation, transformInfoDomNode.getTransformInfoInterface(), ownerTransformInfoInterface)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.objectConfig.generator.StoreFileGenerator import StoreFileGenerator


TransformGeneratorUtil.instance = TransformGeneratorUtil()

