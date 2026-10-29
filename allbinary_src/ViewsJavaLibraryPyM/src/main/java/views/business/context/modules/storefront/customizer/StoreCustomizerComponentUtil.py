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
# package views.business.context.modules.storefront.customizer

from __future__ import annotations



class StoreCustomizerComponentUtil:
    instance: StoreCustomizerComponentUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> StoreCustomizerComponentUtil:
        return StoreCustomizerComponentUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def generate(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> str:
        from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Generating Modified Views For: " + transformInfoInterface.getName(), self, "generateModifiedViews()")
        customizerUtil: CustomizerUtil = CustomizerUtil.getInstance()
        allCustomizedViews: BasicArrayList = customizerUtil.getTransformInfoObjectConfigGroupComponentNodes(transformInfoInterface)
        size: int = allCustomizedViews.size()
        for index in range(0, size):
            nextTransformInfoInterface: TransformInfo = allCustomizedViews.get(index)
            allViewsToBeModified: BasicArrayList = customizerUtil.getTransformInfoObjectConfigComponentNodesToCustomize(transformInfoInterface, nextTransformInfoInterface)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("View or component that was modified by a Customizer: " + nextTransformInfoInterface.getName(), self, "generateModifiedViews()")
            self.generate(abeClientInformation, transformInfoInterface, allViewsToBeModified)
        return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def generate(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, allViewsToBeModifiedVector: BasicArrayList) -> None:
        from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil
        customizerUtil: CustomizerUtil = CustomizerUtil.getInstance()
        size: int = allViewsToBeModifiedVector.size()
        for index in range(0, size):
            nextTransformInfoInterface: TransformInfo = allViewsToBeModifiedVector.get(index)
            specifiedTransformInfoInterface: TransformInfoInterface = customizerUtil.getTransformInfoInterfaceToCustomize(transformInfoInterface, nextTransformInfoInterface)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Retrieved: " + specifiedTransformInfoInterface.getName(), self, "generateModifiedViews()")
            TransformGeneratorUtil.getInstance().generate(abeClientInformation, nextTransformInfoInterface, specifiedTransformInfoInterface)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.generator.TransformGeneratorUtil import TransformGeneratorUtil
from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


StoreCustomizerComponentUtil.instance = StoreCustomizerComponentUtil()

