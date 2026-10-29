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



class DomDocumentFileHelper:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def createDocument(xmlFile: AbFile) -> Document:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        try:
            return DomDocumentHelper.create(AbFileInputStream(xmlFile))
        except Exception as e:
            raise e
    

    # throws Exception
    @staticmethod
    def save(file: AbFile, document: Document) -> None:
        dataOutputStream: AbDataOutputStream = None
        try:
            copyTransformerFactory: TransformerFactory = TransformerFactory.newInstance()
            copyTransformer: Transformer = copyTransformerFactory.newTransformer()
            domSource: DOMSource = DOMSource(document)
            if file.isFile():
                file.delete()
            file.createNewFile()
            dataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(file)
            streamResult: StreamResult = StreamResult(dataOutputStream)
            copyTransformer.transform(domSource, streamResult)
            dataOutputStream.flush()
        except Exception as e:
            raise e
        finally:
            StreamUtil.getInstance().close(dataOutputStream)
# from javax.xml.transform.Transformer import Transformer
# from javax.xml.transform.TransformerFactory import TransformerFactory
# from javax.xml.transform.dom.DOMSource import DOMSource
# from javax.xml.transform.stream.StreamResult import StreamResult
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.w3c.dom.Document import Document


