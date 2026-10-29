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
# package tags

from __future__ import annotations

from tags.HelperTag import HelperTag


#and hidden field removal
class StoreWorkFlowTag(HelperTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.viewName: str = None
        self.viewFile: str = None
    

    def __init__(self) -> None:
        super().__init__(StoreTagWorkFlowHelperFactory())
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    def setName(self, value: str) -> None:
        self.viewName = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().NAME, self.viewName)
    

    # throws Exception
    def process(self) -> int:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.PROCESS)
            helperClass: type = type(self.getHelper())
            method: Method = helperClass.getMethod(self.commonStrings.PROCESS, None)
            result: int = method.invoke(self.getHelper(), None)
            return int(result)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
            raise e
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF(self.commonStrings.START, self, self.tagStrings.DO_START_TAG)
            self.setHelper()
            return self.process()
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from javax.servlet.jsp.JspTagException import JspTagException
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from taghelpers.StoreTagWorkFlowHelperFactory import StoreTagWorkFlowHelperFactory


