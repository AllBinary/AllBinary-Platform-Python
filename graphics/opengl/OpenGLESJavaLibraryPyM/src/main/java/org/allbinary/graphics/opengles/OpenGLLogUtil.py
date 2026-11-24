# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


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
    

    def logError_j1(self, gl: GL10) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from org.allbinary.image.opengles.OpenGLStrings import OpenGLStrings
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        error: int = gl.glGetError()
        if error != GL10.GL_NO_ERROR:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(OpenGLStrings.getInstance().GL_ERROR_LABEL)
            stringBuffer.appendint(error)
            if error == 1281:
                stringBuffer.append(self.MAX_TEXTURE)
                maxTextureSize: list[int] = [0] * (1)
                gl.glGetIntegerv(GL10.GL_MAX_TEXTURE_SIZE, maxTextureSize, 0)
                stringBuffer.appendint(maxTextureSize[0])
            if error == 1280:
                PreLogUtil.put(str(stringBuffer), self, OpenGLStrings.getInstance().SET)
            else:
                ForcedLogUtil.log(str(stringBuffer), self)
    

    def logError_j2(self, gl: GL10, image: Image) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.image.opengles.OpenGLStrings import OpenGLStrings
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        error: int = gl.glGetError()
        if error != GL10.GL_NO_ERROR:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(OpenGLStrings.getInstance().GL_ERROR_LABEL)
            stringBuffer.appendint(error)
            if error == 1281:
                stringBuffer.append(self.MAX_TEXTURE)
                maxTextureSize: list[int] = [0] * (1)
                gl.glGetIntegerv(GL10.GL_MAX_TEXTURE_SIZE, maxTextureSize, 0)
                stringBuffer.appendint(maxTextureSize[0])
            stringBuffer.append(self.IMAGE)
            stringBuffer.append(str(image))
            PreLogUtil.put(str(stringBuffer), self, self.LOG_ERROR)

    def logError(self, *args):
        return getattr(self, "logError_j" + str(len(args)))(*args)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.image.opengles.OpenGLStrings import OpenGLStrings
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil


def _OpenGLLogUtil_instance() -> object:
    return OpenGLLogUtil()

lazy_static(OpenGLLogUtil, "instance", _OpenGLLogUtil_instance)

