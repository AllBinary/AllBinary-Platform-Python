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
# package org.allbinary.logic.visual.transform.template.util

from __future__ import annotations



class TransformTemplateCustomizerUtil:
    instance: TransformTemplateCustomizerUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.CUSTOMIZER_NAME: str = None
        self.BODY_VIEWNAMEKEY: str = None
        self.TITLE_VIEWNAMEKEY: str = None
        self.GLOBALS_NEW: str = None
        self.GLOBALS_INSERT: str = None
        self.GLOBALS_DELETE: str = None
        self.GLOBALS_EDIT: str = None
        self.GLOBALS_UPDATE: str = None
    

    @staticmethod
    def getInstance() -> TransformTemplateCustomizerUtil:
        return TransformTemplateCustomizerUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        SPACE: str = CommonSeps.getInstance().SPACE
        self.CUSTOMIZER_NAME = SPACE + str(CustomizerTransformInfoData.NAME)
        self.BODY_VIEWNAMEKEY = SPACE + str(BodyData.getInstance().VIEWNAMEKEY)
        self.TITLE_VIEWNAMEKEY = SPACE + str(TitleData.getInstance().VIEWNAMEKEY)
        self.GLOBALS_NEW = str(self.GLOBALS2.NEW) + SPACE
        self.GLOBALS_INSERT = str(commonStrings.INSERT) + SPACE
        self.GLOBALS_DELETE = str(commonStrings.DELETE) + SPACE
        self.GLOBALS_EDIT = str(self.GLOBALS2.EDIT) + SPACE
        self.GLOBALS_UPDATE = str(commonStrings.UPDATE) + SPACE
    

    def getPageNameHack(self, viewName: str, storeName: str) -> str:
        SPACE: str = CommonSeps.getInstance().SPACE
        ONE_EMPTY_STRING_ARRAY: list[str] = StringUtil.getInstance().ONE_EMPTY_STRING_ARRAY
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put([viewName + SPACE], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([storeName + SPACE], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.CUSTOMIZER_NAME], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.BODY_VIEWNAMEKEY], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.TITLE_VIEWNAMEKEY], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.GLOBALS_NEW], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.GLOBALS_INSERT], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.GLOBALS_DELETE], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.GLOBALS_EDIT], ONE_EMPTY_STRING_ARRAY)
        hashMap.put([self.GLOBALS_UPDATE], ONE_EMPTY_STRING_ARRAY)
        replace: Replace = None
        rootViewName: str = replace.all(viewName)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("RootViewName for ObjectConfig: " + rootViewName, self, "getPageNameHack")
        return rootViewName
# from java.util.HashMap import HashMap
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.logic.visual.transform.info.CustomizerTransformInfoData import CustomizerTransformInfoData
from org.allbinary.logic.visual.transform.template.customizer.bodies.BodyData import BodyData
from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


TransformTemplateCustomizerUtil.instance = TransformTemplateCustomizerUtil()

