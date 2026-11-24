# Generated Code Do Not Modify
# package org.platform.opengl

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class OpenGLGLU:
    instance: OpenGLGLU = None
    

    @staticmethod
    def getInstance() -> OpenGLGLU:
        return OpenGLGLU.instance
    

    def gluLookAt(self, gl: GL10, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
    

    def gluProject(self, gl: GL10, objX: float, objY: float, objZ: float, model: list[float], modelOffset: int, project: list[float], projectOffset: int, view: list[int], viewOffset: int, win: list[float], winOffset: int) -> int:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
    

    def gluUnProject(self, gl: GL10, winX: float, winY: float, winZ: float, model: list[float], modelOffset: int, project: list[float], projectOffset: int, view: list[int], viewOffset: int, obj: list[float], objOffset: int) -> int:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
    

    def glFrustumf(self, gl: GL10, lt: float, rt: float, btm: float, top: float, zNear: float, zFar: float) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL10 import GL10


def _OpenGLGLU_instance() -> object:
    return OpenGLGLU()

lazy_static(OpenGLGLU, "instance", _OpenGLGLU_instance)

