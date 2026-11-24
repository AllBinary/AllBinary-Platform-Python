# 
# To change this license header, choose License Headers in Project Properties. 
# To change this template file, choose Tools | Templates 
# and open the template in the editor.  
# Generated Code Do Not Modify
# package org.allbinary.media.image

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ImagePersistanceUtil:
    instance: ImagePersistanceUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ImagePersistanceUtil:
        return ImagePersistanceUtil.instance
    

    # throws Exception
    def saveWithBatik(self, file: AbFile, bufferedImage: BufferedImage) -> None:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.apache.batik.ext.awt.image.codec.png.PNGImageWriter import PNGImageWriter
        batikPNGImageWriter: PNGImageWriter = PNGImageWriter()
        fileOutputStream: AbFileOutputStream = AbFileOutputStream.createFromAbFile(file)
        try:
            batikPNGImageWriter.writeImage(bufferedImage, fileOutputStream)
        finally:
            fileOutputStream.flush()
            StreamUtil.getInstance().close(fileOutputStream)
        self.logUtil.putF("Wrote Image: " + str(file.getAbsolutePath()), self, self.commonStrings.SAVE)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def saveWithImageIO_j2_1(self, filePath: str, bufferedImage: BufferedImage) -> None:
        self.saveWithImageIO(File(filePath), bufferedImage)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def saveWithImageIO_j2_2(self, file: File, bufferedImage: BufferedImage) -> None:
        from java.util.Iterator import Iterator
        writer: ImageWriter = None
        ios: ImageOutputStream = None
        try:
            iter: Iterator = ImageIO.getImageWritersByFormatName("jpeg")
            if not iter.hasNext():
                self.logUtil.putF("Unable to save image to jpeg file type.", self, self.commonStrings.SAVE)
                return
            writer = iter.next()
            ios = ImageIO.createImageOutputStream(file)
            writer.setOutput(ios)
            iwp: ImageWriteParam = writer.getDefaultWriteParam()
            iwp.setCompressionMode(ImageWriteParam.MODE_EXPLICIT)
            iwp.setCompressionQuality(0.95)
            writer.write(None, IIOImage(bufferedImage, None, None), iwp)
            self.logUtil.putF("Wrote Image: " + str(file.getAbsolutePath()), self, self.commonStrings.SAVE)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.SAVE, e)
        finally:
            try:
                if ios is not None:
                    ios.flush()
                    try:
                        if ios is not None:
                            self.logUtil.putF(str(ios), ios, self.commonStrings.CLOSE)
                            ios.close()
                    except Exception as e:
                        self.logUtil.put(self.commonStrings.EXCEPTION, ios, self.commonStrings.CLOSE, e)
                if writer is not None:
                    writer.dispose()
            except OSError as e2:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.SAVE, e2)

    def saveWithImageIO(self, *args):
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], str)) and not isinstance(args[1], (str, list, int, float)):
            return self.saveWithImageIO_j2_1(*args)
        if len(args) == 2:
            return self.saveWithImageIO_j2_2(*args)
        return getattr(self, "saveWithImageIO_j" + str(len(args)))(*args)
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.File import File
# from java.io.IOException import IOException
# from java.util.Iterator import Iterator
# from javax.imageio.IIOImage import IIOImage
# from javax.imageio.ImageIO import ImageIO
# from javax.imageio.ImageWriteParam import ImageWriteParam
# from javax.imageio.ImageWriter import ImageWriter
# from javax.imageio.stream.ImageOutputStream import ImageOutputStream
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.apache.batik.ext.awt.image.codec.png.PNGImageWriter import PNGImageWriter


def _ImagePersistanceUtil_instance() -> object:
    return ImagePersistanceUtil()

lazy_static(ImagePersistanceUtil, "instance", _ImagePersistanceUtil_instance)

