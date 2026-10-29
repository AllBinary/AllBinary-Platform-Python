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



class LogoData:
    instance: LogoData = None

    def _init_fields(self) -> None:
        self.NAME: str = "LOGO_NAME"
        self.IMAGEPATH: str = "LOGO_IMAGE_PATH"
        self.IMAGEFILENAME: str = "LOGO_IMAGE_FILE_NAME"
        self.IMAGE: str = "LOGO_IMAGE"
    

    @staticmethod
    def getInstance() -> LogoData:
        return LogoData.instance
    

    def __init__(self) -> None:
        self._init_fields()


LogoData.instance = LogoData()

