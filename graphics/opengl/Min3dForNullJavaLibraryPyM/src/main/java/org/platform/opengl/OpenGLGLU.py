# Generated Code Do Not Modify
# package org.platform.opengl

from __future__ import annotations



class OpenGLGLU:
    instance: OpenGLGLU = None
    

    @staticmethod
    def getInstance() -> OpenGLGLU:
        return OpenGLGLU.instance
    

    def gluLookAt(self, gl: GL10, eyeX: float, eyeY: float, eyeZ: float, centerX: float, centerY: float, centerZ: float, upX: float, upY: float, upZ: float) -> None:
        raise RuntimeError()
    

    def gluProject(self, gl: GL10, objX: float, objY: float, objZ: float, model: list[float], modelOffset: int, project: list[float], projectOffset: int, view: list[int], viewOffset: int, win: list[float], winOffset: int) -> int:
        raise RuntimeError()
    

    def gluUnProject(self, gl: GL10, winX: float, winY: float, winZ: float, model: list[float], modelOffset: int, project: list[float], projectOffset: int, view: list[int], viewOffset: int, obj: list[float], objOffset: int) -> int:
        raise RuntimeError()
    

    def glFrustumf(self, gl: GL10, lt: float, rt: float, btm: float, top: float, zNear: float, zFar: float) -> None:
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL10 import GL10


OpenGLGLU.instance = OpenGLGLU()

