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

from org.allbinary.logic.control.workflow.StoreWorkFlowInterface import StoreWorkFlowInterface
from workflows.template.data.BasicWorkFlow import BasicWorkFlow


class BasicStoreWorkFlow(BasicWorkFlow, StoreWorkFlowInterface):
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__(propertiesHashMap, pageContext)
    

    # throws Exception
    def getStoreName(self) -> str:
        return self.getPropertiesHashMap().get(StoreFrontData.getInstance().NAME)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData


