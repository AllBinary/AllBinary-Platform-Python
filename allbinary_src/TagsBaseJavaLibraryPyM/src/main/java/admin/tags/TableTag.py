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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from tags.PropertiesTag import PropertiesTag


@java_inherited_overloads
class TableTag(PropertiesTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("enabled", None)
        vars(self).setdefault("tagHelperFactoryInterface", None)
        vars(self).setdefault("tagRequestHelperFactoryInterface", None)
        vars(self).setdefault("requestObject", None)
        vars(self).setdefault("current", None)
        vars(self).setdefault("total", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "enabled" not in vars(self): self.enabled: str = None
        if "tagHelperFactoryInterface" not in vars(self): self.tagHelperFactoryInterface: TagHelperFactoryInterface = None
        if "tagRequestHelperFactoryInterface" not in vars(self): self.tagRequestHelperFactoryInterface: TagHelperFactoryInterface = None
        if "requestObject" not in vars(self): self.requestObject: object = None
        if "current" not in vars(self): self.current: int = None
        if "total" not in vars(self): self.total: int = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    def setIsSelected(self, enabled: str) -> None:
        self.enabled = enabled
    

    # throws Exception
    def isEnabled(self) -> bool:
        from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        if not (StringValidationUtil.getInstance().isEmpty(self.enabled)):
            if BooleanUtil.getInstance().getFromString(self.enabled) or ((self.enabled > "on") - (self.enabled < "on")) == 0:
                return True
        return False
    

    def setTagHelperFactory(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
        self.tagHelperFactoryInterface = tagHelperFactoryInterface
    

    def getTagHelperFactoryInterface(self) -> TagHelperFactoryInterface:
        from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
        return self.tagHelperFactoryInterface
    

    def setTagRequestHelperFactory(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
        self.tagRequestHelperFactoryInterface = tagHelperFactoryInterface
    

    def getTagRequestHelperFactoryInterface(self) -> TagHelperFactoryInterface:
        from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
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
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("drop", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to drop table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    # throws LicensingException
    def create(self) -> str:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("create", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to create table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    # throws LicensingException
    def restore(self) -> str:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("restore", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    # throws LicensingException
    def backup(self) -> str:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            anyType: object = self.getTagHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("backup", None)
            result: str = method.invoke(anyType, None)
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
    

    # throws LicensingException
    def insert(self) -> str:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            helperClass: type = type(self.requestObject)
            method: Method = helperClass.getMethod("insert", None)
            result: str = method.invoke(self.requestObject, None)
            return result
        except Exception as e:
            error: str = "Failed to insert"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    # throws LicensingException
    def delete(self) -> str:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            helperClass: type = type(self.requestObject)
            method: Method = helperClass.getMethod(self.commonStrings.delete, None)
            result: str = method.invoke(self.requestObject, None)
            return result
        except Exception as e:
            error: str = "Failed to delete"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    # throws LicensingException
    def update(self) -> str:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            helperClass: type = type(self.requestObject)
            method: Method = helperClass.getMethod("update", None)
            result: str = method.invoke(self.requestObject, None)
            return result
        except Exception as e:
            error: str = "Failed to update"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
                request: HttpServletRequest = self.pageContext.getRequest()
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("TableTag Helper: ")
                stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self.getTagHelperFactoryInterface())))
                stringBuffer.append(" Request URI: ")
                stringBuffer.append(request.getRequestURI())
                self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
            if self.getTagRequestHelperFactoryInterface() is not None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
                    self.logUtil.putF("TableTag RequestHelper: " + __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self.getTagRequestHelperFactoryInterface())), self, self.tagStrings.DO_START_TAG)
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
                    self.logUtil.putF("TableTag RequestHelper: null", self, self.tagStrings.DO_START_TAG)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("TableTag this.getCommand(): " + str(self.getCommand()), self, self.tagStrings.DO_START_TAG)
            if java_predicate(self, "isEnabled"):
                if self.getCommand() is not None:
                    if self.getCommand().compareTo(self.commonStrings.INSERT) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().INSERT_INTO) == 0 or self.getCommand().compareTo(self.commonStrings.DELETE) == 0 or self.getCommand().compareTo(self.commonStrings.UPDATE) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().UPDATE) == 0:
                        self.requestObject = self.getTagRequestHelperFactoryInterface().getInstance(self.getPropertiesHashMap(), self.pageContext)
                    if self.getCommand().compareTo(self.commonStrings.INSERT) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().INSERT_INTO) == 0:
                        self.insert()
                    elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                        self.delete()
                    elif self.getCommand().compareTo(self.commonStrings.UPDATE) == 0 or self.getCommand().compareTo(SqlStrings.getInstance().UPDATE) == 0:
                        self.update()
                    if self.getCommand().compareTo(GLOBALS2.BACKUP) == 0:
                        output: str = self.backup()
                        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(GLOBALS2.RESTORE) == 0:
                        self.getPropertiesHashMap().put("current", self.getCurrent())
                        self.getPropertiesHashMap().put("total", self.getTotal())
                        output: str = self.restore()
                        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(self.commonStrings.DROP) == 0:
                        output: str = self.drop()
                        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(self.commonStrings.CREATE) == 0:
                        output: str = self.create()
                        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                        return self.SKIP_BODY
                    elif self.getCommand().compareTo(self.commonStrings.INSERT) == 0:
                        output: str = self.insert()
                        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                    elif self.getCommand().compareTo(self.commonStrings.DELETE) == 0:
                        output: str = self.delete()
                        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                            self.pageContext.getOut().print_(output + "<br />")
                    elif self.getCommand().compareTo(self.commonStrings.UPDATE) == 0:
                        output: str = self.update()
                        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
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
# from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings
# from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


