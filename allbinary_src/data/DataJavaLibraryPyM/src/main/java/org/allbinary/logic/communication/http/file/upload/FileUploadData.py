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



class FileUploadData:
    instance: FileUploadData = None

    def _init_fields(self) -> None:
        self.FILE: str = "download_file_permissions.xml"
        self.UPLOAD_TO_FILE_PATH: str = "FILE_UPLOAD_UPLOAD_TO_FILE_PATH"
        self.FILE_DATA: str = "FILE_UPLOAD_FILE_DATA"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FileUploadData:
        return FileUploadData.instance


FileUploadData.instance = FileUploadData()

