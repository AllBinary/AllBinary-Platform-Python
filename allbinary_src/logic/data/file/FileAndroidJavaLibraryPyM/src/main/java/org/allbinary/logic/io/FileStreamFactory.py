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

    def _init_fields(self) -> None:
        self.context: object = None
    

    @staticmethod
    def getInstance() -> FileStreamFactory:
        if FileStreamFactory.SINGLETON == NullUtil.getInstance().NULL_OBJECT:
            FileStreamFactory.SINGLETON = FileStreamFactory(ResourceUtil.getInstance().getContext())
        return FileStreamFactory.SINGLETON
    

    def __init__(self, context: Context) -> None:
        self._init_fields()
        self.context = context
    

    # throws Exception
    def getFileInputStreamInstance(self, path: str, fileName: str) -> AbFileInputStream:
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        return AbFileInputStream(self.getContext().openFileInput(fileName))
    

    # throws Exception
    def getFileOutputStreamInstance(self, path: str, fileName: str) -> AbFileOutputStream:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        context: Context = self.getContext()
        context.deleteFile(fileName)
        return AbFileOutputStream(context.openFileOutput(fileName, 0))
    

    # throws Exception
    def delete(self, path: str, fileName: str) -> None:
        self.getContext().deleteFile(fileName)
    

    def getContext(self) -> Context:
        return self.context
from android.content.Context import Context
from org.allbinary.data.resource.ResourceUtil import ResourceUtil


