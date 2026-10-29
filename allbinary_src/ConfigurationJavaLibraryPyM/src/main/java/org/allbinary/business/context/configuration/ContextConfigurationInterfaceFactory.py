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
# package org.allbinary.business.context.configuration

from __future__ import annotations



class ContextConfigurationInterfaceFactory:
    instance: ContextConfigurationInterfaceFactory = None
    

    @staticmethod
    def getInstance() -> ContextConfigurationInterfaceFactory:
        return ContextConfigurationInterfaceFactory.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, document: Document) -> ContextConfigurationInterface:
        from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
        from org.allbinary.business.context.configuration.ContextConfigurationView import ContextConfigurationView
        contextConfigurationData: ContextConfigurationData = ContextConfigurationData.getInstance()
        contextConfigurationNode: Node = DomSearchHelper.getNode(contextConfigurationData.NAME, document.getChildNodes())
        return ContextConfigurationView(contextConfigurationNode).getContextConfigurationInterface()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, contextName: str) -> ContextConfigurationInterface:
        from org.allbinary.business.context.configuration.ContextConfigurationPathUtil import ContextConfigurationPathUtil
        from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
        abPath: AbPath = ContextConfigurationPathUtil.getAbPath(contextName)
        contextConfigurationData: ContextConfigurationData = ContextConfigurationData.getInstance()
        documentString: str = CryptFileReader(contextConfigurationData.UNCRYPTED_EXTENSION, contextConfigurationData.ENCRYPTED_EXTENSION).get(abPath)
        document: Document = DomDocumentHelper.create(documentString)
        return self.getInstance(document)
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.path.AbPath import AbPath
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


ContextConfigurationInterfaceFactory.instance = ContextConfigurationInterfaceFactory()

