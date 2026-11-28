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

from java.lang.JavaRuntimeStatic import lazy_static


class StoreCustomizerComponentUtil:
    instance: StoreCustomizerComponentUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> StoreCustomizerComponentUtil:
        return StoreCustomizerComponentUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def generate_j2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> str:
        from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Generating Modified Views For: " + transformInfoInterface.getName(), self, "generateModifiedViews()")
        customizerUtil: CustomizerUtil = CustomizerUtil.getInstance()
        allCustomizedViews: BasicArrayList = customizerUtil.getTransformInfoObjectConfigGroupComponentNodes(transformInfoInterface)
        size: int = allCustomizedViews.size()
        for index in range(0, size):
            nextTransformInfoInterface: TransformInfo = allCustomizedViews.get(index)
            allViewsToBeModified: BasicArrayList = customizerUtil.getTransformInfoObjectConfigComponentNodesToCustomize(transformInfoInterface, nextTransformInfoInterface)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("View or component that was modified by a Customizer: " + nextTransformInfoInterface.getName(), self, "generateModifiedViews()")
            self.generate(abeClientInformation, transformInfoInterface, allViewsToBeModified)
        return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    def generate_j3(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, allViewsToBeModifiedVector: BasicArrayList) -> None:
        from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.generator.TransformGeneratorUtil import TransformGeneratorUtil
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        customizerUtil: CustomizerUtil = CustomizerUtil.getInstance()
        size: int = allViewsToBeModifiedVector.size()
        for index in range(0, size):
            nextTransformInfoInterface: TransformInfo = allViewsToBeModifiedVector.get(index)
            specifiedTransformInfoInterface: TransformInfoInterface = customizerUtil.getTransformInfoInterfaceToCustomize(transformInfoInterface, nextTransformInfoInterface)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Retrieved: " + specifiedTransformInfoInterface.getName(), self, "generateModifiedViews()")
            TransformGeneratorUtil.getInstance().generate(abeClientInformation, nextTransformInfoInterface, specifiedTransformInfoInterface)

    def generate(self, *args):
        implementation = __class__.__dict__.get("generate_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().generate(*args)
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.visual.transform.generator.TransformGeneratorUtil import TransformGeneratorUtil
# from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _StoreCustomizerComponentUtil_instance() -> object:
    return StoreCustomizerComponentUtil()

lazy_static(StoreCustomizerComponentUtil, "instance", _StoreCustomizerComponentUtil_instance)

