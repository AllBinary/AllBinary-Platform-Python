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
# package org.allbinary.opengles

from __future__ import annotations

from org.allbinary.opengles.JOGL10 import JOGL10
from org.allbinary.opengles.GL11 import GL11


#JOGLEToKhronosGL11
class JOGL11(JOGL10, GL11):

    def _init_fields(self) -> None:
        self.gl11: GL2 = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor1(self, gl: GL) -> None:
        self._constructor2(gl, gl)
    

    def _constructor2(self, gl: GL, gl2: GL2) -> None:
        super().__init__(gl, gl2)
        self._init_fields()
        self.gl11 = self.getJOGLGL()
    

    def glBindBuffer(self, target: int, buffer: int) -> None:
        self.gl11.glBindBuffer(target, buffer)
    

    def glBufferData(self, target: int, size: int, data: Buffer, usage: int) -> None:
        self.gl11.glBufferData(target, size, data, usage)
    

    def glBufferSubData(self, target: int, offset: int, size: int, data: Buffer) -> None:
        self.gl11.glBufferSubData(target, offset, size, data)
    

    def glClipPlanef(self, plane: int, equation: list[float], offset: int) -> None:
        self.gl11.glClipPlanef(plane, equation, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glClipPlanef(self, plane: int, equation: FloatBuffer) -> None:
        self.gl11.glClipPlanef(plane, equation)
    

    def glColor4ub(self, red: int, green: int, blue: int, alpha: int) -> None:
        self.gl11.glColor4ub(red, green, blue, alpha)
    

    def glColorPointer(self, size: int, type_: int, stride: int, offset: int) -> None:
        self.gl11.glColorPointer(size, type_, stride, offset)
    

    def glDeleteBuffers(self, n: int, buffers: list[int], offset: int) -> None:
        self.gl11.glDeleteBuffers(n, buffers, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glDeleteBuffers(self, n: int, buffers: IntBuffer) -> None:
        self.gl11.glDeleteBuffers(n, buffers)
    

    def glDrawElements(self, mode: int, count: int, type_: int, offset: int) -> None:
        self.gl11.glDrawElements(mode, count, type_, offset)
    

    def glGenBuffers(self, n: int, buffers: list[int], offset: int) -> None:
        self.gl11.glGenBuffers(n, buffers, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGenBuffers(self, n: int, buffers: IntBuffer) -> None:
        self.gl11.glGenBuffers(n, buffers)
    

    def glGetBufferParameteriv(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glGetBufferParameteriv(target, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetBufferParameteriv(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glGetBufferParameteriv(target, pname, params)
    

    def glGetClipPlanef(self, pname: int, eqn: list[float], offset: int) -> None:
        self.gl11.glGetClipPlanef(pname, eqn, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetClipPlanef(self, pname: int, eqn: FloatBuffer) -> None:
        self.gl11.glGetClipPlanef(pname, eqn)
    

    def glGetFloatv(self, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetFloatv(pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetFloatv(self, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetFloatv(pname, params)
    

    def glGetLightfv(self, light: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetLightfv(light, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetLightfv(self, light: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetLightfv(light, pname, params)
    

    def glGetMaterialfv(self, face: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetMaterialfv(face, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetMaterialfv(self, face: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetMaterialfv(face, pname, params)
    

    def glGetTexEnviv(self, env: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glGetTexEnviv(env, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetTexEnviv(self, env: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glGetTexEnviv(env, pname, params)
    

    def glGetTexParameterfv(self, target: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetTexParameterfv(target, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetTexParameterfv(self, target: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetTexParameterfv(target, pname, params)
    

    def glGetTexParameteriv(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glGetTexParameteriv(target, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glGetTexParameteriv(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glGetTexParameteriv(target, pname, params)
    

    def glIsBuffer(self, buffer: int) -> bool:
        return self.gl11.glIsBuffer(buffer)
    

    def glIsEnabled(self, cap: int) -> bool:
        return self.gl11.glIsEnabled(cap)
    

    def glIsTexture(self, texture: int) -> bool:
        return self.gl11.glIsTexture(texture)
    

    def glNormalPointer(self, type_: int, stride: int, offset: int) -> None:
        self.gl11.glNormalPointer(type_, stride, offset)
    

    def glPointParameterf(self, pname: int, param: float) -> None:
        self.gl11.glPointParameterf(pname, param)
    

    def glPointParameterfv(self, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glPointParameterfv(pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glPointParameterfv(self, pname: int, params: FloatBuffer) -> None:
        self.gl11.glPointParameterfv(pname, params)
    

    def glTexCoordPointer(self, size: int, type_: int, stride: int, offset: int) -> None:
        self.gl11.glTexCoordPointer(size, type_, stride, offset)
    

    def glTexEnvi(self, target: int, pname: int, param: int) -> None:
        self.gl11.glTexEnvi(target, pname, param)
    

    def glTexEnviv(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glTexEnviv(target, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glTexEnviv(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glTexEnviv(target, pname, params)
    

    def glTexParameterfv(self, target: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glTexParameterfv(target, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glTexParameterfv(self, target: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glTexParameterfv(target, pname, params)
    

    def glTexParameteri(self, target: int, pname: int, param: int) -> None:
        self.gl11.glTexParameteri(target, pname, param)
    

    def glTexParameteriv(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glTexParameteriv(target, pname, params, offset)
    

    # Java overloaded method: Python keeps the last definition
    def glTexParameteriv(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glTexParameteriv(target, pname, params)
    

    def glTexParameterxv(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glTexParameteriv(target, pname, params, offset)
    

    def glVertexPointer(self, size: int, type_: int, stride: int, offset: int) -> None:
        self.gl11.glVertexPointer(size, type_, stride, offset)
from com.jogamp.opengl.GL import GL
from com.jogamp.opengl.GL2 import GL2


