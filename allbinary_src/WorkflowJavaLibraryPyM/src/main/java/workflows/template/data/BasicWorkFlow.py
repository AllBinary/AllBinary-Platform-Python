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

from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface


class BasicWorkFlow(WorkFlowInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.validationDomNodeInterface: ValidationComponentInterface = None
        self.propertiesHashMap: dict = None
        self.pageContext: PageContext = None
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().WORKFLOW):
            self.logUtil.putF("Properties: " + str(propertiesHashMap), self, "BasicWorkFlow()")
        self.propertiesHashMap = propertiesHashMap
        self.pageContext = pageContext
        self.validationDomNodeInterface = TransformFactory.getInstance().getInstance(self.abeClientInformation, propertiesHashMap, pageContext)
    

    # throws Exception
    def getName(self) -> str:
        return self.getPropertiesHashMap().get(WorkFlowData.getInstance().NAME)
    

    def getPropertiesHashMap(self) -> dict:
        return self.propertiesHashMap
    

    def getPageContext(self) -> PageContext:
        return self.pageContext
    

    # throws Exception
    def process(self) -> int:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().WORKFLOW):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.PROCESS)
        if self.validationDomNodeInterface.isValid():
            self.pageContext.getOut().print_(self.validationDomNodeInterface.view())
            return str(TagSupport.EVAL_BODY_INCLUDE)
        else:
            self.pageContext.getOut().print_(self.validationDomNodeInterface.validationInfo())
            return str(TagSupport.SKIP_BODY)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from javax.servlet.jsp.tagext.TagSupport import TagSupport
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
from org.allbinary.string.CommonStrings import CommonStrings


