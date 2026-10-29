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
# package org.allbinary.business.context.modules.storefront

from __future__ import annotations



class StoreFrontData:
    instance: StoreFrontData = None

    def _init_fields(self) -> None:
        self.CANCEL: str = "Cancel Store Front"
        self.SELECT: str = "Select Store Front"
        self.INSTALL: str = "Install Store Front"
        self.INSTALL_COMPLETE: str = "Install Store Front Complete"
        self.NAME: str = "STOREFRONT_NAME"
        self.CURRENTHOSTNAME: str = "STOREFRONT_CURRENTHOSTNAME"
        self.CURRENTHOSTNAMEPATH: str = "STOREFRONT_CURRENTHOSTNAMEPATH"
        self.CURRENTHOMEHOSTNAME: str = "STOREFRONT_CURRENTHOMEHOSTNAME"
        self.CURRENTHOMEHOSTNAMEPATH: str = "STOREFRONT_CURRENTHOMEHOSTNAMEPATH"
        self.HOMEHOSTNAME: str = "STOREFRONT_HOMEHOSTNAME"
        self.HOMEHOSTNAMEPATH: str = "STOREFRONT_HOMEHOSTNAMEPATH"
        self.HOSTNAME: str = "STOREFRONT_HOSTNAME"
        self.HOSTNAMEPATH: str = "STOREFRONT_HOSTNAMEPATH"
        self.TESTHOMEHOSTNAME: str = "STOREFRONT_TESTHOMEHOSTNAME"
        self.TESTHOMEHOSTNAMEPATH: str = "STOREFRONT_TESTHOMEHOSTNAMEPATH"
        self.TESTHOSTNAME: str = "STOREFRONT_TESTHOSTNAME"
        self.TESTHOSTNAMEPATH: str = "STOREFRONT_TESTHOSTNAMEPATH"
        self.IMAGEPATH: str = "STOREFRONT_IMAGEPATH"
        self.STATICPATH: str = "STOREFRONT_STATICPATH"
        self.CATEGORYPATH: str = "STOREFRONT_CATEGORYPATH"
        self.INVENTORYCONTROL: str = "STOREFRONT_INVENTORYCONTROL"
        self.CONFIGURATION: str = "STOREFRONT_CONFIGURATION"
        self.SUBSTORES: str = "STOREFRONT_SUBSTORES"
        self.TAGLOCATION: str = "STOREFRONT_TAGLOCATION"
        self.PACKAGELOCATION: str = "STOREFRONT_PACKAGELOCATION"
        self.FTP: str = "STOREFRONT_FTP"
        self.FTPPATH: str = "STOREFRONT_FTPPATH"
        self.FTPUSERNAME: str = "STOREFRONT_FTPUSERNAME"
        self.FTPPASSWORD: str = "STOREFRONT_FTPPASSWORD"
        self.TESTFTP: str = "STOREFRONT_TESTFTP"
        self.TESTFTPPATH: str = "STOREFRONT_TESTFTPPATH"
        self.TESTFTPUSERNAME: str = "STOREFRONT_TESTFTPUSERNAME"
        self.TESTFTPPASSWORD: str = "STOREFRONT_TESTFTPPASSWORD"
        self.SELECTSTORENAME: str = "STOREFRONT_SELECTSTORENAME"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> StoreFrontData:
        return StoreFrontData.instance


StoreFrontData.instance = StoreFrontData()

