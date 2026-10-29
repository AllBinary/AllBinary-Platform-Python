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



class TransformsGeneratorUtil:
    instance: TransformsGeneratorUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> TransformsGeneratorUtil:
        return TransformsGeneratorUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def generateComponentsFromObjectConfig(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, group: str) -> str:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Started Group: " + group, self, "generateComponentsFromObjectConfig(2)")
        transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface = transformInfoInterface.getObjectConfigInterface()
        result: str = self.generateComponentsFromObjectConfig(abeClientInformation, transformInfoObjectConfigInterface, transformInfoInterface, group)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("End Group: " + group, self, "generateComponentsFromObjectConfig(2)")
        return result
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def generateComponentsFromObjectConfig(self, abeClientInformation: AbeClientInformationInterface, transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface, transformInfoInterface: TransformInfoInterface, group: str) -> str:
        from org.allbinary.logic.visual.transform.generator.TransformGeneratorUtil import TransformGeneratorUtil
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Started Group: " + group, self, "generateComponentsFromObjectConfig()")
        transformInfoObjectConfigComponentVector: BasicArrayList = transformInfoObjectConfigInterface.getTransformsGroup(group)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Processing ")
            stringBuffer.appendint(transformInfoObjectConfigComponentVector.size())
            stringBuffer.append(" Components Group: ")
            stringBuffer.append(group)
            self.logUtil.putF(str(stringBuffer), self, "generateComponentsFromObjectConfig()")
        if transformInfoObjectConfigComponentVector.size() < 1:
            raise Exception("No Pages Generated For Template.")
        size: int = transformInfoObjectConfigComponentVector.size()
        for index in range(0, size):
            transformInfoObjectConfigComponent: TransformInfoDomNode = transformInfoObjectConfigComponentVector.get(index)
            TransformGeneratorUtil.getInstance().generate(abeClientInformation, transformInfoObjectConfigComponent, transformInfoInterface)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Done Group: " + group, self, "generateComponentsFromObjectConfig()")
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("<!-- Generated all template views successfully for View: ")
        stringBuffer.append(transformInfoInterface.getName())
        stringBuffer.append("-->")
        return str(stringBuffer)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface


TransformsGeneratorUtil.instance = TransformsGeneratorUtil()

