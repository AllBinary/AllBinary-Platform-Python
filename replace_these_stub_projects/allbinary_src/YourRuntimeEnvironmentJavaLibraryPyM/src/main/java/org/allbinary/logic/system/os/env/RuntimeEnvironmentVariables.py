# Generated Code Do Not Modify
# package org.allbinary.logic.system.os.env

from __future__ import annotations

import os
import platform


class RuntimeEnvironmentVariables:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getTest1(self) -> str:
        return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get("java.java.home", os.environ.get(str("java.java.home")))
    

    def getVariable(self, var: str) -> str:
        environmentVariables: Properties = self.get()
        return environmentVariables.getProperty(var)
    

    def get(self) -> Properties:
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "get()", e)
            return None
    

    def getTempDir(self) -> str:
        try:
            return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get("java.io.tmpdir", os.environ.get(str("java.io.tmpdir")))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getTempDir()", e)
            return None
    

    def getLibraryPath(self) -> str:
        try:
            return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get("java.library.path", os.environ.get(str("java.library.path")))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getLibraryPath()", e)
            return None
    

    def getClassPath(self) -> str:
        try:
            return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get("java.class.path", os.environ.get(str("java.class.path")))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getClassPath()", e)
            return None
    

    def updateLibraryPath(self, libPath: str) -> None:
        try:
            existingPath: str = self.getLibraryPath()
            System.setProperty("java.library.path", libPath + ":" + existingPath)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateLibraryPath()", e)
    

    def getUserHome(self) -> str:
        try:
            return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get("user.home", os.environ.get(str("user.home")))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getUserHome()", e)
            return None
    

    def getUserDir(self) -> str:
        try:
            return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get("user.dir", os.environ.get(str("user.dir")))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getUserDir()", e)
            return None
    

    def set(self) -> None:
        try:
            pass
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "get()", e)
    

    def setVariable(self, var: str, val: str) -> None:
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().OSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setVariable()", e)
# from java.io.BufferedReader import BufferedReader
# from java.io.InputStreamReader import InputStreamReader
# from java.util.Properties import Properties
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
from org.allbinary.string.CommonStrings import CommonStrings


