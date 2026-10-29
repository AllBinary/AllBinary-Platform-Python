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


class CategoryTag(TableTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.xsl: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.setTagHelperFactory(CategoryHelperFactory())
        self.setTagRequestHelperFactory(CategoryRequestHelperFactory())
    

    def setXsl(self, value: str) -> None:
        self.xsl = value
    

    # throws LicensingException
    def viewCategory(self) -> str:
        try:
            anyType: object = CategoryRequestHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            helperClass: type = type(anyType)
            method: Method = helperClass.getMethod("viewCategory", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to view a Category"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "viewCategory()", e)
            return error
    

    # throws LicensingException
    def viewCategories(self) -> str:
        try:
            anyType: object = CategoryRequestHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            helperClass: type = type(anyType)
            method: Method = helperClass.getMethod("viewCategories", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to view a Categories"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "viewCategories()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.isEnabled():
                if self.getCommand() is not None:
                    self.getPropertiesHashMap().put(TransformInfoData.getInstance().TEMPLATEFILENAME, self.xsl)
                    if self.getCommand().compareTo(CategoryData.getInstance().VIEW) == 0:
                        output: str = self.viewCategory()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output)
                    elif self.getCommand().compareTo(CategoryData.getInstance().VIEW) == 0:
                        output: str = self.viewCategories()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output)
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
from admin.taghelpers.CategoryHelperFactory import CategoryHelperFactory
from admin.taghelpers.CategoryRequestHelperFactory import CategoryRequestHelperFactory
from org.allbinary.business.category.CategoryData import CategoryData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData


