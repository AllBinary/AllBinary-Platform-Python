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

from javax.microedition.khronos.opengles.GL10 import GL10


#JOGLEToKhronosGL10
class JOGL10(GL10):

    def _init_fields(self) -> None:
        self.RED: str = "red: "
        self.GREEN: str = " green: "
        self.BLUE: str = " blue: "
        self.ALPHA: str = " alpha: "
        self.PNAME: str = "pname: "
        self._PNAME: str = " pname: "
        self.PARAM: str = " param: "
        self.PARAMS: str = " params: "
        self.LIGHT: str = "light: "
        self.FACE: str = "face: "
        self.TARGET: str = "target: "
        if "gl10" not in vars(self): self.gl10: GL2 = None
        if "glu" not in vars(self): self.glu: GLU = None
        if "GL_LINE" not in vars(self): self.GL_LINE: int = 0
        if "GL_QUAD_STRIP" not in vars(self): self.GL_QUAD_STRIP: int = 0
    

    def __init__(self, gl: GL, gl2: GL2) -> None:
        from com.jogamp.opengl.glu.GLU import GLU
        from com.jogamp.opengl.GL import GL
        from com.jogamp.opengl.GL2 import GL2
        __class__._init_fields(self)
        self.gl10 = gl2
        self.glu = GLU.createGLU(self.gl10)
        self.GL_LINE = GL2.GL_LINE
        self.GL_QUAD_STRIP = GL2.GL_QUAD_STRIP
    

    def getJOGLGL(self) -> GL2:
        from com.jogamp.opengl.GL2 import GL2
        return self.gl10
    

    def glActiveTexture(self, texture: int) -> None:
        self.gl10.glActiveTexture(texture)
    

    def glAlphaFunc(self, func: int, ref: float) -> None:
        self.gl10.glAlphaFunc(func, ref)
    

    def glBindTexture(self, target: int, texture: int) -> None:
        self.gl10.glBindTexture(target, texture)
    

    def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
        self.gl10.glBlendFunc(sfactor, dfactor)
    

    def glClear(self, mask: int) -> None:
        self.gl10.glClear(mask)
    

    def glClearColor(self, red: float, green: float, blue: float, alpha: float) -> None:
        self.gl10.glClearColor(red, green, blue, alpha)
    

    def glClearDepthf(self, depth: float) -> None:
        self.gl10.glClearDepthf(depth)
    

    def glClearStencil(self, s: int) -> None:
        self.gl10.glClearStencil(s)
    

    def glClientActiveTexture(self, texture: int) -> None:
        self.gl10.glClientActiveTexture(texture)
    

    def glColor4f(self, red: float, green: float, blue: float, alpha: float) -> None:
        self.gl10.glColor4f(red, green, blue, alpha)
    

    def glColorMask(self, red: bool, green: bool, blue: bool, alpha: bool) -> None:
        self.gl10.glColorMask(red, green, blue, alpha)
    

    def glColorPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        self.gl10.glColorPointer(size, type_, stride, pointer)
    

    def glCompressedTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, imageSize: int, data: Buffer) -> None:
        self.gl10.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)
    

    def glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, imageSize: int, data: Buffer) -> None:
        self.gl10.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)
    

    def glCopyTexImage2D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, height: int, border: int) -> None:
        self.gl10.glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)
    

    def glCopyTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, x: int, y: int, width: int, height: int) -> None:
        self.gl10.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)
    

    def glCullFace(self, mode: int) -> None:
        self.gl10.glCullFace(mode)
    

    def glDeleteTextures_j3(self, n: int, textures: list[int], offset: int) -> None:
        self.gl10.glDeleteTextures(n, textures, offset)
    

    def glDeleteTextures_j2(self, n: int, textures: IntBuffer) -> None:
        self.gl10.glDeleteTextures(n, textures)

    def glDeleteTextures(self, *args):
        implementation = __class__.__dict__.get("glDeleteTextures_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glDeleteTextures(*args)
    

    def glDepthFunc(self, func: int) -> None:
        self.gl10.glDepthFunc(func)
    

    def glDepthMask(self, flag: bool) -> None:
        self.gl10.glDepthMask(flag)
    

    def glDepthRangef(self, zNear: float, zFar: float) -> None:
        self.gl10.glDepthRangef(zNear, zFar)
    

    def glDisable(self, cap: int) -> None:
        self.gl10.glDisable(cap)
    

    def glDisableClientState(self, array: int) -> None:
        self.gl10.glDisableClientState(array)
    

    def glDrawArrays(self, mode: int, first: int, count: int) -> None:
        self.gl10.glDrawArrays(mode, first, count)
    

    def glDrawElements(self, mode: int, count: int, type_: int, indices: Buffer) -> None:
        self.gl10.glDrawElements(mode, count, type_, indices)
    

    def glEnable(self, cap: int) -> None:
        self.gl10.glEnable(cap)
    

    def glEnableClientState(self, array: int) -> None:
        self.gl10.glEnableClientState(array)
    

    def glFinish(self) -> None:
        self.gl10.glFinish()
    

    def glFlush(self) -> None:
        self.gl10.glFlush()
    

    def glFogf(self, pname: int, param: float) -> None:
        self.gl10.glFogf(pname, param)
    

    def glFogfv_j3(self, pname: int, params: list[float], offset: int) -> None:
        self.gl10.glFogfv(pname, params, offset)
    

    def glFogfv_j2(self, pname: int, params: FloatBuffer) -> None:
        self.gl10.glFogfv(pname, params)

    def glFogfv(self, *args):
        implementation = __class__.__dict__.get("glFogfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glFogfv(*args)
    

    def glFrontFace(self, mode: int) -> None:
        self.gl10.glFrontFace(mode)
    

    def glFrustumf(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> None:
        self.gl10.glFrustumf(left, right, bottom, top, zNear, zFar)
    

    def glGenTextures_j3(self, n: int, textures: list[int], offset: int) -> None:
        self.gl10.glGenTextures(n, textures, offset)
    

    def glGenTextures_j2(self, n: int, textures: IntBuffer) -> None:
        self.gl10.glGenTextures(n, textures)

    def glGenTextures(self, *args):
        implementation = __class__.__dict__.get("glGenTextures_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGenTextures(*args)
    

    def glGetError(self) -> int:
        return self.gl10.glGetError()
    

    def glGetIntegerv_j3(self, pname: int, params: list[int], offset: int) -> None:
        self.gl10.glGetIntegerv(pname, params, offset)
    

    def glGetIntegerv_j2(self, pname: int, params: IntBuffer) -> None:
        self.gl10.glGetIntegerv(pname, params)

    def glGetIntegerv(self, *args):
        implementation = __class__.__dict__.get("glGetIntegerv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glGetIntegerv(*args)
    

    def glGetString(self, name: int) -> str:
        return self.gl10.glGetString(name)
    

    def glHint(self, target: int, mode: int) -> None:
        self.gl10.glHint(target, mode)
    

    def glLightModelf(self, pname: int, param: float) -> None:
        self.gl10.glLightModelf(pname, param)
    

    def glLightModelfv_j3(self, pname: int, params: list[float], offset: int) -> None:
        self.gl10.glLightModelfv(pname, params, offset)
    

    def glLightModelfv_j2(self, pname: int, params: FloatBuffer) -> None:
        self.gl10.glLightModelfv(pname, params)

    def glLightModelfv(self, *args):
        implementation = __class__.__dict__.get("glLightModelfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glLightModelfv(*args)
    

    def glLightf(self, light: int, pname: int, param: float) -> None:
        self.gl10.glLightf(light, pname, param)
    

    def glLightfv_j4(self, light: int, pname: int, params: list[float], offset: int) -> None:
        self.gl10.glLightfv(light, pname, params, offset)
    

    def glLightfv_j3(self, light: int, pname: int, params: FloatBuffer) -> None:
        self.gl10.glLightfv(light, pname, params)

    def glLightfv(self, *args):
        implementation = __class__.__dict__.get("glLightfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glLightfv(*args)
    

    def glLineWidth(self, width: float) -> None:
        self.gl10.glLineWidth(width)
    

    def glLoadIdentity(self) -> None:
        self.gl10.glLoadIdentity()
    

    def glLoadMatrixf_j2(self, m: list[float], offset: int) -> None:
        self.gl10.glLoadMatrixf(m, offset)
    

    def glLoadMatrixf_j1(self, m: FloatBuffer) -> None:
        self.gl10.glLoadMatrixf(m)

    def glLoadMatrixf(self, *args):
        implementation = __class__.__dict__.get("glLoadMatrixf_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glLoadMatrixf(*args)
    

    def glLogicOp(self, opcode: int) -> None:
        self.gl10.glLogicOp(opcode)
    

    def glMaterialf(self, face: int, pname: int, param: float) -> None:
        self.gl10.glMaterialf(face, pname, param)
    

    def glMaterialfv_j4(self, face: int, pname: int, params: list[float], offset: int) -> None:
        self.gl10.glMaterialfv(face, pname, params, offset)
    

    def glMaterialfv_j3(self, face: int, pname: int, params: FloatBuffer) -> None:
        self.gl10.glMaterialfv(face, pname, params)

    def glMaterialfv(self, *args):
        implementation = __class__.__dict__.get("glMaterialfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glMaterialfv(*args)
    

    def glMatrixMode(self, mode: int) -> None:
        self.gl10.glMatrixMode(mode)
    

    def glMultMatrixf_j2(self, m: list[float], offset: int) -> None:
        self.gl10.glMultMatrixf(m, offset)
    

    def glMultMatrixf_j1(self, m: FloatBuffer) -> None:
        self.gl10.glMultMatrixf(m)

    def glMultMatrixf(self, *args):
        implementation = __class__.__dict__.get("glMultMatrixf_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glMultMatrixf(*args)
    

    def glMultiTexCoord4f(self, target: int, s: float, t: float, r: float, q: float) -> None:
        self.gl10.glMultiTexCoord4f(target, s, t, r, q)
    

    def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
        self.gl10.glNormal3f(nx, ny, nz)
    

    def glNormalPointer(self, type_: int, stride: int, pointer: Buffer) -> None:
        self.gl10.glNormalPointer(type_, stride, pointer)
    

    def glOrthof(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> None:
        self.gl10.glOrthof(left, right, bottom, top, zNear, zFar)
    

    def glPixelStorei(self, pname: int, param: int) -> None:
        self.gl10.glPixelStorei(pname, param)
    

    def glPointSize(self, size: float) -> None:
        self.gl10.glPointSize(size)
    

    def glPolygonOffset(self, factor: float, units: float) -> None:
        self.gl10.glPolygonOffset(factor, units)
    

    def glPopMatrix(self) -> None:
        self.gl10.glPopMatrix()
    

    def glPushMatrix(self) -> None:
        self.gl10.glPushMatrix()
    

    def glReadPixels(self, x: int, y: int, width: int, height: int, format: int, type_: int, pixels: Buffer) -> None:
        self.gl10.glReadPixels(x, y, width, height, format, type_, pixels)
    

    def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
        self.gl10.glRotatef(angle, x, y, z)
    

    def glRotatex(self, angle: int, x: int, y: int, z: int) -> None:
        self.gl10.glRotatef(angle, x, y, z)
    

    def glSampleCoverage(self, value: float, invert: bool) -> None:
        self.gl10.glSampleCoverage(value, invert)
    

    def glScalef(self, x: float, y: float, z: float) -> None:
        self.gl10.glScalef(x, y, z)
    

    def glScalex(self, x: int, y: int, z: int) -> None:
        self.gl10.glScalef(x, y, z)
    

    def glScissor(self, x: int, y: int, width: int, height: int) -> None:
        self.gl10.glScissor(x, y, width, height)
    

    def glShadeModel(self, mode: int) -> None:
        self.gl10.glShadeModel(mode)
    

    def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
        self.gl10.glStencilFunc(func, ref, mask)
    

    def glStencilMask(self, mask: int) -> None:
        self.gl10.glStencilMask(mask)
    

    def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
        self.gl10.glStencilOp(fail, zfail, zpass)
    

    def glTexCoordPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        self.gl10.glTexCoordPointer(size, type_, stride, pointer)
    

    def glTexEnvf(self, target: int, pname: int, param: float) -> None:
        self.gl10.glTexEnvf(target, pname, param)
    

    def glTexEnvfv_j4(self, target: int, pname: int, params: list[float], offset: int) -> None:
        self.gl10.glTexEnvfv(target, pname, params, offset)
    

    def glTexEnvfv_j3(self, target: int, pname: int, params: FloatBuffer) -> None:
        self.gl10.glTexEnvfv(target, pname, params)

    def glTexEnvfv(self, *args):
        implementation = __class__.__dict__.get("glTexEnvfv_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().glTexEnvfv(*args)
    

    def glTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, format: int, type_: int, pixels: Buffer) -> None:
        self.gl10.glTexImage2D(target, level, internalformat, width, height, border, format, type_, pixels)
    

    def glTexParameterf(self, target: int, pname: int, param: float) -> None:
        self.gl10.glTexParameterf(target, pname, param)
    

    def glTexParameteri(self, target: int, pname: int, param: int) -> None:
        self.gl10.glTexParameteri(target, pname, param)
    

    def glTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, type_: int, pixels: Buffer) -> None:
        self.gl10.glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type_, pixels)
    

    def glTranslatef(self, x: float, y: float, z: float) -> None:
        self.gl10.glTranslatef(x, y, z)
    

    def glVertexPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        self.gl10.glVertexPointer(size, type_, stride, pointer)
    

    def glViewport(self, x: int, y: int, width: int, height: int) -> None:
        self.gl10.glViewport(x, y, width, height)
    

    def glBegin(self, i: int) -> None:
        self.gl10.glBegin(i)
    

    def glEnd(self) -> None:
        self.gl10.glEnd()
    

    def glVertex3f(self, f: float, f2: float, f3: float) -> None:
        self.gl10.glVertex3f(f, f2, f3)
    

    def glPolygonMode(self, i: int, i1: int) -> None:
        self.gl10.glPolygonMode(i, i1)
# from com.jogamp.opengl.glu.GLU import GLU
# from com.jogamp.opengl.GL import GL
# from com.jogamp.opengl.GL2 import GL2
# from java.nio.Buffer import Buffer
# from java.nio.FloatBuffer import FloatBuffer
# from java.nio.IntBuffer import IntBuffer


