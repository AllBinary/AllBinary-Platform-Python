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
# package org.allbinary.input.automation.module.osgi

from __future__ import annotations

import os
import platform
import threading
from org.allbinary.thread.RunnableInterface import RunnableInterface


class InputAutomationNewBundleRunnable(RunnableInterface):
    FILE: str = "file:"
    JAR_DIR_PROP: str = "org.knopflerfish.gosg.jars"
    INPUT_AUTMATION_MODULE_BUNDLE_JAR_PATH: str = "ia/auto"
    MODULES_START_LEVEL: int = 8
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.inputAutomationBundleActivator: InputAutomationBundleActivator = None
        self.running: bool = False
        self.fileBasicArrayList: BasicArrayList = None
    

    def __init__(self, inputAutomationBundleActivator: InputAutomationBundleActivator) -> None:
        self._init_fields()
        self.inputAutomationBundleActivator = inputAutomationBundleActivator
        self.fileBasicArrayList = BasicArrayListD()
    

    # throws Exception
    def setThread(self, thread: threading.Thread) -> None:
        pass
    

    def isRunning(self) -> bool:
        with self._lock:
            return self._isRunning_unlocked()

    def _isRunning_unlocked(self) -> bool:
        return self.running
    

    def setRunning(self, running: bool) -> None:
        with self._lock:
            return self._setRunning_unlocked(running)

    def _setRunning_unlocked(self, running: bool) -> None:
        self.running = running
    

    # throws Exception
    def updateModules(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "updateModules")
        list_: BasicArrayList = self.findNewModules()
        size: int = list_.size()
        bundle: Bundle = None
        for index in range(0, size):
            bundle = self.install(list_.get(index))
            if bundle is not None:
                bundle.start(InputAutomationNewBundleRunnable.MODULES_START_LEVEL)
    

    # throws Exception
    def getAllJarSymbolicNameHashMap(self) -> dict:
        self.logUtil.putF(self.commonStrings.START, self, "getAllJarSymbolicNameHashMap")
        hashMap: dict = StdUtil.getInstance().createHashMap()
        jarFileBasicArrayList: BasicArrayList = self.getJarModuleFileBasicArrayList()
        self.logUtil.putF("Jar Module Files: " + str(jarFileBasicArrayList), self, "getAllJarSymbolicNameHashMap")
        size: int = jarFileBasicArrayList.size()
        file: File = None
        for index in range(0, size):
            file = jarFileBasicArrayList.get(index)
            if not file.isDirectory():
                fileInputStream: FileInputStream = FileInputStream(file)
                jarInputStream: JarInputStream = JarInputStream(fileInputStream)
                manifest: Manifest = jarInputStream.getManifest()
                if manifest is None:
                    pass
                else:
                    symbolicName: str = manifest.getMainAttributes().getValue(Constants.BUNDLE_SYMBOLICNAME)
                    if symbolicName is not None:
                        hashMap.put(symbolicName, URL(InputAutomationNewBundleRunnable.FILE + file.getAbsolutePath()))
        return hashMap
    

    def getJarModuleFileBasicArrayList(self) -> BasicArrayList:
        self.logUtil.putF(self.commonStrings.START, self, "getJarModuleFileBasicArrayList")
        baseJarPath: str = {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get(InputAutomationNewBundleRunnable.JAR_DIR_PROP, os.environ.get(str(InputAutomationNewBundleRunnable.JAR_DIR_PROP)))
        if baseJarPath.startswith(InputAutomationNewBundleRunnable.FILE):
            baseJarPath = baseJarPath[InputAutomationNewBundleRunnable.FILE.length():]
        jarFileFilter: FileFilter = BasicFileFilterUtil.getInstance(".jar")
        path: str = baseJarPath + str(InputAutomationNewBundleRunnable.INPUT_AUTMATION_MODULE_BUNDLE_JAR_PATH)
        self.logUtil.putF("Path: " + path, self, "getJarModuleFileBasicArrayList")
        file: File = File(path)
        self.logUtil.putF("File: " + str(file.getAbsolutePath()) + " isDirectory: " + str(file.isDirectory()), self, "getJarModuleFileBasicArrayList")
        return SubDirectory.getInstance().search(jarFileFilter, FileWrapperUtil.wrapFile(file))
    

    # throws Exception
    def getInstalledJarSymbolicNameBasicArrayList(self) -> BasicArrayList:
        self.logUtil.putF(self.commonStrings.START, self, "getInstalledJarSymbolicNameBasicArrayList")
        vector: BasicArrayList = BasicArrayListD()
        bundleContext: BundleContext = InputAutomationBundleActivator.getBundleContext()
        bundleArray: list[Bundle] = bundleContext.getBundles()
        if bundleArray is not None:
            self.logUtil.putF("bundleArray: " + str(len(bundleArray)), self, "getInputAutomationModuleServices")
            for index in range(0, len(bundleArray)):
                bundle: Bundle = bundleArray[index]
                vector.add(bundle.getSymbolicName())
        return vector
    

    # throws Exception
    def isInstalled(self, symbolicName: str) -> bool:
        self.logUtil.putF(str(CommonLabels.getInstance().START) + symbolicName, self, "isInstalled")
        list_: BasicArrayList = self.getInstalledJarSymbolicNameBasicArrayList()
        size: int = list_.size()
        nextSymbolicName: str = None
        for index in range(0, size):
            nextSymbolicName = list_.get(index)
            if ((nextSymbolicName > symbolicName) - (nextSymbolicName < symbolicName)) == 0:
                return True
        return False
    

    # throws Exception
    def findNewModules(self) -> BasicArrayList:
        self.logUtil.putF(self.commonStrings.START, self, "findNewModules")
        vector: BasicArrayList = BasicArrayListD()
        hashMap: dict = self.getAllJarSymbolicNameHashMap()
        self.logUtil.putF("All: " + str(hashMap), self, "findNewModules")
        set: Set = hashMap.keySet()
        symbolicNameArray: list[object] = set.toArray()
        size: int = len(symbolicNameArray)
        for index in range(0, size):
            symbolicName: str = symbolicNameArray[index]
            if not self.isInstalled(symbolicName):
                vector.add(hashMap.get(symbolicName))
        return vector
    

    # throws Exception
    def install(self, url: URL) -> Bundle:
        self.logUtil.putF(CommonLabels.getInstance().START + url, self, "install")
        bundleContext: BundleContext = InputAutomationBundleActivator.getBundleContext()
        return bundleContext.installBundle(str(url))
    

    def run(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            while self.isRunning():
                timeHelper.setStartTimeTNT()
                self.logUtil.putF(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT(), self, self.commonStrings.RUN)
                self.updateModules()
                break
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
# from java.io.File import File
# from java.io.FileFilter import FileFilter
# from java.io.FileInputStream import FileInputStream
# from java.net.URL import URL
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from java.util.jar.JarInputStream import JarInputStream
# from java.util.jar.Manifest import Manifest
from org.osgi.framework.Bundle import Bundle
from org.osgi.framework.BundleContext import BundleContext
from org.osgi.framework.Constants import Constants
from bundle.input.automation.InputAutomationBundleActivator import InputAutomationBundleActivator
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
from org.allbinary.logic.io.file.directory.SubDirectory import SubDirectory
from org.allbinary.logic.io.file.filter.BasicFileFilterUtil import BasicFileFilterUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


