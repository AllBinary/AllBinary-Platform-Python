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
# package org.allbinary.business.user.modules.configuration

from __future__ import annotations

from org.allbinary.data.tree.dom.document.mapping.DomDocumentMappingInterface import DomDocumentMappingInterface


class UserConfigurationDomDocumentMapping(DomDocumentMappingInterface):

    def _init_fields(self) -> None:
        self.userConfigurationInterface: UserConfigurationInterface = None
    

    def __init__(self, userConfigurationInterface: UserConfigurationInterface) -> None:
        self._init_fields()
        self.userConfigurationInterface = userConfigurationInterface
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        from org.allbinary.business.user.modules.configuration.UserConfigurationView import UserConfigurationView
        document: Document = DomDocumentHelper.create()
        node: Node = UserConfigurationView(self.userConfigurationInterface).toXmlNode(document)
        document.appendChild(node)
        return document
    

    # throws Exception
    def toDomDocumentString(self) -> str:
        return XmlDocumentHelper.toString(self.toXmlDoc())
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


