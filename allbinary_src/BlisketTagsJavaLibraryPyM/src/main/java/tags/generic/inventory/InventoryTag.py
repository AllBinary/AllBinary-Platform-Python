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
# package tags.generic.inventory

from __future__ import annotations

from tags.StoreValidationTransformTag import StoreValidationTransformTag


class InventoryTag(StoreValidationTransformTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws LicensingException
    def search(self) -> None:
        try:
            anyType: object = InventoryHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("search", None)
            result: str = method.invoke(anyType, None)
            self.pageContext.getOut().print_(result)
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to search Inventory by keyword"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "search()", e)
            try:
                self.pageContext.getOut().print_(error + "<br>")
                self.pageContext.getOut().print_("Exception: " + str(e) + "<br>")
            except Exception as e2:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LICENSINGERROR):
                    self.logUtil.put("Exception in Exception Handling", self, "search()", e)
    

    # throws LicensingException
    def viewSummary(self) -> None:
        try:
            anyType: object = InventoryHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            helperClass: type = type(anyType)
            method: Method = helperClass.getMethod("viewSummary", None)
            result: str = method.invoke(anyType, None)
            self.pageContext.getOut().print_(result)
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to View Summary"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "viewSummary()", e)
            try:
                self.pageContext.getOut().print_(error + "<br>")
                self.pageContext.getOut().print_("Exception: " + str(e) + "<br>")
            except Exception as e2:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LICENSINGERROR):
                    self.logUtil.put("Exception in Exception Handling", self, "viewSummary())", e)
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.getCommand() is not None:
                if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.SEARCH) == 0:
                    self.setName("Basic Search Inventory View")
                    self.setObjectFile("views.generic.inventory.AutoSearchValidationInventoryView")
                    self.search()
                    return self.EVAL_BODY_INCLUDE
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.VIEWSUMMARY) == 0:
                    self.setName("Basic Inventory View")
                    self.setObjectFile("views.generic.inventory.AutoValidationInventoryView")
                    self.viewSummary()
                    return self.EVAL_BODY_INCLUDE
                elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.VIEW) == 0:
                    self.setName("Basic Inventory View")
                    self.setObjectFile("views.generic.inventory.AutoValidationInventoryView")
                    return super().doStartTag()
                else:
                    raise Exception("No Such View Command: " + str(self.getCommand()))
            raise Exception("Command Null")
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
from taghelpers.InventoryHelperFactory import InventoryHelperFactory


