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
# package org.allbinary.logic.visual.transform.template.customizer.widgets.logo

from __future__ import annotations



class LogoImageFileUtil:

    def _init_fields(self) -> None:
        self.directory: Directory = Directory.getInstance()
        self.fileName: str = None
        self.imageFileAbPath: AbPath = None
    

    def __init__(self, imageAbPath: AbPath, imageFile: str) -> None:
        self._init_fields()
        self.fileName = imageFile
        self.imageFileAbPath = imageAbPath
    

    # throws Exception
    def saveFiles(self, fileItem: FileItem) -> None:
        if self.fileName is None:
            raise Exception("Image File Name Was Null")
        if not self.directory.create(self.imageFileAbPath):
            raise Exception("Unable to save file to non creatable directory")
        originalImageFile: AbFile = AbFile.createAbFile(str(self.imageFileAbPath) + self.fileName)
        originalImageFile.createNewFile()
        FileUtil.getInstance().write(ByteArrayInputStream(fileItem.get()), originalImageFile)
# from java.io.ByteArrayInputStream import ByteArrayInputStream
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.io.path.AbPath import AbPath
from org.apache.commons.fileupload.FileItem import FileItem


