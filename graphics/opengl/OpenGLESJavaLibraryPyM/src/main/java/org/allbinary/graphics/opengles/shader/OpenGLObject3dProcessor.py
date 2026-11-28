# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles.shader

from __future__ import annotations



class OpenGLObject3dProcessor:

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def process_j2(self, gl: GL10, object3d: object) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def process_j3(self, gl: GL10, object3d: object, index: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass

    def process(self, *args):
        implementation = __class__.__dict__.get("process_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().process(*args)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from org.allbinary.string.CommonStrings import CommonStrings


