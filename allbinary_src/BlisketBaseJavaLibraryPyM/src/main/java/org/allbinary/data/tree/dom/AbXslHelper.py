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

from java.lang.JavaRuntimeStatic import lazy_static


class AbXslHelper:
    instance: AbXslHelper = None
    

    @staticmethod
    def getInstance() -> AbXslHelper:
        return AbXslHelper.instance
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j2_1(self, xslFile: AbFile, xmlFile: AbFile) -> str:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return self.translate(xslFile.getAbsolutePath(), xmlFile.getAbsolutePath())
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j2_2(self, xslPath: AbPath, xmlPath: AbPath) -> str:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.translate(xslPath.getPath(), xmlPath.getPath())
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j2_3(self, xsltFilePath: str, xmlFilePath: str) -> str:
        from org.allbinary.data.tree.dom.XslHelper import XslHelper
        from java.io.ByteArrayOutputStream import ByteArrayOutputStream
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(XslHelper.getInstance().translate(StreamSource(xsltFilePath), StreamSource(xmlFilePath), StreamResult(outputStream)))
        except Exception as e:
            raise e

    def translate(self, *args):
        if len(args) == 2 and True and (args[0] is None or any(base.__name__ == "AbFile" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "AbFile" for base in type(args[1]).__mro__)):
            return __class__.__dict__["translate_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 2 and True and (args[0] is None or any(base.__name__ == "AbPath" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "AbPath" for base in type(args[1]).__mro__)):
            return __class__.__dict__["translate_j2_2"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["translate_j2_3"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("translate_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().translate(*args)
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from javax.xml.transform.stream.StreamResult import StreamResult
# from javax.xml.transform.stream.StreamSource import StreamSource
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.path.AbPath import AbPath


def _AbXslHelper_instance() -> object:
    return AbXslHelper()

lazy_static(AbXslHelper, "instance", _AbXslHelper_instance)

