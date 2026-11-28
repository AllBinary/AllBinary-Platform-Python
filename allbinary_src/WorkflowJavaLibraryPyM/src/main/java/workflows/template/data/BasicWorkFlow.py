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
# package workflows.template.data

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface


class BasicWorkFlow(WorkFlowInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        if "validationDomNodeInterface" not in vars(self): self.validationDomNodeInterface: ValidationComponentInterface = None
        if "propertiesHashMap" not in vars(self): self.propertiesHashMap: HashMap = None
        if "pageContext" not in vars(self): self.pageContext: PageContext = None
    

    def __init__(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
        from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().WORKFLOW):
            self.logUtil.putF("Properties: " + str(propertiesHashMap), self, "BasicWorkFlow()")
        self.propertiesHashMap = propertiesHashMap
        self.pageContext = pageContext
        self.validationDomNodeInterface = TransformFactory.getInstance().getInstance(self.abeClientInformation, propertiesHashMap, pageContext)
    

    # throws Exception
    def getName(self) -> str:
        from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
        return self.getPropertiesHashMap().get(WorkFlowData.getInstance().NAME)
    

    def getPropertiesHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.propertiesHashMap
    

    def getPageContext(self) -> PageContext:
        return self.pageContext
    

    # throws Exception
    def process(self) -> int:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().WORKFLOW):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.PROCESS)
        if java_predicate(self.validationDomNodeInterface, "isValid"):
            self.pageContext.getOut().print_(self.validationDomNodeInterface.view())
            return str(TagSupport.EVAL_BODY_INCLUDE)
        else:
            self.pageContext.getOut().print_(self.validationDomNodeInterface.validationInfo())
            return str(TagSupport.SKIP_BODY)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from javax.servlet.jsp.tagext.TagSupport import TagSupport
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
# from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
# from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


