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
# package taghelpers.transform.info

from __future__ import annotations

from admin.taghelpers.ModifyTable import ModifyTable


class TransformInfoRequestHelper(ModifyTable):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.transformInfoInterface: TransformInfoHttpInterface = None
    

    def __init__(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreNoManipulation import TransformInfoHttpStoreNoManipulation
        super().__init__()
        self._init_fields()
        self.transformInfoInterface = TransformInfoHttpStoreNoManipulation(propertiesHashMap, pageContext)
    

    def update(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Updated Successfully"
            hashMapData: HashMap = self.transformInfoInterface.toHashMap()
            TransformInfoEntityBuilder.getInstance().update(hashMapData)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update storefronts table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def insert(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Added TransformInfo Successfully"
            values: BasicArrayList = self.transformInfoInterface.toVector()
            TransformInfoEntityBuilder.getInstance().insert(values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to add storefronts table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Delete Successfully"
            TransformInfoEntityBuilder.getInstance().delete(self.transformInfoInterface.getKey())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to delete storefronts table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreNoManipulation import TransformInfoHttpStoreNoManipulation
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


