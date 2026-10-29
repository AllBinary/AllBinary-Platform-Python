# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations



class OpenGLLogUtil:
    instance: OpenGLLogUtil = None

    def _init_fields(self) -> None:
        self.MAX_TEXTURE: str = " Max Texture Size: "
        self.LOG_ERROR: str = "logError"
        self.IMAGE: str = " Image: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLLogUtil:
        return OpenGLLogUtil.instance
    

    def logError(self, gl: GL10) -> None:
        error: int = gl.glGetError()
        if error != self.GL10.GL_NO_ERROR:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(OpenGLStrings.getInstance().GL_ERROR_LABEL)
            stringBuffer.appendint(error)
            if error == 1281:
                stringBuffer.append(self.MAX_TEXTURE)
                maxTextureSize: list[int] = [0] * (1)
                gl.glGetIntegerv(self.GL10.GL_MAX_TEXTURE_SIZE, maxTextureSize, 0)
                stringBuffer.appendint(maxTextureSize[0])
            if error == 1280:
                PreLogUtil.put(str(stringBuffer), self, OpenGLStrings.getInstance().SET)
            else:
                ForcedLogUtil.log(str(stringBuffer), self)
    

    # Java overloaded method: Python keeps the last definition
    def logError(self, gl: GL10, image: Image) -> None:
        error: int = gl.glGetError()
        if error != self.GL10.GL_NO_ERROR:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(OpenGLStrings.getInstance().GL_ERROR_LABEL)
            stringBuffer.appendint(error)
            if error == 1281:
                stringBuffer.append(self.MAX_TEXTURE)
                maxTextureSize: list[int] = [0] * (1)
                gl.glGetIntegerv(self.GL10.GL_MAX_TEXTURE_SIZE, maxTextureSize, 0)
                stringBuffer.appendint(maxTextureSize[0])
            stringBuffer.append(self.IMAGE)
            stringBuffer.append(str(image))
            PreLogUtil.put(str(stringBuffer), self, self.LOG_ERROR)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.opengles.OpenGLStrings import OpenGLStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil


OpenGLLogUtil.instance = OpenGLLogUtil()

