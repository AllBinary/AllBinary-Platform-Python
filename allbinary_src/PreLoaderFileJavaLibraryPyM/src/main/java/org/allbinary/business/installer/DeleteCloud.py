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
# package org.allbinary.business.installer

from __future__ import annotations



class DeleteCloud:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def delete(self, prePath: str, current: int, total: int) -> bool:
        try:
            if AbIOSystem.getInstance().isType("com.vobject.appengine.java.io"):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append(self.URLGLOBALS.getWebappPath())
                stringBuffer.append(prePath)
                path: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
                file: AbFile = AbFile.createAbFileFromAbPath(path)
                fileBasicArrayList: BasicArrayList = Directory.getInstance().search(file, True)
                size: int = fileBasicArrayList.size()
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append("Searched: ")
                stringBuffer.append(path.toFileSystemString())
                stringBuffer.append(" BasicArrayList: ")
                stringBuffer.appendint(size)
                portion: int = int(size / total) + 1
                start: int = portion * current
                end: int = start + portion
                if end > size:
                    end = size
                stringBuffer.append(" Section: ")
                stringBuffer.appendint(start)
                stringBuffer.append(" - ")
                stringBuffer.appendint(end)
                self.logUtil.putF(str(stringBuffer), self, "initialize()")
                nextFile: AbFile = None
                for index in range(start, end):
                    nextFile = fileBasicArrayList.get(index)
                    try:
                        if nextFile.getPath().indexOf(FileUploadData.getInstance().FILE) < 0:
                            nextFile.delete()
                    except Exception as e:
                        pass
                self.logUtil.putF("Deleted Files From Cloud", self, "initialize()")
            return True
        except Exception as e:
            self.logUtil.put("Unable to copy installer files into cloud", self, "initialize()", e)
            return False
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.http.file.upload.FileUploadData import FileUploadData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbIOSystem import AbIOSystem
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList


