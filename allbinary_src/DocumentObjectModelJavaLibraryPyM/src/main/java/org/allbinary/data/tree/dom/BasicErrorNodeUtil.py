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
# package org.allbinary.data.tree.dom

from __future__ import annotations



class BasicErrorNodeUtil:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def get(document: Document, errorText: str) -> Node:
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        try:
            node: Node = document.createElement(ErrorData.getInstance().NAME)
            node.appendChild(ModDomHelper.createNameValueNodes(document, ErrorData.getInstance().TEXT, errorText))
            return node
        except Exception as e:
            raise Exception("Error Node Creation Failure")
from org.allbinary.business.error.ErrorData import ErrorData
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


