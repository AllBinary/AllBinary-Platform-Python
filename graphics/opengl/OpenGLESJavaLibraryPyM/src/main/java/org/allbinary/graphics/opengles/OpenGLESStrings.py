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
# package org.allbinary.graphics.opengles

from __future__ import annotations



class OpenGLESStrings:
    

    # throws Exception
    def set(self, gl: GL10) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
    

    def initFont(self, gl: GL10, width: int, height: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
    

    # throws Exception
    def update(self, gl: GL10, width: int, height: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
    

    def drawChar(self, gl: GL10, graphics: Graphics, character: str, x: int, y: int, anchor: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.lcdui.Graphics import Graphics
        raise RuntimeError()
    

    def drawChars(self, gl: GL10, graphics: Graphics, data: list[str], offset: int, length: int, x: int, y: int, anchor: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.lcdui.Graphics import Graphics
        raise RuntimeError()
    

    def drawString(self, gl: GL10, graphics: Graphics, string: str, x: int, y: int, anchor: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.lcdui.Graphics import Graphics
        raise RuntimeError()
    

    def drawSubstring(self, gl: GL10, graphics: Graphics, string: str, offset: int, len_: int, x: int, y: int, anchor: int) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.lcdui.Graphics import Graphics
        raise RuntimeError()
    

    def charWidth(self, ch: str) -> int:
        raise RuntimeError()
    

    def charsWidth(self, ch: list[str], offset: int, length: int) -> int:
        raise RuntimeError()
    

    def stringWidth_j1(self, string: str) -> int:
        raise RuntimeError()
    

    def stringWidth_j3(self, string: str, offset: int, len_: int) -> int:
        raise RuntimeError()

    def stringWidth(self, *args):
        implementation = __class__.__dict__.get("stringWidth_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().stringWidth(*args)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics


