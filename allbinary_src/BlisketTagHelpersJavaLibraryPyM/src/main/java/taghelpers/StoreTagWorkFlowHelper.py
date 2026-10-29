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
# package taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelper import TagHelper


class StoreTagWorkFlowHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.storeWorkFlowInterface: StoreWorkFlowInterface = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
            self.logUtil.putF("Properties: " + str(hashMap), self, "StoreTagWorkFlowHelper()")
        self.storeWorkFlowInterface = StoreTagWorkFlowFactory.getInstance().getInstance(self.abeClientInformation, hashMap, pageContext)
    

    # throws Exception
    def process(self) -> int:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF("Process", self, self.commonStrings.PROCESS)
            return self.storeWorkFlowInterface.process()
        except Exception as e:
            error: str = "Failed to process workflow: "
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.workflow.StoreTagWorkFlowFactory import StoreTagWorkFlowFactory
from org.allbinary.logic.control.workflow.StoreWorkFlowInterface import StoreWorkFlowInterface
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


