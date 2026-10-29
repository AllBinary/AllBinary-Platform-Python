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
# package org.allbinary.logic.communication.http.file.upload

from __future__ import annotations

from org.apache.commons.fileupload.FileUpload import FileUpload


class AbFileUpload(FileUpload):
    

    def __init__(self, fileItemFactory: FileItemFactory) -> None:
        super().__init__(fileItemFactory)
    

    # throws FileUploadException, IOException
    def getItemIterator(self, request: HttpServletRequest) -> FileItemIterator:
        return super().getItemIterator(ServletRequestContext(request))
# from java.io.IOException import IOException
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.apache.commons.fileupload.FileItemFactory import FileItemFactory
from org.apache.commons.fileupload.FileItemIterator import FileItemIterator
from org.apache.commons.fileupload.FileUploadException import FileUploadException
from org.apache.commons.fileupload.servlet.ServletRequestContext import ServletRequestContext


