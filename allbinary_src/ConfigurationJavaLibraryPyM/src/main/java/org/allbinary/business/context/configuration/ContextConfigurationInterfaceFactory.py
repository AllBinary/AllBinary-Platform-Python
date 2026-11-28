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

from java.lang.JavaRuntimeStatic import lazy_static


class ContextConfigurationInterfaceFactory:
    instance: ContextConfigurationInterfaceFactory = None
    

    @staticmethod
    def getInstance_j0() -> ContextConfigurationInterfaceFactory:
        return ContextConfigurationInterfaceFactory.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_1(self, document: Document) -> ContextConfigurationInterface:
        from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
        from org.allbinary.business.context.configuration.ContextConfigurationView import ContextConfigurationView
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        contextConfigurationData: ContextConfigurationData = ContextConfigurationData.getInstance()
        contextConfigurationNode: Node = DomSearchHelper.getNode(contextConfigurationData.NAME, document.getChildNodes())
        return ContextConfigurationView(contextConfigurationNode).getContextConfigurationInterface()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_2(self, contextName: str) -> ContextConfigurationInterface:
        from org.allbinary.business.context.configuration.ContextConfigurationPathUtil import ContextConfigurationPathUtil
        from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.w3c.dom.Document import Document
        abPath: AbPath = ContextConfigurationPathUtil.getAbPath(contextName)
        contextConfigurationData: ContextConfigurationData = ContextConfigurationData.getInstance()
        documentString: str = CryptFileReader(contextConfigurationData.UNCRYPTED_EXTENSION, contextConfigurationData.ENCRYPTED_EXTENSION).get(abPath)
        document: Document = DomDocumentHelper.create(documentString)
        return self.getInstance(document)

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "Document" for base in type(args[0]).__mro__)):
            return __class__.__dict__["getInstance_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["getInstance_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


def _ContextConfigurationInterfaceFactory_instance() -> object:
    return ContextConfigurationInterfaceFactory()

lazy_static(ContextConfigurationInterfaceFactory, "instance", _ContextConfigurationInterfaceFactory_instance)

