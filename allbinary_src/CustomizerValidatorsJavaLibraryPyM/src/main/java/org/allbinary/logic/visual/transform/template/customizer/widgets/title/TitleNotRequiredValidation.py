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
# package org.allbinary.logic.visual.transform.template.customizer.widgets.title

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleView import TitleView


@java_inherited_overloads
class TitleNotRequiredValidation(*java_bases(TitleView, ValidationInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def _constructor1_1(self, node: Node) -> None:
        __class__._java_defaults(self)
        from org.w3c.dom.Node import Node
        super().__init__(node)
        __class__._init_fields(self)
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        super().__init__(hashMap)
        __class__._init_fields(self)
    

    def isValid(self) -> bool:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            valid: bool = True
            if not (StringValidationUtil.getInstance().isValidNotRequired(self.getTitle(), 0, TitleData.getInstance().MAXLEN)):
                valid = False
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Title: ")
                stringBuffer.append(self.getTitle())
                stringBuffer.append("End: ")
                stringBuffer.appendboolean(valid)
                self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            return valid
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Title is not valid.")
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
# from java.util.HashMap import HashMap
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


