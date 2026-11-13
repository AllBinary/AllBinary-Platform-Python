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

from java.lang.JavaRuntimeStatic import lazy_static


class FileStreamFactory:
    SINGLETON: object = None
    

    @staticmethod
    def getInstance() -> FileStreamFactory:
        from org.allbinary.logic.NullUtil import NullUtil
        if FileStreamFactory.SINGLETON == NullUtil.getInstance().NULL_OBJECT:
            FileStreamFactory.SINGLETON = FileStreamFactory()
        return FileStreamFactory.SINGLETON
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def getFileInputStreamInstance(self, path: str, fileName: str) -> AbFileInputStream:
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        FILEABPATH: AbPath = AbPath(path, fileName)
        file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
        return AbFileInputStream.createFromAbFile(file)
    

    # throws Exception
    def getFileOutputStreamInstance(self, path: str, fileName: str) -> AbFileOutputStream:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        FILEABPATH: AbPath = AbPath(path, fileName)
        file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
        if file.exists():
            file.delete()
            file.createNewFile()
        return AbFileOutputStream.createFromAbFile(file)
    

    # throws Exception
    def delete(self, path: str, fileName: str) -> None:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        FILEABPATH: AbPath = AbPath(path, fileName)
        file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
        file.delete()
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.path.AbPath import AbPath


def _FileStreamFactory_SINGLETON() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(FileStreamFactory, "SINGLETON", _FileStreamFactory_SINGLETON)

