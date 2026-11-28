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

import threading


class LicenseClientAndServerTest:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.vector: BasicArrayList = BasicArrayListD()
    

    def __init__(self, options: list[str]) -> None:
        from org.allbinary.logic.system.security.licensing.PrintLicenseInitInfo import PrintLicenseInitInfo
        from org.allbinary.logic.system.security.licensing.PrintLicenseInitInfo import PrintLicenseInitInfo
        from java.io.File import File
        from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
        from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
        __class__._init_fields(self)
        LicenseInitInfoUtil.getInstance().setFilePath(PrintLicenseInitInfo.PATH + PATH_GLOBALS.getInstance().INIT_PATH)
        for index in range(1, len(options)):
            self.vector.add(options[index])
        if len(options) < 2:
            file: File = File(str(PrintLicenseInitInfo.PATH) + "testlicenseservers.txt")
            reader: FileReader = FileReader(file)
            lineNumberReader: LineNumberReader = LineNumberReader(reader)
            while lineNumberReader.ready():
                self.vector.add(lineNumberReader.readLine())
    

    def test(self) -> None:
        with self._lock:
            return __class__.__dict__["_test_unlocked"].__get__(self, __class__)()

    def _test_unlocked(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
        from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
        from org.allbinary.logic.system.security.licensing.client.XmlRpcAbeLicenseRetrievalClient import XmlRpcAbeLicenseRetrievalClient
        from org.allbinary.util.BasicArrayList import BasicArrayList
        stringBuffer: StringMaker = StringMaker()
        try:
            list_: BasicArrayList = BasicArrayListD()
            TESTING: str = "Testing with new licence:<br/>"
            PROCESSING: str = "Processing: <br/>"
            END: str = "<br/>End<br/>"
            RESULT: str = "Test Result: "
            size: int = self.vector.size()
            for index in range(0, size):
                stringBuffer.append(TESTING)
                serverName: str = self.vector.get(index)
                try:
                    licenseInitInfo: LicenseInitInfo = LicenseInitInfo()
                    licenseInitInfo.addServer(serverName)
                    LicenseInitInfoUtil.getInstance().write(licenseInitInfo)
                    abeClientInformation: AbeClientInformationInterface = AbeClientInformationInterfaceFactory.getInstance()
                    xmlRpcAbeLicenseClient: XmlRpcAbeLicenseRetrievalClient = XmlRpcAbeLicenseRetrievalClient(abeClientInformation)
                    abeLicenseInterface: AbeLicenseInterface = xmlRpcAbeLicenseClient.get(None)
                    if abeLicenseInterface is not None:
                        stringBuffer.append(PROCESSING)
                        stringBuffer.append(str(abeLicenseInterface))
                    stringBuffer.append(END)
                    self.logUtil.putF(RESULT + str(stringBuffer), self, "test")
                    stringBuffer.delete(0, stringBuffer.length())
                except Exception as e:
                    list_.add(serverName)
                    self.logUtil.put("Test Error: " + str(stringBuffer), self, "test", e)
            self.logUtil.putF("Total Servers Failed: " + str(list_.size()) + " Failed Servers: " + str(list_), self, "test")
        except Exception as e:
            self.logUtil.put("Test Error: " + str(stringBuffer), self, "test", e)
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            licensingTest: LicenseClientAndServerTest = LicenseClientAndServerTest(args)
            licensingTest.test()
        except Exception as e:
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.put(CommonStrings.getInstance().EXCEPTION, "main()", "main()", e)
# from java.io.File import File
# from java.io.FileReader import FileReader
# from java.io.LineNumberReader import LineNumberReader
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
# from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.client.XmlRpcAbeLicenseRetrievalClient import XmlRpcAbeLicenseRetrievalClient
# from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.string.CommonStrings import CommonStrings


