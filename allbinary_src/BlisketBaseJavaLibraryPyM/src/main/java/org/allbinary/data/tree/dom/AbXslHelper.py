#
# AllBinary Open License Version 1
# Copyright (c) 2022 AllBinary
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



class AbXslHelper:
    instance: AbXslHelper = None
    

    @staticmethod
    def getInstance() -> AbXslHelper:
        return AbXslHelper.instance
    

    # throws Exception
    def translate(self, xslFile: AbFile, xmlFile: AbFile) -> str:
        return self.translate(xslFile.getAbsolutePath(), xmlFile.getAbsolutePath())
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def translate(self, xslPath: AbPath, xmlPath: AbPath) -> str:
        return self.translate(xslPath.getPath(), xmlPath.getPath())
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def translate(self, xsltFilePath: str, xmlFilePath: str) -> str:
        from org.allbinary.data.tree.dom.XslHelper import XslHelper
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(XslHelper.getInstance().translate(StreamSource(xsltFilePath), StreamSource(xmlFilePath), StreamResult(outputStream)))
        except Exception as e:
            raise e
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from javax.xml.transform.stream.StreamResult import StreamResult
# from javax.xml.transform.stream.StreamSource import StreamSource
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPath import AbPath


AbXslHelper.instance = AbXslHelper()

