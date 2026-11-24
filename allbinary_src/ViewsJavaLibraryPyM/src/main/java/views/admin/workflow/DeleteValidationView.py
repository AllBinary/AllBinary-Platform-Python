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
# package views.admin.workflow

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.workflow.WorkFlowView import WorkFlowView


class DeleteValidationView(*java_bases(WorkFlowView, ValidationComponentInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.workFlowName: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.workFlowName = self.getPageContext().getRequest().getParameter(WorkFlowData.getInstance().NAME)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Name: " + self.workFlowName, self, self.commonStrings.CONSTRUCTOR)
    

    def isValid(self) -> bool:
        from org.allbinary.data.tables.workflow.WorkFlowEntityFactory import WorkFlowEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if self.workFlowName is None:
                return False
            if WorkFlowEntityFactory.getInstance().create2().get(self.workFlowName, self.getWeblisketSession().getStoreName()) is None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("WorkFlow does not exist.", self, self.commonStrings.IS_VALID)
                return False
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from org.allbinary.data.tables.workflow.WorkFlowEntityFactory import WorkFlowEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.workFlowName is None:
                stringBuffer.append("WorkFlow name is invalid<br />")
            if WorkFlowEntityFactory.getInstance().create2().get(self.workFlowName, self.getWeblisketSession().getStoreName()) is None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("WorkFlow does not exist.", self, "validationInfo()")
                stringBuffer.append("WorkFlow does not exist<br />")
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return super().getTransformInfoInterface()
# from org.allbinary.data.tables.workflow.WorkFlowEntityFactory import WorkFlowEntityFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


