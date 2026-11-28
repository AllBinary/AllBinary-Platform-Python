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
# package org.allbinary.logic.io.file

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FileFactory:
    SINGLETON: FileFactory = None

    def _init_fields(self) -> None:
        if "context" not in vars(self): self.context: Context = None
    

    def __init__(self, context: Context) -> None:
        from android.content.Context import Context
        __class__._init_fields(self)
        self.context = context
    

    @staticmethod
    def getInstance_j0() -> FileFactory:
        return FileFactory.SINGLETON
    

    # throws Exception
    def isFile(self, path: str) -> bool:
        from java.io.FileNotFoundException import FileNotFoundException
        try:
            self.context.openFileInput(path)
            return True
        except FileNotFoundException as e:
            return False
    

    def getContext(self) -> Context:
        from android.content.Context import Context
        return self.context
    

    # throws Exception
    def getFile(self, filePath: str) -> AbFile:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return AbFile.createAbFileFromRawPath(filePath)
    

    # throws Exception
    def getInstance_j2(self, file: AbFile, childFilePath: str) -> AbFile:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return AbFile.createAbFileWithChild(file, childFilePath)

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.io.FileNotFoundException import FileNotFoundException
# from android.content.Context import Context
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil


def _FileFactory_SINGLETON() -> object:
    from org.allbinary.data.resource.ResourceUtil import ResourceUtil
    return FileFactory(ResourceUtil.getInstance().getContext())

lazy_static(FileFactory, "SINGLETON", _FileFactory_SINGLETON)

