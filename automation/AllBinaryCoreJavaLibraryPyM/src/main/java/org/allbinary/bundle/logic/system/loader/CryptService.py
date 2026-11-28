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
# package org.allbinary.bundle.logic.system.loader

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate


class CryptService:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.security.AbCryptUtil import AbCryptUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abCryptUtil: AbCryptUtil = AbCryptUtil.getInstance()
    

    def __init__(self) -> None:
        from org.allbinary.globals.Globals import Globals
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        __class__._init_fields(self)
        Globals.getInstance().init(__import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.getSystemClassLoader(), "./")
        self.logUtil.putF("Set Globals: " + str(URLGLOBALS.getWebappPath()), self, self.commonStrings.CONSTRUCTOR)
    

    def getDecryptedInputStream(self, abeClientInformation: AbeClientInformationInterface, name: str, inputStream: InputStream) -> InputStream:
        from java.io.ByteArrayInputStream import ByteArrayInputStream
        from java.io.InputStream import InputStream
        from org.allbinary.logic.system.security.AbKeys import AbKeys
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        try:
            key: str = AbKeys.getInstance().getKey(abeClientInformation, name)
            decrypted: list[int] = self.abCryptUtil.decrypt(inputStream, key)
            return ByteArrayInputStream(decrypted)
        except LicensingException as e:
            self.showLicenseDialog(abeClientInformation, e)
        except Exception as e:
            self.showLicenseDialog(abeClientInformation, e)
        return None
    

    def showLicenseDialog(self, abeClientInformation: AbeClientInformationInterface, e: Exception) -> None:
        from org.allbinary.gui.dialog.BasicTextJDialog import BasicTextJDialog
        from org.allbinary.gui.dialog.ExitCloseListener import ExitCloseListener
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.AbeLicenseInterface import AbeLicenseInterface
        from org.allbinary.logic.system.security.licensing.AbeLicenseInterfaceFactory import AbeLicenseInterfaceFactory
        from org.allbinary.logic.system.security.licensing.AbeNoLicense import AbeNoLicense
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        try:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
            basicTextJDialog: BasicTextJDialog = BasicTextJDialog(str(e))
            try:
                abeLicenseInterface: AbeLicenseInterface = AbeLicenseInterfaceFactory.getInstance().getLicenseInstance(abeClientInformation)
                if abeLicenseInterface != AbeNoLicense.getInstance():
                    if java_predicate(abeLicenseInterface, "isValid"):
                        basicTextJDialog.setText("Subscription Invalid")
            except LicensingException as e2:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e2)
            basicTextJDialog.addCloseListener(ExitCloseListener())
            basicTextJDialog.setVisible(True)
        except Exception as e3:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e3)
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.InputStream import InputStream
# from org.allbinary.globals.Globals import Globals
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.gui.dialog.BasicTextJDialog import BasicTextJDialog
# from org.allbinary.gui.dialog.ExitCloseListener import ExitCloseListener
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.AbCryptUtil import AbCryptUtil
# from org.allbinary.logic.system.security.AbKeys import AbKeys
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.AbeLicenseInterface import AbeLicenseInterface
# from org.allbinary.logic.system.security.licensing.AbeLicenseInterfaceFactory import AbeLicenseInterfaceFactory
# from org.allbinary.logic.system.security.licensing.AbeNoLicense import AbeNoLicense
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.string.CommonStrings import CommonStrings


