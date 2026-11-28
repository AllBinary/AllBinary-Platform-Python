# Generated Code Do Not Modify
# package org.allbinary.device

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.image.opengles.OpenGLSurfaceChangedInterface import OpenGLSurfaceChangedInterface
from org.allbinary.device.GraphicsInterface import GraphicsInterface


@java_inherited_overloads
class OpenGLESGraphics(*java_bases(Graphics, OpenGLSurfaceChangedInterface, GraphicsInterface)):
    def _java_defaults(self):
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("gl", None)

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gl: GL10 = NullGL10.NULL_GL10
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def updateGL(self, gl: GL) -> None:
        from javax.microedition.khronos.opengles.GL import GL
        pass
    

    def set(self, gl: GL) -> None:
        from javax.microedition.khronos.opengles.GL import GL
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
        from javax.microedition.khronos.opengles.GL10 import GL10
        return self.gl
    

    def setFontDebug(self, font: Font, fontDebug: FontDebugBase) -> None:
        from javax.microedition.lcdui.Font import Font
        from org.allbinary.graphics.font.FontDebugBase import FontDebugBase
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Font import Font
# from org.allbinary.graphics.font.FontDebugBase import FontDebugBase
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.device.NullGL10 import NullGL10


