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
# package org.allbinary.logic.visual.transform

from __future__ import annotations

from org.allbinary.logic.visual.transform.AbTransformer import AbTransformer


class BasicTransformer(AbTransformer):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.streamUtil: StreamUtil = StreamUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = None
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.setTemplateAsInputStream()
    

    # throws Exception
    def setEncryptedTemplateFileAsInputStream(self, file: AbFile) -> None:
        outputStream: ByteArrayOutputStream = None
        inputStream: AbFileInputStream = None
        try:
            outputStream = ByteArrayOutputStream()
            inputStream = AbFileInputStream(file)
            outputStream = self.streamUtil.get(inputStream, outputStream, [0] * (16384))
            abCrypt: AbCrypt = AbCrypt(KeySpecFactory.DESEDE, AbKeys.getInstance().getKey(self.abeClientInformation, file.getAbsolutePath()))
            decrypted: list[int] = abCrypt.decrypt(outputStream.toByteArray())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Decrypted Template: \n" + str(bytes(decrypted).decode()), self, "setEncryptedTemplateFileAsInputStream(file)")
            self.setInputStream(ByteArrayInputStream(decrypted))
            self.setURIResolver(BasicUriResolver(TransformInfoTemplateData.getInstance().ENCRYPTED_EXTENSION))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Failed to get Encrypted File: ")
                stringBuffer.append(file.getPath())
                stringBuffer.append(" \nName:")
                stringBuffer.append(file.getName())
                self.logUtil.put(str(stringBuffer), self, "setEncryptedTemplateFileAsInputStream()", e)
            raise e
        finally:
            self.streamUtil.close(outputStream)
            self.streamUtil.close(inputStream)
    

    # throws Exception
    def setEncryptedTemplateAsInputStream(self) -> None:
        outputStream: ByteArrayOutputStream = None
        inputStream: ByteArrayInputStream = None
        try:
            outputStream = ByteArrayOutputStream()
            inputStream = ByteArrayInputStream(self.getTransformInfoInterface().getTemplate().getBytes())
            outputStream = self.streamUtil.get(inputStream, outputStream, [0] * (16384))
            abCrypt: AbCrypt = AbCrypt(KeySpecFactory.DESEDE, AbKeys.getInstance().getKey(self.abeClientInformation, self.getTransformInfoInterface().getName()))
            decrypted: list[int] = abCrypt.decrypt(outputStream.toByteArray())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF("Decrypted Template: \n" + str(decrypted), self, "setEncryptedTemplateAsInputStream()")
            self.setInputStream(ByteArrayInputStream(decrypted))
            self.setURIResolver(BasicUriResolver(TransformInfoTemplateData.getInstance().ENCRYPTED_EXTENSION))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put("Failed to set with template: " + str(self.getTransformInfoInterface().getTemplateFilePath()), self, "setEncryptedTemplateFileAsInputStream()", e)
            raise e
        finally:
            self.streamUtil.close(outputStream)
            self.streamUtil.close(inputStream)
    

    # throws Exception
    def setTemplateAsInputStream(self) -> None:
        inputStream: AbFileInputStream = None
        outputStream: ByteArrayOutputStream = None
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                self.logUtil.putF(self.getTransformInfoInterface().log(), self, "setTemplateAsInputStream()")
            transformInfoTemplateData: TransformInfoTemplateData = TransformInfoTemplateData.getInstance()
            pathUtil: PathUtil = PathUtil.getInstance()
            if self.getTransformInfoInterface().getTemplateFilePath() is not None:
                extension: str = pathUtil.getExtensionWithAbPath(self.getTransformInfoInterface().getTemplateFilePath())
                filePath: str = pathUtil.getWithoutExtensionWithAbPath(self.getTransformInfoInterface().getTemplateFilePath())
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                    self.logUtil.putF(self.getTransformInfoInterface().log(), self, "setTemplateAsInputStream()")
                if ((extension > transformInfoTemplateData.UNCRYPTED_EXTENSION) - (extension < transformInfoTemplateData.UNCRYPTED_EXTENSION)) == 0:
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(filePath)
                    stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
                    stringBuffer.append(transformInfoTemplateData.ENCRYPTED_EXTENSION)
                    encFile: AbFile = AbFile.createAbFile(str(stringBuffer))
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                        self.logUtil.putF(self.getTransformInfoInterface().log(), self, "setTemplateAsInputStream()")
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                        stringBuffer = StringMaker()
                        stringBuffer.append("Encrypted Template File isFile=")
                        stringBuffer.appendboolean(encFile.isFile())
                        stringBuffer.append("\nEncTemplateFilePath: ")
                        stringBuffer.append(encFile.getPath())
                        self.logUtil.putF(str(stringBuffer), self, "setTemplateAsInputStream()")
                    if encFile.isFile():
                        self.setEncryptedTemplateFileAsInputStream(encFile)
                        return
                    else:
                        file: AbFile = AbFile.createAbFileFromAbPath(self.getTransformInfoInterface().getTemplateFilePath())
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                            self.logUtil.putF(self.getTransformInfoInterface().log(), self, "setTemplateAsInputStream()")
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                            self.logUtil.putF("Template File isFile=" + str(file.isFile()), self, "setTemplateAsInputStream()")
                        if file.isFile():
                            inputStream = AbFileInputStream(file)
                            outputStream = ByteArrayOutputStream()
                            outputStream = self.streamUtil.get(inputStream, outputStream, [0] * (16384))
                            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                                self.logUtil.putF("Template: " + str(outputStream), self, "getTemplateAsInputStream()")
                            self.setInputStream(ByteArrayInputStream(outputStream.toByteArray()))
                            self.setURIResolver(BasicUriResolver(transformInfoTemplateData.UNCRYPTED_EXTENSION))
                            return
                elif ((extension > transformInfoTemplateData.ENCRYPTED_EXTENSION) - (extension < transformInfoTemplateData.ENCRYPTED_EXTENSION)) == 0:
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(filePath)
                    stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
                    stringBuffer.append(transformInfoTemplateData.ENCRYPTED_EXTENSION)
                    file: AbFile = AbFile.createAbFile(str(stringBuffer))
                    if file.isFile():
                        self.setEncryptedTemplateFileAsInputStream(file)
                else:
                    raise Exception("View Template File Type Is Not Recognized: " + str(self.getTransformInfoInterface().getTemplateFilePath()))
            else:
                self.setEncryptedTemplateAsInputStream()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put("Failed to get Template Data", self, "setTemplateAsInputStream()", e)
            raise e
        finally:
            self.streamUtil.close(outputStream)
            self.streamUtil.close(inputStream)
        raise Exception("Error setTemplateAsInputStream()")
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.InputStream import InputStream
# from javax.xml.transform.URIResolver import URIResolver
from org.allbinary.data.tree.dom.BasicUriResolver import BasicUriResolver
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.jcehelper.AbCrypt import AbCrypt
from org.allbinary.logic.control.crypt.jcehelper.KeySpecFactory import KeySpecFactory
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.io.path.PathUtil import PathUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.AbKeys import AbKeys
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.template.TransformInfoTemplateData import TransformInfoTemplateData


