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

from org.allbinary.logic.NullUtil import NullUtil


class FileStreamFactory:
    SINGLETON: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getInstance() -> FileStreamFactory:
        if FileStreamFactory.SINGLETON == NullUtil.getInstance().NULL_OBJECT:
            FileStreamFactory.SINGLETON = FileStreamFactory()
        return FileStreamFactory.SINGLETON
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def getFileInputStreamInstance(self, path: str, fileName: str) -> AbFileInputStream:
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        FILEABPATH: AbPath = AbPath(path, fileName)
        file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
        return AbFileInputStream(file)
    

    # throws Exception
    def getFileOutputStreamInstance(self, path: str, fileName: str) -> AbFileOutputStream:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        FILEABPATH: AbPath = AbPath(path, fileName)
        file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
        if file.exists():
            file.delete()
            file.createNewFile()
        return AbFileOutputStream.createFromAbFile(file)
    

    # throws Exception
    def delete(self, path: str, fileName: str) -> None:
        FILEABPATH: AbPath = AbPath(path, fileName)
        file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
        file.delete()
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPath import AbPath


