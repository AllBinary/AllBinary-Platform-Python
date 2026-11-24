# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.device

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from javax.microedition.khronos.opengles.GL10 import GL10


class NullGL10(GL10):
    NULL_GL10: NullGL10 = None
    

    def glActiveTexture(self, texture: int) -> None:
        return
    

    def glAlphaFunc(self, func: int, ref: float) -> None:
        return
    

    def glBindTexture(self, target: int, texture: int) -> None:
        return
    

    def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
        return
    

    def glClear(self, mask: int) -> None:
        return
    

    def glClearColor(self, red: float, green: float, blue: float, alpha: float) -> None:
        return
    

    def glClearDepthf(self, depth: float) -> None:
        return
    

    def glClearStencil(self, s: int) -> None:
        return
    

    def glClientActiveTexture(self, texture: int) -> None:
        return
    

    def glColor4f(self, red: float, green: float, blue: float, alpha: float) -> None:
        return
    

    def glColorMask(self, red: bool, green: bool, blue: bool, alpha: bool) -> None:
        return
    

    def glColorPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        return
    

    def glCompressedTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, imageSize: int, data: Buffer) -> None:
        return
    

    def glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, imageSize: int, data: Buffer) -> None:
        return
    

    def glCopyTexImage2D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, height: int, border: int) -> None:
        return
    

    def glCopyTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, x: int, y: int, width: int, height: int) -> None:
        return
    

    def glCullFace(self, mode: int) -> None:
        return
    

    def glDeleteTextures_j3(self, n: int, textures: list[int], offset: int) -> None:
        return
    

    def glDeleteTextures_j2(self, n: int, textures: IntBuffer) -> None:
        return

    def glDeleteTextures(self, *args):
        return getattr(self, "glDeleteTextures_j" + str(len(args)))(*args)
    

    def glDepthFunc(self, func: int) -> None:
        return
    

    def glDepthMask(self, flag: bool) -> None:
        return
    

    def glDepthRangef(self, zNear: float, zFar: float) -> None:
        return
    

    def glDisable(self, cap: int) -> None:
        return
    

    def glDisableClientState(self, array: int) -> None:
        return
    

    def glDrawArrays(self, mode: int, first: int, count: int) -> None:
        return
    

    def glDrawElements(self, mode: int, count: int, type_: int, indices: Buffer) -> None:
        return
    

    def glEnable(self, cap: int) -> None:
        return
    

    def glEnableClientState(self, array: int) -> None:
        return
    

    def glFinish(self) -> None:
        return
    

    def glFlush(self) -> None:
        return
    

    def glFogf(self, pname: int, param: float) -> None:
        return
    

    def glFogfv_j3(self, pname: int, params: list[float], offset: int) -> None:
        return
    

    def glFogfv_j2(self, pname: int, params: FloatBuffer) -> None:
        return

    def glFogfv(self, *args):
        return getattr(self, "glFogfv_j" + str(len(args)))(*args)
    

    def glFrontFace(self, mode: int) -> None:
        return
    

    def glFrustumf(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> None:
        return
    

    def glGenTextures_j3(self, n: int, textures: list[int], offset: int) -> None:
        return
    

    def glGenTextures_j2(self, n: int, textures: IntBuffer) -> None:
        return

    def glGenTextures(self, *args):
        return getattr(self, "glGenTextures_j" + str(len(args)))(*args)
    

    def glGetError(self) -> int:
        return 0
    

    def glGetIntegerv_j3(self, pname: int, params: list[int], offset: int) -> None:
        return
    

    def glGetIntegerv_j2(self, pname: int, params: IntBuffer) -> None:
        return

    def glGetIntegerv(self, *args):
        return getattr(self, "glGetIntegerv_j" + str(len(args)))(*args)
    

    def glGetString(self, name: int) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING
    

    def glHint(self, target: int, mode: int) -> None:
        return
    

    def glLightModelf(self, pname: int, param: float) -> None:
        return
    

    def glLightModelfv_j3(self, pname: int, params: list[float], offset: int) -> None:
        return
    

    def glLightModelfv_j2(self, pname: int, params: FloatBuffer) -> None:
        return

    def glLightModelfv(self, *args):
        return getattr(self, "glLightModelfv_j" + str(len(args)))(*args)
    

    def glLightf(self, light: int, pname: int, param: float) -> None:
        return
    

    def glLightfv_j4(self, light: int, pname: int, params: list[float], offset: int) -> None:
        return
    

    def glLightfv_j3(self, light: int, pname: int, params: FloatBuffer) -> None:
        return

    def glLightfv(self, *args):
        return getattr(self, "glLightfv_j" + str(len(args)))(*args)
    

    def glLineWidth(self, width: float) -> None:
        return
    

    def glLoadIdentity(self) -> None:
        return
    

    def glLoadMatrixf_j2(self, m: list[float], offset: int) -> None:
        return
    

    def glLoadMatrixf_j1(self, m: FloatBuffer) -> None:
        return

    def glLoadMatrixf(self, *args):
        return getattr(self, "glLoadMatrixf_j" + str(len(args)))(*args)
    

    def glLogicOp(self, opcode: int) -> None:
        return
    

    def glMaterialf(self, face: int, pname: int, param: float) -> None:
        return
    

    def glMaterialfv_j4(self, face: int, pname: int, params: list[float], offset: int) -> None:
        return
    

    def glMaterialfv_j3(self, face: int, pname: int, params: FloatBuffer) -> None:
        return

    def glMaterialfv(self, *args):
        return getattr(self, "glMaterialfv_j" + str(len(args)))(*args)
    

    def glMatrixMode(self, mode: int) -> None:
        return
    

    def glMultMatrixf_j2(self, m: list[float], offset: int) -> None:
        return
    

    def glMultMatrixf_j1(self, m: FloatBuffer) -> None:
        return

    def glMultMatrixf(self, *args):
        return getattr(self, "glMultMatrixf_j" + str(len(args)))(*args)
    

    def glMultiTexCoord4f(self, target: int, s: float, t: float, r: float, q: float) -> None:
        return
    

    def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
        return
    

    def glNormalPointer(self, type_: int, stride: int, pointer: Buffer) -> None:
        return
    

    def glOrthof(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> None:
        return
    

    def glPixelStorei(self, pname: int, param: int) -> None:
        return
    

    def glPointSize(self, size: float) -> None:
        return
    

    def glPolygonOffset(self, factor: float, units: float) -> None:
        return
    

    def glPopMatrix(self) -> None:
        return
    

    def glPushMatrix(self) -> None:
        return
    

    def glReadPixels(self, x: int, y: int, width: int, height: int, format: int, type_: int, pixels: Buffer) -> None:
        return
    

    def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
        return
    

    def glRotatex(self, angle: int, x: int, y: int, z: int) -> None:
        return
    

    def glSampleCoverage(self, value: float, invert: bool) -> None:
        return
    

    def glScalef(self, x: float, y: float, z: float) -> None:
        return
    

    def glScalex(self, x: int, y: int, z: int) -> None:
        return
    

    def glScissor(self, x: int, y: int, width: int, height: int) -> None:
        return
    

    def glShadeModel(self, mode: int) -> None:
        return
    

    def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
        return
    

    def glStencilMask(self, mask: int) -> None:
        return
    

    def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
        return
    

    def glTexCoordPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        return
    

    def glTexEnvf(self, target: int, pname: int, param: float) -> None:
        return
    

    def glTexEnvfv_j4(self, target: int, pname: int, params: list[float], offset: int) -> None:
        return
    

    def glTexEnvfv_j3(self, target: int, pname: int, params: FloatBuffer) -> None:
        return

    def glTexEnvfv(self, *args):
        return getattr(self, "glTexEnvfv_j" + str(len(args)))(*args)
    

    def glTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, format: int, type_: int, pixels: Buffer) -> None:
        return
    

    def glTexParameterf(self, target: int, pname: int, param: float) -> None:
        return
    

    def glTexParameteri(self, target: int, pname: int, param: int) -> None:
        return
    

    def glTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, type_: int, pixels: Buffer) -> None:
        return
    

    def glTranslatef(self, x: float, y: float, z: float) -> None:
        return
    

    def glVertexPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        return
    

    def glViewport(self, x: int, y: int, width: int, height: int) -> None:
        return
    

    def glBegin(self, i: int) -> None:
        return
    

    def glEnd(self) -> None:
        return
    

    def glVertex3f(self, f: float, f2: float, f3: float) -> None:
        return
    

    def glPolygonMode(self, i: int, i1: int) -> None:
        return
# from java.nio.Buffer import Buffer
# from java.nio.FloatBuffer import FloatBuffer
# from java.nio.IntBuffer import IntBuffer
# from org.allbinary.logic.string.StringUtil import StringUtil


def _NullGL10_NULL_GL10() -> object:
    return NullGL10()

lazy_static(NullGL10, "NULL_GL10", _NullGL10_NULL_GL10)

