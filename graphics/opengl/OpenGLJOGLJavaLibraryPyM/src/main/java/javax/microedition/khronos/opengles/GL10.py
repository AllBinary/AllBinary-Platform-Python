# Generated Code Do Not Modify
# package javax.microedition.khronos.opengles

from __future__ import annotations

from javax.microedition.khronos.opengles.GL import GL


# Java interface
class GL10(GL):
    GL_ADD: int = 260
    GL_ALIASED_LINE_WIDTH_RANGE: int = 33902
    GL_ALIASED_POINT_SIZE_RANGE: int = 33901
    GL_ALPHA: int = 6406
    GL_ALPHA_BITS: int = 3413
    GL_ALPHA_TEST: int = 3008
    GL_ALWAYS: int = 519
    GL_AMBIENT: int = 4608
    GL_AMBIENT_AND_DIFFUSE: int = 5634
    GL_AND: int = 5377
    GL_AND_INVERTED: int = 5380
    GL_AND_REVERSE: int = 5378
    GL_BACK: int = 1029
    GL_BLEND: int = 3042
    GL_BLUE_BITS: int = 3412
    GL_BYTE: int = 5120
    GL_CCW: int = 2305
    GL_CLAMP_TO_EDGE: int = 33071
    GL_CLEAR: int = 5376
    GL_COLOR_ARRAY: int = 32886
    GL_COLOR_BUFFER_BIT: int = 16384
    GL_COLOR_LOGIC_OP: int = 3058
    GL_COLOR_MATERIAL: int = 2903
    GL_COMPRESSED_TEXTURE_FORMATS: int = 34467
    GL_CONSTANT_ATTENUATION: int = 4615
    GL_COPY: int = 5379
    GL_COPY_INVERTED: int = 5388
    GL_CULL_FACE: int = 2884
    GL_CW: int = 2304
    GL_DECAL: int = 8449
    GL_DECR: int = 7683
    GL_DEPTH_BITS: int = 3414
    GL_DEPTH_BUFFER_BIT: int = 256
    GL_DEPTH_TEST: int = 2929
    GL_DIFFUSE: int = 4609
    GL_DITHER: int = 3024
    GL_DONT_CARE: int = 4352
    GL_DST_ALPHA: int = 772
    GL_DST_COLOR: int = 774
    GL_EMISSION: int = 5632
    GL_EQUAL: int = 514
    GL_EQUIV: int = 5385
    GL_EXP: int = 2048
    GL_EXP2: int = 2049
    GL_EXTENSIONS: int = 7939
    GL_FALSE: int = 0
    GL_FASTEST: int = 4353
    GL_FIXED: int = 5132
    GL_FLAT: int = 7424
    GL_FLOAT: int = 5126
    GL_FOG: int = 2912
    GL_FOG_COLOR: int = 2918
    GL_FOG_DENSITY: int = 2914
    GL_FOG_END: int = 2916
    GL_FOG_HINT: int = 3156
    GL_FOG_MODE: int = 2917
    GL_FOG_START: int = 2915
    GL_FRONT: int = 1028
    GL_FRONT_AND_BACK: int = 1032
    GL_GEQUAL: int = 518
    GL_GREATER: int = 516
    GL_GREEN_BITS: int = 3411
    GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES: int = 35739
    GL_IMPLEMENTATION_COLOR_READ_TYPE_OES: int = 35738
    GL_INCR: int = 7682
    GL_INVALID_ENUM: int = 1280
    GL_INVALID_OPERATION: int = 1282
    GL_INVALID_VALUE: int = 1281
    GL_INVERT: int = 5386
    GL_KEEP: int = 7680
    GL_LEQUAL: int = 515
    GL_LESS: int = 513
    GL_LIGHT_MODEL_AMBIENT: int = 2899
    GL_LIGHT_MODEL_TWO_SIDE: int = 2898
    GL_LIGHT0: int = 16384
    GL_LIGHT1: int = 16385
    GL_LIGHT2: int = 16386
    GL_LIGHT3: int = 16387
    GL_LIGHT4: int = 16388
    GL_LIGHT5: int = 16389
    GL_LIGHT6: int = 16390
    GL_LIGHT7: int = 16391
    GL_LIGHTING: int = 2896
    GL_LINE_LOOP: int = 2
    GL_LINE_SMOOTH: int = 2848
    GL_LINE_SMOOTH_HINT: int = 3154
    GL_LINE_STRIP: int = 3
    GL_LINEAR: int = 9729
    GL_LINEAR_ATTENUATION: int = 4616
    GL_LINEAR_MIPMAP_LINEAR: int = 9987
    GL_LINEAR_MIPMAP_NEAREST: int = 9985
    GL_LINES: int = 1
    GL_LUMINANCE: int = 6409
    GL_LUMINANCE_ALPHA: int = 6410
    GL_MAX_ELEMENTS_INDICES: int = 33001
    GL_MAX_ELEMENTS_VERTICES: int = 33000
    GL_MAX_LIGHTS: int = 3377
    GL_MAX_MODELVIEW_STACK_DEPTH: int = 3382
    GL_MAX_PROJECTION_STACK_DEPTH: int = 3384
    GL_MAX_TEXTURE_SIZE: int = 3379
    GL_MAX_TEXTURE_STACK_DEPTH: int = 3385
    GL_MAX_TEXTURE_UNITS: int = 34018
    GL_MAX_VIEWPORT_DIMS: int = 3386
    GL_MODELVIEW: int = 5888
    GL_MODULATE: int = 8448
    GL_MULTISAMPLE: int = 32925
    GL_NAND: int = 5390
    GL_NEAREST: int = 9728
    GL_NEAREST_MIPMAP_LINEAR: int = 9986
    GL_NEAREST_MIPMAP_NEAREST: int = 9984
    GL_NEVER: int = 512
    GL_NICEST: int = 4354
    GL_NO_ERROR: int = 0
    GL_NOOP: int = 5381
    GL_NOR: int = 5384
    GL_NORMAL_ARRAY: int = 32885
    GL_NORMALIZE: int = 2977
    GL_NOTEQUAL: int = 517
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: int = 34466
    GL_ONE: int = 1
    GL_ONE_MINUS_DST_ALPHA: int = 773
    GL_ONE_MINUS_DST_COLOR: int = 775
    GL_ONE_MINUS_SRC_ALPHA: int = 771
    GL_ONE_MINUS_SRC_COLOR: int = 769
    GL_OR: int = 5383
    GL_OR_INVERTED: int = 5389
    GL_OR_REVERSE: int = 5387
    GL_OUT_OF_MEMORY: int = 1285
    GL_PACK_ALIGNMENT: int = 3333
    GL_PALETTE4_R5_G6_B5_OES: int = 35730
    GL_PALETTE4_RGB5_A1_OES: int = 35732
    GL_PALETTE4_RGB8_OES: int = 35728
    GL_PALETTE4_RGBA4_OES: int = 35731
    GL_PALETTE4_RGBA8_OES: int = 35729
    GL_PALETTE8_R5_G6_B5_OES: int = 35735
    GL_PALETTE8_RGB5_A1_OES: int = 35737
    GL_PALETTE8_RGB8_OES: int = 35733
    GL_PALETTE8_RGBA4_OES: int = 35736
    GL_PALETTE8_RGBA8_OES: int = 35734
    GL_PERSPECTIVE_CORRECTION_HINT: int = 3152
    GL_POINT_SMOOTH: int = 2832
    GL_POINT_SMOOTH_HINT: int = 3153
    GL_POINTS: int = 0
    GL_POINT_FADE_THRESHOLD_SIZE: int = 33064
    GL_POINT_SIZE: int = 2833
    GL_POLYGON_OFFSET_FILL: int = 32823
    GL_POLYGON_SMOOTH_HINT: int = 3155
    GL_POSITION: int = 4611
    GL_PROJECTION: int = 5889
    GL_QUADRATIC_ATTENUATION: int = 4617
    GL_RED_BITS: int = 3410
    GL_RENDERER: int = 7937
    GL_REPEAT: int = 10497
    GL_REPLACE: int = 7681
    GL_RESCALE_NORMAL: int = 32826
    GL_RGB: int = 6407
    GL_RGBA: int = 6408
    GL_SAMPLE_ALPHA_TO_COVERAGE: int = 32926
    GL_SAMPLE_ALPHA_TO_ONE: int = 32927
    GL_SAMPLE_COVERAGE: int = 32928
    GL_SCISSOR_TEST: int = 3089
    GL_SET: int = 5391
    GL_SHININESS: int = 5633
    GL_SHORT: int = 5122
    GL_SMOOTH: int = 7425
    GL_SMOOTH_LINE_WIDTH_RANGE: int = 2850
    GL_SMOOTH_POINT_SIZE_RANGE: int = 2834
    GL_SPECULAR: int = 4610
    GL_SPOT_CUTOFF: int = 4614
    GL_SPOT_DIRECTION: int = 4612
    GL_SPOT_EXPONENT: int = 4613
    GL_SRC_ALPHA: int = 770
    GL_SRC_ALPHA_SATURATE: int = 776
    GL_SRC_COLOR: int = 768
    GL_STACK_OVERFLOW: int = 1283
    GL_STACK_UNDERFLOW: int = 1284
    GL_STENCIL_BITS: int = 3415
    GL_STENCIL_BUFFER_BIT: int = 1024
    GL_STENCIL_TEST: int = 2960
    GL_SUBPIXEL_BITS: int = 3408
    GL_TEXTURE: int = 5890
    GL_TEXTURE_2D: int = 3553
    GL_TEXTURE_COORD_ARRAY: int = 32888
    GL_TEXTURE_ENV: int = 8960
    GL_TEXTURE_ENV_COLOR: int = 8705
    GL_TEXTURE_ENV_MODE: int = 8704
    GL_TEXTURE_MAG_FILTER: int = 10240
    GL_TEXTURE_MIN_FILTER: int = 10241
    GL_TEXTURE_WRAP_S: int = 10242
    GL_TEXTURE_WRAP_T: int = 10243
    GL_TEXTURE0: int = 33984
    GL_TEXTURE1: int = 33985
    GL_TEXTURE2: int = 33986
    GL_TEXTURE3: int = 33987
    GL_TEXTURE4: int = 33988
    GL_TEXTURE5: int = 33989
    GL_TEXTURE6: int = 33990
    GL_TEXTURE7: int = 33991
    GL_TEXTURE8: int = 33992
    GL_TEXTURE9: int = 33993
    GL_TEXTURE10: int = 33994
    GL_TEXTURE11: int = 33995
    GL_TEXTURE12: int = 33996
    GL_TEXTURE13: int = 33997
    GL_TEXTURE14: int = 33998
    GL_TEXTURE15: int = 33999
    GL_TEXTURE16: int = 34000
    GL_TEXTURE17: int = 34001
    GL_TEXTURE18: int = 34002
    GL_TEXTURE19: int = 34003
    GL_TEXTURE20: int = 34004
    GL_TEXTURE21: int = 34005
    GL_TEXTURE22: int = 34006
    GL_TEXTURE23: int = 34007
    GL_TEXTURE24: int = 34008
    GL_TEXTURE25: int = 34009
    GL_TEXTURE26: int = 34010
    GL_TEXTURE27: int = 34011
    GL_TEXTURE28: int = 34012
    GL_TEXTURE29: int = 34013
    GL_TEXTURE30: int = 34014
    GL_TEXTURE31: int = 34015
    GL_TRIANGLE_FAN: int = 6
    GL_TRIANGLE_STRIP: int = 5
    GL_TRIANGLES: int = 4
    GL_TRUE: int = 1
    GL_UNPACK_ALIGNMENT: int = 3317
    GL_UNSIGNED_BYTE: int = 5121
    GL_UNSIGNED_SHORT: int = 5123
    GL_UNSIGNED_SHORT_4_4_4_4: int = 32819
    GL_UNSIGNED_SHORT_5_5_5_1: int = 32820
    GL_UNSIGNED_SHORT_5_6_5: int = 33635
    GL_VENDOR: int = 7936
    GL_VERSION: int = 7938
    GL_VERTEX_ARRAY: int = 32884
    GL_XOR: int = 5382
    GL_ZERO: int = 0
    

    def glActiveTexture(self, texture: int) -> None:
        raise NotImplementedError()
    

    def glAlphaFunc(self, func: int, ref: float) -> None:
        raise NotImplementedError()
    

    def glBindTexture(self, target: int, texture: int) -> None:
        raise NotImplementedError()
    

    def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
        raise NotImplementedError()
    

    def glClear(self, mask: int) -> None:
        raise NotImplementedError()
    

    def glClearColor(self, red: float, green: float, blue: float, alpha: float) -> None:
        raise NotImplementedError()
    

    def glClearDepthf(self, depth: float) -> None:
        raise NotImplementedError()
    

    def glClearStencil(self, s: int) -> None:
        raise NotImplementedError()
    

    def glClientActiveTexture(self, texture: int) -> None:
        raise NotImplementedError()
    

    def glColor4f(self, red: float, green: float, blue: float, alpha: float) -> None:
        raise NotImplementedError()
    

    def glColorMask(self, red: bool, green: bool, blue: bool, alpha: bool) -> None:
        raise NotImplementedError()
    

    def glColorPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        raise NotImplementedError()
    

    def glCompressedTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, imageSize: int, data: Buffer) -> None:
        raise NotImplementedError()
    

    def glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, imageSize: int, data: Buffer) -> None:
        raise NotImplementedError()
    

    def glCopyTexImage2D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, height: int, border: int) -> None:
        raise NotImplementedError()
    

    def glCopyTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, x: int, y: int, width: int, height: int) -> None:
        raise NotImplementedError()
    

    def glCullFace(self, mode: int) -> None:
        raise NotImplementedError()
    

    def glDeleteTextures(self, n: int, textures: list[int], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glDeleteTextures(self, n: int, textures: IntBuffer) -> None:
        raise NotImplementedError()
    

    def glDepthFunc(self, func: int) -> None:
        raise NotImplementedError()
    

    def glDepthMask(self, flag: bool) -> None:
        raise NotImplementedError()
    

    def glDepthRangef(self, zNear: float, zFar: float) -> None:
        raise NotImplementedError()
    

    def glDisable(self, cap: int) -> None:
        raise NotImplementedError()
    

    def glDisableClientState(self, array: int) -> None:
        raise NotImplementedError()
    

    def glDrawArrays(self, mode: int, first: int, count: int) -> None:
        raise NotImplementedError()
    

    def glDrawElements(self, mode: int, count: int, type_: int, indices: Buffer) -> None:
        raise NotImplementedError()
    

    def glEnable(self, cap: int) -> None:
        raise NotImplementedError()
    

    def glEnableClientState(self, array: int) -> None:
        raise NotImplementedError()
    

    def glFinish(self) -> None:
        raise NotImplementedError()
    

    def glFlush(self) -> None:
        raise NotImplementedError()
    

    def glFogf(self, pname: int, param: float) -> None:
        raise NotImplementedError()
    

    def glFogfv(self, pname: int, params: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glFogfv(self, pname: int, params: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glFrontFace(self, mode: int) -> None:
        raise NotImplementedError()
    

    def glFrustumf(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> None:
        raise NotImplementedError()
    

    def glGenTextures(self, n: int, textures: list[int], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glGenTextures(self, n: int, textures: IntBuffer) -> None:
        raise NotImplementedError()
    

    def glGetError(self) -> int:
        raise NotImplementedError()
    

    def glGetIntegerv(self, pname: int, params: list[int], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glGetIntegerv(self, pname: int, params: IntBuffer) -> None:
        raise NotImplementedError()
    

    def glGetString(self, name: int) -> str:
        raise NotImplementedError()
    

    def glHint(self, target: int, mode: int) -> None:
        raise NotImplementedError()
    

    def glLightModelf(self, pname: int, param: float) -> None:
        raise NotImplementedError()
    

    def glLightModelfv(self, pname: int, params: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glLightModelfv(self, pname: int, params: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glLightf(self, light: int, pname: int, param: float) -> None:
        raise NotImplementedError()
    

    def glLightfv(self, light: int, pname: int, params: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glLightfv(self, light: int, pname: int, params: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glLineWidth(self, width: float) -> None:
        raise NotImplementedError()
    

    def glLoadIdentity(self) -> None:
        raise NotImplementedError()
    

    def glLoadMatrixf(self, m: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glLoadMatrixf(self, m: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glLogicOp(self, opcode: int) -> None:
        raise NotImplementedError()
    

    def glMaterialf(self, face: int, pname: int, param: float) -> None:
        raise NotImplementedError()
    

    def glMaterialfv(self, face: int, pname: int, params: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glMaterialfv(self, face: int, pname: int, params: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glMatrixMode(self, mode: int) -> None:
        raise NotImplementedError()
    

    def glMultMatrixf(self, m: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glMultMatrixf(self, m: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glMultiTexCoord4f(self, target: int, s: float, t: float, r: float, q: float) -> None:
        raise NotImplementedError()
    

    def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
        raise NotImplementedError()
    

    def glNormalPointer(self, type_: int, stride: int, pointer: Buffer) -> None:
        raise NotImplementedError()
    

    def glOrthof(self, left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> None:
        raise NotImplementedError()
    

    def glPixelStorei(self, pname: int, param: int) -> None:
        raise NotImplementedError()
    

    def glPointSize(self, size: float) -> None:
        raise NotImplementedError()
    

    def glPolygonOffset(self, factor: float, units: float) -> None:
        raise NotImplementedError()
    

    def glPopMatrix(self) -> None:
        raise NotImplementedError()
    

    def glPushMatrix(self) -> None:
        raise NotImplementedError()
    

    def glReadPixels(self, x: int, y: int, width: int, height: int, format: int, type_: int, pixels: Buffer) -> None:
        raise NotImplementedError()
    

    def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
        raise NotImplementedError()
    

    def glRotatex(self, angle: int, x: int, y: int, z: int) -> None:
        raise NotImplementedError()
    

    def glSampleCoverage(self, value: float, invert: bool) -> None:
        raise NotImplementedError()
    

    def glScalef(self, x: float, y: float, z: float) -> None:
        raise NotImplementedError()
    

    def glScalex(self, x: int, y: int, z: int) -> None:
        raise NotImplementedError()
    

    def glScissor(self, x: int, y: int, width: int, height: int) -> None:
        raise NotImplementedError()
    

    def glShadeModel(self, mode: int) -> None:
        raise NotImplementedError()
    

    def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
        raise NotImplementedError()
    

    def glStencilMask(self, mask: int) -> None:
        raise NotImplementedError()
    

    def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
        raise NotImplementedError()
    

    def glTexCoordPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        raise NotImplementedError()
    

    def glTexEnvf(self, target: int, pname: int, param: float) -> None:
        raise NotImplementedError()
    

    def glTexEnvfv(self, target: int, pname: int, params: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glTexEnvfv(self, target: int, pname: int, params: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, format: int, type_: int, pixels: Buffer) -> None:
        raise NotImplementedError()
    

    def glTexParameterf(self, target: int, pname: int, param: float) -> None:
        raise NotImplementedError()
    

    def glTexParameteri(self, target: int, pname: int, param: int) -> None:
        raise NotImplementedError()
    

    def glTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, type_: int, pixels: Buffer) -> None:
        raise NotImplementedError()
    

    def glTranslatef(self, x: float, y: float, z: float) -> None:
        raise NotImplementedError()
    

    def glVertexPointer(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        raise NotImplementedError()
    

    def glViewport(self, x: int, y: int, width: int, height: int) -> None:
        raise NotImplementedError()
    

    def glBegin(self, i: int) -> None:
        raise NotImplementedError()
    

    def glEnd(self) -> None:
        raise NotImplementedError()
    

    def glVertex3f(self, f: float, f2: float, f3: float) -> None:
        raise NotImplementedError()
    

    def glPolygonMode(self, i: int, i1: int) -> None:
        raise NotImplementedError()


