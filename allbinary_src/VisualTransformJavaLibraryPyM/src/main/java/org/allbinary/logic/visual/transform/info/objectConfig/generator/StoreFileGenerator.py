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
# package org.allbinary.logic.visual.transform.info.objectConfig.generator

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGenerator import TransformInfoObjectConfigGenerator


@java_inherited_overloads
class StoreFileGenerator(TransformInfoObjectConfigGenerator):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("output", None)
        vars(self).setdefault("fileAbPath", None)
        vars(self).setdefault("file", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "output" not in vars(self): self.output: str = None
        if "fileAbPath" not in vars(self): self.fileAbPath: AbPath = None
        if "file" not in vars(self): self.file: AbFile = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.string.regex.replace.Replace import Replace
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreInterface import TransformInfoHttpStoreInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        __class__._init_fields(self)
        httpTransformInfoInterface: TransformInfoHttpInterface = transformInfoInterface
        weblisketSession: WeblisketSession = WeblisketSession(httpTransformInfoInterface.getPropertiesHashMap(), httpTransformInfoInterface.getPageContext())
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(URLGLOBALS.getWebappPath())
        stringBuffer.append(weblisketSession.getStoreName())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        abPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
        fileName: str = httpTransformInfoInterface.getPropertiesHashMap().get(InputOutputTypeData.getInstance().FILE)
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if stringValidationUtil.isEmpty(fileName):
            transformInfoHttpStoreInterface: TransformInfoHttpStoreInterface = transformInfoInterface
            fileName = transformInfoInterface.getName().substring(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(transformInfoHttpStoreInterface.getStoreName()) + 1)
            outputMappingHashMap: HashMap = StdUtil.getInstance().createHashMap()
            outputMappingHashMap.put(TransformInfosData.getInstance().PREVIEW, "Preview")
            outputMappingHashMap.put(TransformInfosData.getInstance().SMALL_PREVIEW, "SmallPreview")
            outputMappingHashMap.put(CommonSeps.getInstance().SPACE, StringUtil.getInstance().EMPTY_STRING)
            replace: Replace = Replace(outputMappingHashMap)
            fileName = replace.all(fileName)
        if stringValidationUtil.isEmpty(fileName):
            raise Exception("TransformInfoObjectConfigGenerator FileName Not Specified")
        tempOutput: str = httpTransformInfoInterface.getPropertiesHashMap().get(InputOutputTypeData.getInstance().NAME)
        if stringValidationUtil.isEmpty(tempOutput):
            tempOutput = InputOutputTypeData.getInstance().DEFAULT
        self.output = tempOutput
        if stringValidationUtil.isEmpty(self.output):
            raise Exception("TransformInfoObjectConfigGenerator Output=extension Not Specified")
        stringBuffer = StringMaker()
        stringBuffer.append(fileName)
        stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
        stringBuffer.append(self.output)
        abPath = AbPath(str(abPath), str(stringBuffer))
        self.fileAbPath = abPath
        self.file = AbFile.createAbFileFromAbPath(self.fileAbPath)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("File: " + str(self.fileAbPath), self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def process(self, input: str) -> str:
        from java.io.ByteArrayInputStream import ByteArrayInputStream
        from java.io.InputStream import InputStream
        from org.allbinary.logic.io.file.FileUtil import FileUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Processing", self, self.commonStrings.PROCESS)
        if not (self.file.exists()):
            self.file.createNewFile()
        if self.file.exists():
            inputStream: InputStream = ByteArrayInputStream(list(input.encode()))
            FileUtil.getInstance().write(inputStream, self.file)
        else:
            raise Exception("Could Not Create: " + str(self.fileAbPath))
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Processed", self, self.commonStrings.PROCESS)
        return StringUtil.getInstance().EMPTY_STRING
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.InputStream import InputStream
# from java.util.HashMap import HashMap
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.FileUtil import FileUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.string.regex.replace.Replace import Replace
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreInterface import TransformInfoHttpStoreInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


