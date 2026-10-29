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
# package org.allbinary.business.category

from __future__ import annotations



class CategoryData:
    instance: CategoryData = None

    def _init_fields(self) -> None:
        self.PARENT: str = "CATEGORY_PARENT"
        self.NAME: str = "CATEGORY_NAME"
        self.PATH: str = "CATEGORY_PATH"
        self.LABEL: str = "CATEGORY_LABEL"
        self.VIEW: str = "CATEGORY_VIEW_CATEGORY"
        self.LEVEL: str = "CATEGORY_LEVEL"
        self.REQUEST: str = "request"
        self.ROOTCATEGORY: str = "Category"
        self.UNCRYPTED_EXTENSION: str = CommonDataFileStrings.getInstance().UNCRYPTED_EXTENSION
        self.ENCRYPTED_EXTENSION: str = CommonDataFileStrings.getInstance().ENCRYPTED_EXTENSION
    

    @staticmethod
    def getInstance() -> CategoryData:
        return CategoryData.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings


CategoryData.instance = CategoryData()

