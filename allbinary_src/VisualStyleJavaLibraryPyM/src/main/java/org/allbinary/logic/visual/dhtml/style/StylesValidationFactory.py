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
# package org.allbinary.logic.visual.dhtml.style

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class StylesValidationFactory:
    instance: StylesValidationFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> StylesValidationFactory:
        return StylesValidationFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_1(self, document: Document) -> BasicArrayList:
        from org.allbinary.logic.visual.dhtml.style.StylesData import StylesData
        from org.allbinary.logic.visual.dhtml.style.StyleData import StyleData
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.logic.visual.dhtml.style.css.CssElementData import CssElementData
        from org.allbinary.logic.visual.dhtml.style.css.CssElementsValidationFactory import CssElementsValidationFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        commonStrings: CommonStrings = CommonStrings.getInstance()
        nodeList: NodeList = document.getElementsByTagName(StylesData.getInstance().NAME)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Style Present: " + XmlDocumentHelper.toString(document), self, commonStrings.GET_INSTANCE)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Styles Present: " + str(nodeList.getLength()), self, commonStrings.GET_INSTANCE)
        for index in range(0, nodeList.getLength()):
            stylesNode: Node = nodeList.item(index)
            styleNodeList: BasicArrayList = DomSearchHelper.getAllNodes(StyleData.getInstance().NAME, stylesNode.getChildNodes())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Number Of Style Nodes Present: " + str(styleNodeList.size()), self, commonStrings.GET_INSTANCE)
            for styleNodesIndex in range(0, styleNodeList.size()):
                styleNode: Node = styleNodeList.get(styleNodesIndex)
                cssElementStyleNodeList: BasicArrayList = DomSearchHelper.getAllNodes(CssElementData.getInstance().NAME, styleNode.getChildNodes())
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Number Of Element Nodes Present: " + str(cssElementStyleNodeList.size()), self, commonStrings.GET_INSTANCE)
                return CssElementsValidationFactory.getInstance(cssElementStyleNodeList)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("No Style Present", self, commonStrings.GET_INSTANCE)
        return BasicArrayListD()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def getInstance_j1_2(hashMap: HashMap) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.w3c.dom.Document import Document
        stylesDocument: Document = hashMap.get(NameSpaceRequestParamData.DOCUMENT)
        return StylesValidationFactory.getInstance_j0()
            .getInstance(stylesDocument)

    def getInstance(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)):
            return __class__.__dict__["getInstance_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["getInstance_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.visual.dhtml.style.css.CssElementData import CssElementData
# from org.allbinary.logic.visual.dhtml.style.css.CssElementsValidationFactory import CssElementsValidationFactory
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _StylesValidationFactory_instance() -> object:
    return StylesValidationFactory()

lazy_static(StylesValidationFactory, "instance", _StylesValidationFactory_instance)

