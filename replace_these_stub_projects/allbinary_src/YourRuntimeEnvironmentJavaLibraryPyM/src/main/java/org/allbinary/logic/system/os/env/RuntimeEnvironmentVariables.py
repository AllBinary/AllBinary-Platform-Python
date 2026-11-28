# Generated Code Do Not Modify
# package org.allbinary.logic.system.os.env

from __future__ import annotations

from java.lang.System import System
from java.lang.Runtime import Runtime
import os
import platform


class RuntimeEnvironmentVariables:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getTest1(self) -> str:
        return System.getProperty("java.java.home")
    

    def getVariable(self, var: str) -> str:
        from java.util.Properties import Properties
        environmentVariables: Properties = self.get()
        return environmentVariables.getProperty(var)
    

    def get(self) -> Properties:
        from java.io.BufferedReader import BufferedReader
        from java.io.InputStreamReader import InputStreamReader
        from java.util.Properties import Properties
        from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
        from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
        from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            process: Process = None
            environmentVariables: Properties = Properties()
            operatingSystemInterface: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
            osName: str = operatingSystemInterface.getName()
            linuxCommand: str = "env"
            windowsCommand: str = "cmd.exe /c set"
            solarisCommand: str = linuxCommand
            operatingSystems: OperatingSystems = OperatingSystems.getInstance()
            if ((osName > operatingSystems.LINUX) - (osName < operatingSystems.LINUX)) == 0:
                process = Runtime.getRuntime().exec_(linuxCommand)
            elif osName.find(operatingSystems.WINDOWS) >= 0:
                process = Runtime.getRuntime().exec_(windowsCommand)
            elif ((osName > operatingSystems.SOLARIS) - (osName < operatingSystems.SOLARIS)) == 0:
                process = Runtime.getRuntime().exec_(solarisCommand)
            else:
                raise Exception()
            processInputStreamReader: InputStreamReader = InputStreamReader(process.getInputStream())
            bufferedReader: BufferedReader = BufferedReader(processInputStreamReader)
            keyValuePair: str = None
            while ((keyValuePair := bufferedReader.readLine())) is not None:
                index: int = keyValuePair.find('=')
                key: str = keyValuePair[0:index]
                value: str = keyValuePair[index + 1:]
                environmentVariables.put(key, value)
            return environmentVariables
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "get()", e)
            return None
    

    def getTempDir(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return System.getProperty("java.io.tmpdir")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getTempDir()", e)
            return None
    

    def getLibraryPath(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return System.getProperty("java.library.path")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getLibraryPath()", e)
            return None
    

    def getClassPath(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return System.getProperty("java.class.path")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getClassPath()", e)
            return None
    

    def updateLibraryPath(self, libPath: str) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            existingPath: str = self.getLibraryPath()
            System.setProperty("java.library.path", libPath + ":" + existingPath)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateLibraryPath()", e)
    

    def getUserHome(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return System.getProperty("user.home")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getUserHome()", e)
            return None
    

    def getUserDir(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return System.getProperty("user.dir")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getUserDir()", e)
            return None
    

    def set(self) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            pass
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "get()", e)
    

    def setVariable(self, var: str, val: str) -> None:
        from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
        from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
        from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            process: Process = None
            operatingSystemInterface: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
            operatingSystems: OperatingSystems = OperatingSystems.getInstance()
            osName: str = operatingSystemInterface.getName()
            windowsCommand: str = "cmd.exe /c set" + var + "=" + val
            if ((osName > operatingSystems.LINUX) - (osName < operatingSystems.LINUX)) == 0:
                raise Exception()
            elif osName.find(operatingSystems.WINDOWS) >= 0:
                process = Runtime.getRuntime().exec_(windowsCommand)
            elif ((osName > operatingSystems.SOLARIS) - (osName < operatingSystems.SOLARIS)) == 0:
                raise Exception()
            else:
                raise Exception()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setVariable()", e)
# from java.io.BufferedReader import BufferedReader
# from java.io.InputStreamReader import InputStreamReader
# from java.util.Properties import Properties
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
# from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
# from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


