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
# package views.generic.address

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class StatesView(DomNodeInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.LineReader import LineReader
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            node: Node = document.createElement(StreetAddressData.STATES)
            statesFile: str = str(URLGLOBALS.getMainPath() + FREEBLISKET_PATH_GLOBALS.getInstance().LINEDATAPATH) + "states.txt"
            lineReader: LineReader = LineReader(statesFile)
            while java_predicate(lineReader, "hasNext"):
                option: str = lineReader.next()
                node.appendChild(ModDomHelper.createNameValueNodes(document, StreetAddressData.STATE, option))
            return node
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
# from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.LineReader import LineReader
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


