# Generated Code Do Not Modify
# package org.allbinary.device

from __future__ import annotations

# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.image.opengles.OpenGLSurfaceChangedInterface import OpenGLSurfaceChangedInterface
from org.allbinary.device.GraphicsInterface import GraphicsInterface


class OpenGLESGraphics(Graphics, OpenGLSurfaceChangedInterface, GraphicsInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gl: GL10 = NullGL10.NULL_GL10
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateGL(self, gl: GL) -> None:
        pass
    

    def set(self, gl: GL) -> None:
        pass
    

    # throws Exception
    def init(self) -> None:
        pass
    

    # throws Exception
    def update(self) -> None:
        pass
    

    def setOrthoginalMode(self) -> None:
        pass
    

    def setCameraMode(self) -> None:
        pass
    

    def getGl10(self) -> GL10:
        return self.gl
    

    def setFontDebug(self, font: Font, fontDebug: FontDebugBase) -> None:
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Font import Font
from org.allbinary.graphics.font.FontDebugBase import FontDebugBase
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.device.NullGL10 import NullGL10


