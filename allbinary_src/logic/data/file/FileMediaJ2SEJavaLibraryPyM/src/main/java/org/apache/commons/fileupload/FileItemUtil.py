# Generated Code Do Not Modify
# package org.apache.commons.fileupload

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FileItemUtil:
    instance: FileItemUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.DEFAULT_CHARSET: str = "ISO-8859-1"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FileItemUtil:
        return FileItemUtil.instance
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getString_j1_1(self, byteArray: list[int]) -> str:
        return bytes(byteArray, self.DEFAULT_CHARSET).decode()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getString_j1_2(self, fileItem: FileItemStream) -> str:
        return str(self.getBytes(fileItem), self.DEFAULT_CHARSET)

    def getString(self, *args):
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], list)):
            return self.getString_j1_1(*args)
        if len(args) == 1:
            return self.getString_j1_2(*args)
        return getattr(self, "getString_j" + str(len(args)))(*args)
    

    # throws Exception
    def getBytes(self, fileItem: FileItemStream) -> list[int]:
        from java.io.InputStream import InputStream
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        streamUtil: StreamUtil = StreamUtil.getInstance()
        inputStream: InputStream = None
        outputStream: ByteArrayOutputStream = None
        try:
            inputStream = fileItem.openStream()
            outputStream = ByteArrayOutputStream()
            if fileItem.isFormField():
                self.logUtil.putF("FileItemStream FieldName: " + str(fileItem.getFieldName()), self, "write()")
            else:
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Uploaded File FieldName: ")
                stringBuffer.append(fileItem.getFieldName())
                stringBuffer.append(" name = ")
                stringBuffer.append(fileItem.getName())
                self.logUtil.putF(str(stringBuffer), self, "write()")
            outputStream = streamUtil.get(inputStream, outputStream, [0] * (16384))
            return outputStream.toByteArray()
        finally:
            streamUtil.close(outputStream)
            streamUtil.close(inputStream)
    

    # throws Exception
    def write(self, fileItem: FileItem, file: AbFile) -> None:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil
        fileItem.write(AbFileNativeUtil.get(file))
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.InputStream import InputStream
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil
# from org.allbinary.logic.string.StringMaker import StringMaker


def _FileItemUtil_instance() -> object:
    return FileItemUtil()

lazy_static(FileItemUtil, "instance", _FileItemUtil_instance)

