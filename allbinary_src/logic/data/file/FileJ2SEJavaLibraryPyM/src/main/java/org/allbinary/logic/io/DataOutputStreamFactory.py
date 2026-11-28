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


class DataOutputStreamFactory:
    instance: DataOutputStreamFactory = None
    

    @staticmethod
    def getInstance_j0() -> DataOutputStreamFactory:
        return DataOutputStreamFactory.instance
    

    # throws Exception
    def getInstanceForAbFile(self, file: AbFile) -> AbDataOutputStream:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
        from org.allbinary.logic.io.file.AbFile import AbFile
        idFileOutputStream: AbFileOutputStream = AbFileOutputStream.createFromAbFile(file)
        idOutData: AbDataOutputStream = AbDataOutputStream(idFileOutputStream)
        return idOutData
    

    # throws Exception
    def getInstance_j2(self, filePath: str, fileName: str) -> AbDataOutputStream:
        from org.allbinary.logic.io.FileStreamFactory import FileStreamFactory
        from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
        fileStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
        fileOutputStream: AbFileOutputStream = fileStreamFactory.getFileOutputStreamInstance(filePath, fileName)
        idOutData: AbDataOutputStream = AbDataOutputStream(fileOutputStream)
        return idOutData

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from org.allbinary.logic.io.file.AbFile import AbFile


def _DataOutputStreamFactory_instance() -> object:
    return DataOutputStreamFactory()

lazy_static(DataOutputStreamFactory, "instance", _DataOutputStreamFactory_instance)

