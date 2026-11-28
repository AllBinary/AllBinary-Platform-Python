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
# package org.allbinary.data.tables.category

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.category.CategoryEntityInterface import CategoryEntityInterface


@java_inherited_overloads
class CategoryEntity(*java_bases(AbSqlBean, CategoryEntityInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("tableName", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "categories"

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)
    

    def _constructor1(self, categoryFactoryInterface: CategoryFactoryInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
        from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
        super().__init__(InventoryDbInitInfo())
        __class__._init_fields(self)
        self.setTableName(self.tableName)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
        super().__init__(InventoryDbInitInfo())
        __class__._init_fields(self)
        self.setTableName(self.tableName)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def insert_j1_1(self, category: Category) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.category.Category import Category
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryVector: BasicArrayList = category.toVector()
            values: BasicArrayList = BasicArrayListD()
            values.add(categoryVector.get(0))
            values.add(categoryVector.get(1))
            java_super_call(super(), "insert", values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def delete(self, value: str) -> None:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            java_super_call(super(), "deleteWhere", CategoryData.getInstance().NAME, value)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(CategoryData.getInstance().NAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(CategoryData.getInstance().LEVEL)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(self.sqlStrings.PRIMARY_KEY)
        stringBuffer.append(CategoryData.getInstance().NAME)
        stringBuffer.append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return java_super_call(super(), "createTable", self.createTableStatement())
    

    def update(self, updatedValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryData import CategoryData
        java_super_call(super(), "updateWhere", CategoryData.getInstance().NAME, updatedValues.get(CategoryData.getInstance().NAME), updatedValues)
    

    def dropTable(self) -> str:
        return java_super_call(super(), "dropTable")
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def insert_j1_2(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        java_super_call(super(), "insert", values)

    def insert(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "Category" for base in type(args[0]).__mro__)):
            return __class__.__dict__["insert_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["insert_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("insert_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().insert(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.category.Category import Category
# from org.allbinary.business.category.CategoryData import CategoryData
# from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
# from org.allbinary.business.init.db.InventoryDbInitInfo import InventoryDbInitInfo
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


