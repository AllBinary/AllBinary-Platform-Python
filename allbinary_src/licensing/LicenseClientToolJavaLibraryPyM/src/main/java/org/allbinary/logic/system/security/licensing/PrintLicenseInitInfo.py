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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations

import traceback


class PrintLicenseInitInfo:
    PATH: str = "G:\\mnt\\bc\\mydev\\work\\allbinary_src\\licensing\\data\\"
    

    def __init__(self, options: list[str]) -> None:
        LicenseInitInfoUtil.getInstance().setFilePath(PrintLicenseInitInfo.PATH + self.PATH_GLOBALS.getInstance().INIT_PATH)
    

    # throws Exception
    def getLicenseInitInfo(self) -> LicenseInitInfo:
        licenseInitInfoUtil: LicenseInitInfoUtil = LicenseInitInfoUtil.getInstance()
        if FileFactory.getInstance().isFile(licenseInitInfoUtil.getFilePath()):
            return licenseInitInfoUtil.read()
        else:
            print("No Licence File at: " + str(licenseInitInfoUtil.getFilePath()))
            return LicenseInitInfo()
    

    def printInitInfo(self) -> None:
        try:
            licenseInitInfo: LicenseInitInfo = self.getLicenseInitInfo()
            print("License ID: " + str(licenseInitInfo.getLicenseId()))
            list_: BasicArrayList = licenseInitInfo.getServerList()
            size: int = list_.size()
            for index in range(0, size):
                print("Lic Serv: " + str(list_.get(index)))
        except Exception as e:
            print("Error: " + str(e), end="")
            traceback.print_exception(e)
    

    # throws Exception
    @staticmethod
    def main(args: list[str]) -> None:
        initInfo: PrintLicenseInitInfo = PrintLicenseInitInfo(args)
        initInfo.printInitInfo()
from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
from org.allbinary.logic.io.file.FileFactory import FileFactory
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
from org.allbinary.util.BasicArrayList import BasicArrayList


