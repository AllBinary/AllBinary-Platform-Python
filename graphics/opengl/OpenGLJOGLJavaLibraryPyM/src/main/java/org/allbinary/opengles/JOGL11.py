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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from javax.microedition.khronos.opengles.GL11 import GL11
from org.allbinary.opengles.JOGL10 import JOGL10


#JOGLEToKhronosGL11
@java_inherited_overloads
class JOGL11(*java_bases(JOGL10, GL11)):
    def _java_defaults(self):
        vars(self).setdefault("gl11", None)

    def _init_fields(self) -> None:
        if "gl11" not in vars(self): self.gl11: GL2 = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor1(self, gl: GL) -> None:
        __class__._java_defaults(self)
        from com.jogamp.opengl.GL import GL
        from com.jogamp.opengl.GL2 import GL2
        __class__._constructor2(self, gl, gl)
    

    def _constructor2(self, gl: GL, gl2: GL2) -> None:
        __class__._java_defaults(self)
        from com.jogamp.opengl.GL import GL
        from com.jogamp.opengl.GL2 import GL2
        super().__init__(gl, gl2)
        __class__._init_fields(self)
        self.gl11 = self.getJOGLGL()
    

    def glBindBuffer(self, target: int, buffer: int) -> None:
        self.gl11.glBindBuffer(target, buffer)
    

    def glBufferData(self, target: int, size: int, data: Buffer, usage: int) -> None:
        self.gl11.glBufferData(target, size, data, usage)
    

    def glBufferSubData(self, target: int, offset: int, size: int, data: Buffer) -> None:
        self.gl11.glBufferSubData(target, offset, size, data)
    

    def glClipPlanef_j3(self, plane: int, equation: list[float], offset: int) -> None:
        self.gl11.glClipPlanef(plane, equation, offset)
    

    def glClipPlanef_j2(self, plane: int, equation: FloatBuffer) -> None:
        self.gl11.glClipPlanef(plane, equation)

    def glClipPlanef(self, *args):
        implementation = __class__.__dict__.get("glClipPlanef_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glClipPlanef(*args)
    

    def glColor4ub(self, red: int, green: int, blue: int, alpha: int) -> None:
        self.gl11.glColor4ub(red, green, blue, alpha)
    

    def glColorPointer(self, size: int, type_: int, stride: int, offset: int) -> None:
        self.gl11.glColorPointer(size, type_, stride, offset)
    

    def glDeleteBuffers_j3(self, n: int, buffers: list[int], offset: int) -> None:
        self.gl11.glDeleteBuffers(n, buffers, offset)
    

    def glDeleteBuffers_j2(self, n: int, buffers: IntBuffer) -> None:
        self.gl11.glDeleteBuffers(n, buffers)

    def glDeleteBuffers(self, *args):
        implementation = __class__.__dict__.get("glDeleteBuffers_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glDeleteBuffers(*args)
    

    def glDrawElements(self, mode: int, count: int, type_: int, offset: int) -> None:
        self.gl11.glDrawElements(mode, count, type_, offset)
    

    def glGenBuffers_j3(self, n: int, buffers: list[int], offset: int) -> None:
        self.gl11.glGenBuffers(n, buffers, offset)
    

    def glGenBuffers_j2(self, n: int, buffers: IntBuffer) -> None:
        self.gl11.glGenBuffers(n, buffers)

    def glGenBuffers(self, *args):
        implementation = __class__.__dict__.get("glGenBuffers_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGenBuffers(*args)
    

    def glGetBufferParameteriv_j4(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glGetBufferParameteriv(target, pname, params, offset)
    

    def glGetBufferParameteriv_j3(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glGetBufferParameteriv(target, pname, params)

    def glGetBufferParameteriv(self, *args):
        implementation = __class__.__dict__.get("glGetBufferParameteriv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetBufferParameteriv(*args)
    

    def glGetClipPlanef_j3(self, pname: int, eqn: list[float], offset: int) -> None:
        self.gl11.glGetClipPlanef(pname, eqn, offset)
    

    def glGetClipPlanef_j2(self, pname: int, eqn: FloatBuffer) -> None:
        self.gl11.glGetClipPlanef(pname, eqn)

    def glGetClipPlanef(self, *args):
        implementation = __class__.__dict__.get("glGetClipPlanef_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetClipPlanef(*args)
    

    def glGetFloatv_j3(self, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetFloatv(pname, params, offset)
    

    def glGetFloatv_j2(self, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetFloatv(pname, params)

    def glGetFloatv(self, *args):
        implementation = __class__.__dict__.get("glGetFloatv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetFloatv(*args)
    

    def glGetLightfv_j4(self, light: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetLightfv(light, pname, params, offset)
    

    def glGetLightfv_j3(self, light: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetLightfv(light, pname, params)

    def glGetLightfv(self, *args):
        implementation = __class__.__dict__.get("glGetLightfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetLightfv(*args)
    

    def glGetMaterialfv_j4(self, face: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetMaterialfv(face, pname, params, offset)
    

    def glGetMaterialfv_j3(self, face: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetMaterialfv(face, pname, params)

    def glGetMaterialfv(self, *args):
        implementation = __class__.__dict__.get("glGetMaterialfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetMaterialfv(*args)
    

    def glGetTexEnviv_j4(self, env: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glGetTexEnviv(env, pname, params, offset)
    

    def glGetTexEnviv_j3(self, env: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glGetTexEnviv(env, pname, params)

    def glGetTexEnviv(self, *args):
        implementation = __class__.__dict__.get("glGetTexEnviv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetTexEnviv(*args)
    

    def glGetTexParameterfv_j4(self, target: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glGetTexParameterfv(target, pname, params, offset)
    

    def glGetTexParameterfv_j3(self, target: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glGetTexParameterfv(target, pname, params)

    def glGetTexParameterfv(self, *args):
        implementation = __class__.__dict__.get("glGetTexParameterfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetTexParameterfv(*args)
    

    def glGetTexParameteriv_j4(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glGetTexParameteriv(target, pname, params, offset)
    

    def glGetTexParameteriv_j3(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glGetTexParameteriv(target, pname, params)

    def glGetTexParameteriv(self, *args):
        implementation = __class__.__dict__.get("glGetTexParameteriv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetTexParameteriv(*args)
    

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
    

    def glPointParameterfv_j3(self, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glPointParameterfv(pname, params, offset)
    

    def glPointParameterfv_j2(self, pname: int, params: FloatBuffer) -> None:
        self.gl11.glPointParameterfv(pname, params)

    def glPointParameterfv(self, *args):
        implementation = __class__.__dict__.get("glPointParameterfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glPointParameterfv(*args)
    

    def glTexCoordPointer(self, size: int, type_: int, stride: int, offset: int) -> None:
        self.gl11.glTexCoordPointer(size, type_, stride, offset)
    

    def glTexEnvi(self, target: int, pname: int, param: int) -> None:
        self.gl11.glTexEnvi(target, pname, param)
    

    def glTexEnviv_j4(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glTexEnviv(target, pname, params, offset)
    

    def glTexEnviv_j3(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glTexEnviv(target, pname, params)

    def glTexEnviv(self, *args):
        implementation = __class__.__dict__.get("glTexEnviv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glTexEnviv(*args)
    

    def glTexParameterfv_j4(self, target: int, pname: int, params: list[float], offset: int) -> None:
        self.gl11.glTexParameterfv(target, pname, params, offset)
    

    def glTexParameterfv_j3(self, target: int, pname: int, params: FloatBuffer) -> None:
        self.gl11.glTexParameterfv(target, pname, params)

    def glTexParameterfv(self, *args):
        implementation = __class__.__dict__.get("glTexParameterfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glTexParameterfv(*args)
    

    def glTexParameteri(self, target: int, pname: int, param: int) -> None:
        self.gl11.glTexParameteri(target, pname, param)
    

    def glTexParameteriv_j4(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glTexParameteriv(target, pname, params, offset)
    

    def glTexParameteriv_j3(self, target: int, pname: int, params: IntBuffer) -> None:
        self.gl11.glTexParameteriv(target, pname, params)

    def glTexParameteriv(self, *args):
        implementation = __class__.__dict__.get("glTexParameteriv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glTexParameteriv(*args)
    

    def glTexParameterxv(self, target: int, pname: int, params: list[int], offset: int) -> None:
        self.gl11.glTexParameteriv(target, pname, params, offset)
    

    def glVertexPointer(self, size: int, type_: int, stride: int, offset: int) -> None:
        self.gl11.glVertexPointer(size, type_, stride, offset)
# from com.jogamp.opengl.GL import GL
# from com.jogamp.opengl.GL2 import GL2
# from java.nio.Buffer import Buffer
# from java.nio.FloatBuffer import FloatBuffer
# from java.nio.IntBuffer import IntBuffer


