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
from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
from org.allbinary.image.gui.JPanel import JPanel


class ResizeImageJPanel(JPanel, ImageProcessorInputCompositeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageProcessorInput: ImageProcessorInput = None
        self.aboveJButton: JButton = None
        self.adjustFor16AboveJButton: JButton = None
        self.adjustFor16BelowJButton: JButton = None
        self.floatPercentJTextField: JTextField = None
        self.jComboBox1: JComboBox[str] = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.jLabel3: JLabel = None
        self.jTextField1: JTextField = None
        self.jTextField2: JTextField = None
        self.updateJButton: JButton = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        from org.allbinary.image.gui.DefaultComboBoxModel import DefaultComboBoxModel
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.imageProcessorInput = imageProcessorInput
        numberStringArray: list[str] = [None] * (101)
        numberStringArray[0] = str(-1)
        for index in range(1, 100):
            numberStringArray[index] = str(index)
        self.jComboBox1.setModel(DefaultComboBoxModel(numberStringArray))
        araster: Raster = self.imageProcessorInput.getBufferedImageArray()[0].getAlphaRaster()
        if araster is None:
            print("there is no Alpha channel!!!!!!!!!")
        else:
            print("Alpha channel found !")
    

    def process(self) -> None:
        (threading.Thread()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     imageUtil: ImageUtil = ImageUtil.getInstance()
#                     percent: int = str(self.jComboBox1.getSelectedItem())
#                     percentAsFloat: float = float(self.floatPercentJTextField.getText())
#                     imageProcessorInput: ImageProcessorInput = self.getImageProcessorInput()
#                     files: list[File] = imageProcessorInput.getFiles()
#                     generatedBufferedImageArray: list[BufferedImage] = None
#                     if int(percentAsFloat) != -1:
#                         generatedBufferedImageArray = imageUtil.createBufferedImage2(imageProcessorInput.getBufferedImageArray(), percentAsFloat, True)
#                     elif int(percent) != -1:
#                         generatedBufferedImageArray = imageUtil.createBufferedImageForResize(imageProcessorInput.getBufferedImageArray(), percent, True)
#                     else:
#                         width: int = str(self.jTextField1.getText())
#                         height: int = str(self.jTextField2.getText())
#                         generatedBufferedImageArray = imageUtil.createBufferedImage3(imageProcessorInput.getBufferedImageArray(), width, height, True)
#                     araster: Raster = generatedBufferedImageArray[0].getAlphaRaster()
#                     if araster is None:
#                         print("No Alpha Channel In Result")
#                     else:
#                         print("Found Alpha Channel In Result")
#                     imagePersistanceUtil: ImagePersistanceUtil = ImagePersistanceUtil.getInstance()
#                     for index in range(0, len(generatedBufferedImageArray)):
#                         imagePersistanceUtil.saveWithBatik(FileWrapperUtil.wrapFile(files[index]), generatedBufferedImageArray[index])
#                     self.getParent().repaint()
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def update(self) -> None:
        (threading.Thread()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     imageProcessorInput: ImageProcessorInput = self.getImageProcessorInput()
#                     size: int = len(imageProcessorInput.getBufferedImageArray())
#                     bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
#                     bufferedImage: BufferedImage = None
#                     for index in range(0, size):
#                         bufferedImage = bufferedImageArray[0]
#                         self.jTextField1.setText(str(bufferedImage.getWidth()))
#                         self.jTextField2.setText(str(bufferedImage.getHeight()))
#                     self.getParent().repaint()
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def updateFor16Above(self) -> None:
        (threading.Thread()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     imageProcessorInput: ImageProcessorInput = self.getImageProcessorInput()
#                     size: int = len(imageProcessorInput.getBufferedImageArray())
#                     bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
#                     bufferedImage: BufferedImage = None
#                     for index in range(0, size):
#                         bufferedImage = bufferedImageArray[0]
#                         self.jTextField1.setText(str(bufferedImage.getWidth() / 16 * 16))
#                         self.jTextField2.setText(str(bufferedImage.getHeight() / 16 * 16))
#                     self.getParent().repaint()
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def updateFor16Below(self) -> None:
        (threading.Thread()  # Java anonymous class body:
#             
# 
#             def run(self) -> None:
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 try:
#                     imageProcessorInput: ImageProcessorInput = self.getImageProcessorInput()
#                     size: int = len(imageProcessorInput.getBufferedImageArray())
#                     bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
#                     bufferedImage: BufferedImage = None
#                     for index in range(0, size):
#                         bufferedImage = bufferedImageArray[0]
#                         self.jTextField1.setText(str(((bufferedImage.getWidth() / 16) + 1) * 16))
#                         self.jTextField2.setText(str(((bufferedImage.getHeight() / 16) + 1) * 16))
#                     self.getParent().repaint()
#                 except Exception as e:
#                     logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
).start()
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        self.imageProcessorInput = imageProcessorInput
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JComboBox import JComboBox
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.Dimension import Dimension
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        self.jLabel1 = JLabel()
        self.jComboBox1 = JComboBox()
        self.aboveJButton = JButton()
        self.jTextField1 = JTextField()
        self.jLabel2 = JLabel()
        self.jLabel3 = JLabel()
        self.jTextField2 = JTextField()
        self.updateJButton = JButton()
        self.floatPercentJTextField = JTextField()
        self.adjustFor16AboveJButton = JButton()
        self.adjustFor16BelowJButton = JButton()
        self.jLabel1.setText("Percent:")
        self.jComboBox1.setModel(DefaultComboBoxModel(["Item 1", "Item 2", "Item 3", "Item 4"]))
        self.aboveJButton.setText("Process")
        self.aboveJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.aboveJButtonActionPerformed(evt)
))
        self.jLabel2.setText("Width:")
        self.jLabel3.setText("Height:")
        self.updateJButton.setText("Update")
        self.updateJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.updateJButtonActionPerformed(evt)
))
        self.floatPercentJTextField.setText("-1.000000")
        self.floatPercentJTextField.setMinimumSize(Dimension(120, 22))
        self.adjustFor16AboveJButton.setText("Adjust for 16 Above")
        self.adjustFor16AboveJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.adjustFor16AboveJButtonActionPerformed(evt)
))
        self.adjustFor16BelowJButton.setText("Adjust for 16 Below")
        self.adjustFor16BelowJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.adjustFor16BelowJButtonActionPerformed(evt)
))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jLabel1).addComponent(self.jLabel2).addComponent(self.jLabel3)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, False).addComponent(self.jComboBox1, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.jTextField1).addComponent(self.jTextField2)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.floatPercentJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.adjustFor16AboveJButton).addComponent(self.adjustFor16BelowJButton)).addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)).addGroup(layout.createSequentialGroup().addComponent(self.updateJButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.aboveJButton).addGap(0, 250, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.jComboBox1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.floatPercentJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2).addComponent(self.adjustFor16AboveJButton)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel3).addComponent(self.jTextField2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.adjustFor16BelowJButton)).addGap(18, 18, 18).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.aboveJButton).addComponent(self.updateJButton)).addContainerGap(175, Short.MAX_VALUE)))
    

    def aboveJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.process()
    

    def updateJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.update()
    

    def adjustFor16AboveJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.updateFor16Above()
    

    def adjustFor16BelowJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.updateFor16Below()
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.Raster import Raster
# from java.io.File import File
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
from org.allbinary.media.image.ImageUtil import ImageUtil
from org.allbinary.string.CommonStrings import CommonStrings


