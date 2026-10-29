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
# package admin.tags

from __future__ import annotations

from admin.tags.TableTag import TableTag


class StoreFrontsTag(TableTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.setTagHelperFactory(StoreFrontsHelperFactory())
        self.setTagRequestHelperFactory(StoreFrontsRequestHelperFactory())
    

    # throws LicensingException
    def generateSelect(self) -> str:
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            method: Method = type(anyType).getMethod("generateSelect", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to generate storefronts select"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateSelect()", e)
            return error
    

    # throws LicensingException
    def install(self) -> str:
        try:
            anyType: object = self.getTagRequestHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            method: Method = type(anyType).getMethod("install", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to generate storefronts select"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateSelect()", e)
            return error
    

    # throws LicensingException
    def sendStoreCreatedEmails(self) -> str:
        try:
            anyType: object = self.getTagRequestHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            method: Method = type(anyType).getMethod("sendStoreCreatedEmails", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to send email"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "sendStoreCreatedEmails()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.isEnabled():
                if self.getCommand() is not None:
                    storeFrontData: StoreFrontData = StoreFrontData.getInstance()
                    if self.getCommand().compareTo(storeFrontData.SELECT) == 0:
                        self.pageContext.getOut().print_(self.generateSelect())
                    elif self.getCommand().compareTo(storeFrontData.INSTALL) == 0:
                        self.getPropertiesHashMap().put("current", self.getCurrent())
                        self.getPropertiesHashMap().put("total", self.getTotal())
                        if int(self.getCurrent()) == int(self.getTotal()):
                            return TagSupport.EVAL_BODY_INCLUDE
                        self.install()
                    elif self.getCommand().compareTo(storeFrontData.INSTALL_COMPLETE) == 0:
                        self.sendStoreCreatedEmails()
                    else:
                        return super().doStartTag()
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.tagext.TagSupport import TagSupport
from admin.taghelpers.StoreFrontsHelperFactory import StoreFrontsHelperFactory
from admin.taghelpers.StoreFrontsRequestHelperFactory import StoreFrontsRequestHelperFactory
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


