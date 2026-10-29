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
# package org.allbinary.data.tree.dom.document

from __future__ import annotations



class DocumentToNode:
    XMLROOT: str = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    XMLROOTSTART: str = "<?xml"
    XMLROOTEND: str = "?>"
    XMLJSPROOTSTART: str = "<jsp:root"
    XMLEND: str = ">"
    XMLJSPROOTENDSTART: str = "</jsp:root"
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def convertDocumentToNodeString(documentString: str) -> str:
        documentString = DocumentToNode.remove(documentString, DocumentToNode.XMLJSPROOTSTART, DocumentToNode.XMLEND)
        documentString = DocumentToNode.remove(documentString, DocumentToNode.XMLJSPROOTENDSTART, DocumentToNode.XMLEND)
        replaceXmlRoot: Replace = Replace(DocumentToNode.XMLROOT, StringUtil.getInstance().EMPTY_STRING)
        return replaceXmlRoot.all(documentString)
    

    @staticmethod
    def removeXmlDefinitionFromDocumentString(documentString: str) -> str:
        return DocumentToNode.remove(documentString, DocumentToNode.XMLROOTSTART, DocumentToNode.XMLROOTEND)
    

    @staticmethod
    def remove(documentString: str, start: str, end: str) -> str:
        startIndex: int = 0
        while ((startIndex := documentString.find(start))) != -1:
            if startIndex >= 0:
                endIndex: int = documentString.find(end, startIndex)
                if endIndex >= 0:
                    startString: str = documentString[0:startIndex]
                    resultString: str = documentString[endIndex + 1:]
                    return startString + resultString
        return documentString
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace


