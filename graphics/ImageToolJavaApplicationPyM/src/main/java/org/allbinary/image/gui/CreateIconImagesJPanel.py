# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.image.gui

from __future__ import annotations

import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
# from javax.swing.JPanel import JPanel


class CreateIconImagesJPanel(*java_bases(JPanel, ImageProcessorInputCompositeInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageProcessorInput: ImageProcessorInput = None
        self.aboveJButton: JButton = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.imageProcessorInput = imageProcessorInput
        numberStringArray: list[str] = [None] * (101)
        numberStringArray[0] = str(-1)
        for index in range(1, 100):
            numberStringArray[index] = str(index)
        araster: Raster = self.imageProcessorInput.getBufferedImageArray()[0].getAlphaRaster()
        if araster is None:
            print("there is no Alpha channel!!!!!!!!!")
        else:
            print("Alpha channel found !")
    

    def process(self) -> None:
        from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        from org.allbinary.media.image.ImageUtil import ImageUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        (threading.Thread()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
#                 from org.allbinary.logic.communication.log.LogUtil import LogUtil
#                 from org.allbinary.logic.io.file.AbFile import AbFile
#                 from org.allbinary.logic.string.StringMaker import StringMaker
#                 from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
#                 from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
#                 from org.allbinary.media.image.ImageUtil import ImageUtil
#                 from org.allbinary.util.BasicArrayList import BasicArrayList
#                 from org.allbinary.util.BasicArrayListD import BasicArrayListD
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     imageUtil: ImageUtil = ImageUtil.getInstance()
#                     stringMaker: StringMaker = StringMaker()
#                     imageProcessorInput: ImageProcessorInput = self.getImageProcessorInput()
#                     files: list[File] = imageProcessorInput.getFiles()
#                     iconWidthList: BasicArrayList = BasicArrayListD()
#                     iconHeightList: BasicArrayList = BasicArrayListD()
#                     iconWidthList.add(864)
#                     iconHeightList.add(864)
#                     ANDROID: str = "android-icon-"
#                     IOS: str = "ios-icon-"
#                     size: int = iconWidthList.size()
#                     width: int = 0
#                     height: int = 0
#                     for index2 in range(0, size):
#                         width = int((iconWidthList.get(index2)))
#                         height = int((iconHeightList.get(index2)))
#                         generatedBufferedImageArray: list[BufferedImage] = imageUtil.createBufferedImage3(imageProcessorInput.getBufferedImageArray(), width, height, True)
#                         imagePersistanceUtil: ImagePersistanceUtil = ImagePersistanceUtil.getInstance()
#                         for index in range(0, len(generatedBufferedImageArray)):
#                             filePath: str = files[index].getAbsolutePath()
#                             endIndex: int = filePath.rfind('\\')
#                             path: str = filePath[0:endIndex + 1]
#                             stringMaker.delete(0, stringMaker.length())
#                             stringMaker.append(path).append(ANDROID).appendint(width).append(CanvasStrings.getInstance()._PNG)
#                             newFilePath: str = str(stringMaker)
#                             imagePersistanceUtil.saveWithBatik(AbFile.createAbFile(newFilePath), generatedBufferedImageArray[index])
#                             stringMaker.delete(0, stringMaker.length())
#                             stringMaker.append(path).append(IOS).appendint(width).append(CanvasStrings.getInstance()._PNG)
#                             newFilePath = str(stringMaker)
#                             imagePersistanceUtil.saveWithBatik(AbFile.createAbFile(newFilePath), generatedBufferedImageArray[index])
#                     self.getParent().repaint()
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        self.imageProcessorInput = imageProcessorInput
    

    def initComponents(self) -> None:
        self.aboveJButton = JButton()
        self.aboveJButton.setText("Process")
        self.aboveJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.aboveJButtonActionPerformed(evt)
))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.aboveJButton).addGap(0, 335, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addComponent(self.aboveJButton).addContainerGap(286, Short.MAX_VALUE)))
    

    def aboveJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.Raster import Raster
# from java.io.File import File
# from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageUtil import ImageUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton


