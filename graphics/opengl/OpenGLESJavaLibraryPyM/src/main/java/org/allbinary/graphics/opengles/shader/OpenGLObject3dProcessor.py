# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles.shader

from __future__ import annotations



class OpenGLObject3dProcessor:

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def process_j2(self, gl: GL10, object3d: object) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def process_j3(self, gl: GL10, object3d: object, index: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass

    def process(self, *args):
        return getattr(self, "process_j" + str(len(args)))(*args)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from org.allbinary.string.CommonStrings import CommonStrings


