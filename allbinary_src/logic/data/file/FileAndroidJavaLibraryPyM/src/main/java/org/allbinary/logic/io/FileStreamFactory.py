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

    def _init_fields(self) -> None:
        self.context: object = None
    

    @staticmethod
    def getInstance() -> FileStreamFactory:
        from org.allbinary.data.resource.ResourceUtil import ResourceUtil
        from org.allbinary.logic.NullUtil import NullUtil
        if FileStreamFactory.SINGLETON == NullUtil.getInstance().NULL_OBJECT:
            FileStreamFactory.SINGLETON = FileStreamFactory(ResourceUtil.getInstance().getContext())
        return FileStreamFactory.SINGLETON
    

    def __init__(self, context: Context) -> None:
        from android.content.Context import Context
        self._init_fields()
        self.context = context
    

    # throws Exception
    def getFileInputStreamInstance(self, path: str, fileName: str) -> AbFileInputStream:
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        return AbFileInputStream(self.getContext().openFileInput(fileName))
    

    # throws Exception
    def getFileOutputStreamInstance(self, path: str, fileName: str) -> AbFileOutputStream:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        from android.content.Context import Context
        context: Context = self.getContext()
        context.deleteFile(fileName)
        return AbFileOutputStream(context.openFileOutput(fileName, 0))
    

    # throws Exception
    def delete(self, path: str, fileName: str) -> None:
        self.getContext().deleteFile(fileName)
    

    def getContext(self) -> Context:
        from android.content.Context import Context
        return self.context
# from android.content.Context import Context
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil
# from org.allbinary.logic.NullUtil import NullUtil


def _FileStreamFactory_SINGLETON() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(FileStreamFactory, "SINGLETON", _FileStreamFactory_SINGLETON)

