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

from tags.PropertiesTag import PropertiesTag


class TableTag(PropertiesTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.enabled: str = None
        self.tagHelperFactoryInterface: TagHelperFactoryInterface = None
        self.tagRequestHelperFactoryInterface: TagHelperFactoryInterface = None
        self.requestObject: object = None
        self.current: int = None
        self.total: int = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    def setIsSelected(self, enabled: str) -> None:
        self.enabled = enabled
    

    # throws Exception
    def isEnabled(self) -> bool:
        if not StringValidationUtil.getInstance().isEmpty(self.enabled):
            if BooleanUtil.getInstance().getFromString(self.enabled) or ((self.enabled > "on") - (self.enabled < "on")) == 0:
                return True
        return False
    

    def setTagHelperFactory(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        self.tagHelperFactoryInterface = tagHelperFactoryInterface
    

    def getTagHelperFactoryInterface(self) -> TagHelperFactoryInterface:
        return self.tagHelperFactoryInterface
    

    def setTagRequestHelperFactory(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        self.tagRequestHelperFactoryInterface = tagHelperFactoryInterface
    

    def getTagRequestHelperFactoryInterface(self) -> TagHelperFactoryInterface:
        return self.tagRequestHelperFactoryInterface
    

    def setCurrent(self, current: int) -> None:
        self.current = current
    

    def getCurrent(self) -> int:
        return self.current
    

    def setTotal(self, total: int) -> None:
        self.total = total
    

    def getTotal(self) -> int:
        return self.total
    

    # throws LicensingException
    def drop(self) -> str:
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("drop", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to drop table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    # throws LicensingException
    def create(self) -> str:
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("create", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to create table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    # throws LicensingException
    def restore(self) -> str:
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("restore", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    # throws LicensingException
    def backup(self) -> str:
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("backup", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
    

    # throws LicensingException
    def insert(self) -> str:
        try:
            helperClass: type = type(self.requestObject)
            method: Method = helperClass.getMethod("insert", None)
            result: str = method.invoke(self.requestObject, None)
            return result
        except Exception as e:
            error: str = "Failed to insert"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    # throws LicensingException
    def delete(self) -> str:
        try:
            helperClass: type = type(self.requestObject)
            method: Method = helperClass.getMethod(self.commonStrings.delete, None)
            result: str = method.invoke(self.requestObject, None)
            return result
        except Exception as e:
            error: str = "Failed to delete"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    # throws LicensingException
    def update(self) -> str:
        try:
            helperClass: type = type(self.requestObject)
            method: Method = helperClass.getMethod("update", None)
            result: str = method.invoke(self.requestObject, None)
            return result
        except Exception as e:
            error: str = "Failed to update"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                request: HttpServletRequest = self.pageContext.getRequest()
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("TableTag Helper: ")
                stringBuffer.append(type(self.getTagHelperFactoryInterface()).__module__ + "." + type(self.getTagHelperFactoryInterface()).__qualname__)
                stringBuffer.append(" Request URI: ")
                stringBuffer.append(request.getRequestURI())
                self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
            if self.getTagRequestHelperFactoryInterface() is not None:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                    self.logUtil.putF("TableTag RequestHelper: " + type(self.getTagRequestHelperFactoryInterface()).__module__ + "." + type(self.getTagRequestHelperFactoryInterface()).__qualname__, self, self.tagStrings.DO_START_TAG)
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                    self.logUtil.putF("TableTag RequestHelper: null", self, self.tagStrings.DO_START_TAG)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("TableTag this.getCommand(): " + str(self.getCommand()), self, self.tagStrings.DO_START_TAG)
            if self.isEnabled():
                if self.getCommand() is not None:
                    if self.getCommand().compareTo(self.commonStrings.INSERT) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().INSERT_INTO) == 0 or self.getCommand().compareTo(self.commonStrings.DELETE) == 0 or self.getCommand().compareTo(self.commonStrings.UPDATE) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().UPDATE) == 0:
                        self.requestObject = self.getTagRequestHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
                    if self.getCommand().compareTo(self.commonStrings.INSERT) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().INSERT_INTO) == 0:
                        self.insert()
                    elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                        self.delete()
                    elif self.getCommand().compareTo(self.commonStrings.UPDATE) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().UPDATE) == 0:
                        self.update()
                    if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.BACKUP) == 0:
                        output: str = self.backup()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.RESTORE) == 0:
                        self.getPropertiesHashMap().put("current", self.getCurrent())
                        self.getPropertiesHashMap().put("total", self.getTotal())
                        output: str = self.restore()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(self.commonStrings.DROP) == 0:
                        output: str = self.drop()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(self.commonStrings.CREATE) == 0:
                        output: str = self.create()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(self.commonStrings.INSERT) == 0:
                        output: str = self.insert()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                    elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                        output: str = self.delete()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                    elif self.getCommand().compareTo(self.commonStrings.UPDATE) == 0:
                        output: str = self.update()
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
            return self.EVAL_BODY_INCLUDE
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings
from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


