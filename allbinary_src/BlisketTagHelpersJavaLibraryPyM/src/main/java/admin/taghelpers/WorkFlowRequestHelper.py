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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.ModifyTable import ModifyTable


class WorkFlowRequestHelper(ModifyTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.workFlowInterface: WorkFlowInterface = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.workFlowInterface = NewWorkFlowFactory.getInstance().getInstance(self.abeClientInformation, hashMap, pageContext)
    

    # throws Exception
    def delete(self) -> str:
        try:
            stringUtil: StringUtil = StringUtil.getInstance()
            WorkFlowEntityFactory.getInstance().create2().delete(self.workFlowInterface.getName(), stringUtil.EMPTY_STRING)
            success: str = "Successfully Removed the workflow with " + str(WorkFlowData.getInstance().NAME) + "= " + self.workFlowInterface.getName() + " from "
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            try:
                error: str = "Failed to remove workflow with " + str(WorkFlowData.getInstance().NAME) + "= " + self.workFlowInterface.getName() + " from "
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                    self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
                raise Exception(e)
            except Exception as e2:
                error: str = "Failed to get data from workflowinterface to set error string"
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                    self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e2)
                return error
    

    def insert(self) -> str:
        try:
            success: str = "New User Successfully added to the Users Table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "add()")
            return success
        except Exception as e:
            error: str = "Failed to add User"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "add()", e)
            return error
    

    def update(self) -> str:
        try:
            success: str = "Updated WorkFlow Successfully"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update WorkFlow"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.data.tables.workflow.WorkFlowEntityFactory import WorkFlowEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.workflow.NewWorkFlowFactory import NewWorkFlowFactory
from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


