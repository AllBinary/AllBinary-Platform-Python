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
# package org.allbinary.logic.io

from __future__ import annotations



class DataOutputStreamFactory:
    instance: DataOutputStreamFactory = None
    

    @staticmethod
    def getInstance() -> DataOutputStreamFactory:
        return DataOutputStreamFactory.instance
    

    # throws Exception
    def getInstanceForAbFile(self, file: AbFile) -> AbDataOutputStream:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
        idFileOutputStream: AbFileOutputStream = AbFileOutputStream.createFromAbFile(file)
        idOutData: AbDataOutputStream = AbDataOutputStream(idFileOutputStream)
        return idOutData
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, filePath: str, fileName: str) -> AbDataOutputStream:
        from org.allbinary.logic.io.FileStreamFactory import FileStreamFactory
        from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
        fileStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
        fileOutputStream: AbFileOutputStream = fileStreamFactory.getFileOutputStreamInstance(filePath, fileName)
        idOutData: AbDataOutputStream = AbDataOutputStream(fileOutputStream)
        return idOutData
from org.allbinary.logic.io.file.AbFile import AbFile


DataOutputStreamFactory.instance = DataOutputStreamFactory()

