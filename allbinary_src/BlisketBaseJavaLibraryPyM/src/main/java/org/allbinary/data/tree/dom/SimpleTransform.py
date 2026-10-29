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



class SimpleTransform:

    def _init_fields(self) -> None:
        self.xsltFilePath: AbPath = None
        self.dataFilePath: AbPath = None
    

    def __init__(self, xsltFilePath: AbPath, dataFilePath: AbPath) -> None:
        self._init_fields()
        self.xsltFilePath = xsltFilePath
        self.dataFilePath = dataFilePath
    

    # throws Exception
    def transform(self) -> str:
        from org.allbinary.data.tree.dom.XslHelper import XslHelper
        inputStream: AbFileLocalInputStream = AbFileLocalInputStream(AbFile.createAbFileFromAbPath(self.xsltFilePath))
        document: Document = DomDocumentHelper.create(AbFileLocalInputStream(AbFile.createAbFileFromAbPath(self.dataFilePath)))
        result: str = XslHelper.getInstance().translate(StreamSource(inputStream), StreamSource(StringBufferInputStream(XmlDocumentHelper.toString(document))))
        return result
# from java.io.StringBufferInputStream import StringBufferInputStream
# from javax.xml.transform.stream.StreamSource import StreamSource
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPath import AbPath
from org.w3c.dom.Document import Document


