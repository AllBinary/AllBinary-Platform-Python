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
from java.lang.JavaRuntimeStatic import lazy_static


class SetLicenseInitInfo:
    stdinput: BufferedReader = None

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.vector: BasicArrayList = BasicArrayListD()
    

    def __init__(self, options: list[str]) -> None:
        from org.allbinary.logic.system.security.licensing.PrintLicenseInitInfo import PrintLicenseInitInfo
        from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
        from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
        self._init_fields()
        LicenseInitInfoUtil.getInstance().setFilePath(PrintLicenseInitInfo.PATH + PATH_GLOBALS.getInstance().INIT_PATH)
        for index in range(1, len(options)):
            self.vector.add(options[index])
    

    # throws Exception
    def getLicenseInitInfo(self) -> LicenseInitInfo:
        from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
        from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
        from org.allbinary.logic.io.file.FileFactory import FileFactory
        licenseInitInfoUtil: LicenseInitInfoUtil = LicenseInitInfoUtil.getInstance()
        if FileFactory.getInstance().isFile(licenseInitInfoUtil.INITFILENAME):
            return licenseInitInfoUtil.read()
        else:
            return LicenseInitInfo()
    

    def createNewLicenseInitInfo(self, licenceServerVector: BasicArrayList) -> None:
        from org.allbinary.logic.system.security.licensing.PrintLicenseInitInfo import PrintLicenseInitInfo
        from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
        from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            if licenceServerVector is None:
                raise Exception("null BasicArrayList Passed - Just Make Empty if you want")
            licenseInitInfo: LicenseInitInfo = self.getLicenseInitInfo()
            print("License Serv Example: http://www.dartstatistics.com/LicServ/serverssl.php")
            licenseInitInfo.clearServers()
            file: File = File(str(PrintLicenseInitInfo.PATH) + "licenseservers.txt")
            reader: FileReader = FileReader(file)
            lineNumberReader: LineNumberReader = LineNumberReader(reader)
            while lineNumberReader.ready():
                licenseInitInfo.addServer(lineNumberReader.readLine())
            LicenseInitInfoUtil.getInstance().write(licenseInitInfo)
            LicenseInitInfoUtil.getInstance().read()
        except Exception as e:
            print("Error: " + str(e), end="")
            traceback.print_exception(e)
    

    # throws Exception
    @staticmethod
    def main(args: list[str]) -> None:
        initInfo: SetLicenseInitInfo = SetLicenseInitInfo(args)
        initInfo.createNewLicenseInitInfo(BasicArrayListD())
# from java.io.BufferedReader import BufferedReader
# from java.io.InputStreamReader import InputStreamReader
# from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
# from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
# from org.allbinary.logic.io.file.FileFactory import FileFactory
# from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
# from java.io.File import File
# from java.io.FileReader import FileReader
# from java.io.LineNumberReader import LineNumberReader
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _SetLicenseInitInfo_stdinput() -> object:
    return BufferedReader(InputStreamReader(System.in_))

lazy_static(SetLicenseInitInfo, "stdinput", _SetLicenseInitInfo_stdinput)

