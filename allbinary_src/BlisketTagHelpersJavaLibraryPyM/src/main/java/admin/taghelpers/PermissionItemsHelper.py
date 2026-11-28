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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.BasicTable import BasicTable


@java_inherited_overloads
class PermissionItemsHelper(BasicTable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("portion", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "portion" not in vars(self): self.portion: Portion = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.installer.Portion import Portion
        super().__init__()
        __class__._init_fields(self)
        self.portion = Portion(hashMap)
    

    def create(self) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.item.permissions.PermissionItemsEntityFactory import PermissionItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = PermissionItemsEntityFactory.getInstance().getPermissionItemsEntityInstance().createTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def drop(self) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.item.permissions.PermissionItemsEntityFactory import PermissionItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = PermissionItemsEntityFactory.getInstance().getPermissionItemsEntityInstance().dropTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop pricing tables"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def restore(self) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.item.permissions.PermissionItemsEntityFactory import PermissionItemsEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().restoreTable(PermissionItemsEntityFactory.getInstance().getPermissionItemsEntityInstance(), self.portion)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "restore()")
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    def backup(self) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.item.permissions.PermissionItemsEntityFactory import PermissionItemsEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Backup Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(PermissionItemsEntityFactory.getInstance().getPermissionItemsEntityInstance())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.installer.Portion import Portion
# from org.allbinary.data.tables.user.commerce.inventory.item.permissions.PermissionItemsEntityFactory import PermissionItemsEntityFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


