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
    instance: FileFactory = None
    

    @staticmethod
    def getInstance_j0() -> FileFactory:
        return FileFactory.instance
    

    # throws Exception
    def getInstance_j1(self, filePath: str) -> AbFile:
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
    

    # throws Exception
    def isFile(self, path: str) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        file: AbFile = AbFile.createAbFile(path)
        if file.exists():
            return True
        else:
            return False


def _FileFactory_instance() -> object:
    return FileFactory()

lazy_static(FileFactory, "instance", _FileFactory_instance)

