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

from java.lang.System import System
from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class ResizeImageJPanel(*java_bases(JPanel, ImageProcessorInputCompositeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("imageProcessorInput", None)
        vars(self).setdefault("aboveJButton", None)
        vars(self).setdefault("adjustFor16AboveJButton", None)
        vars(self).setdefault("adjustFor16BelowJButton", None)
        vars(self).setdefault("floatPercentJTextField", None)
        vars(self).setdefault("jComboBox1", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("jLabel3", None)
        vars(self).setdefault("jTextField1", None)
        vars(self).setdefault("jTextField2", None)
        vars(self).setdefault("updateJButton", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "imageProcessorInput" not in vars(self): self.imageProcessorInput: ImageProcessorInput = None
        if "aboveJButton" not in vars(self): self.aboveJButton: JButton = None
        if "adjustFor16AboveJButton" not in vars(self): self.adjustFor16AboveJButton: JButton = None
        if "adjustFor16BelowJButton" not in vars(self): self.adjustFor16BelowJButton: JButton = None
        if "floatPercentJTextField" not in vars(self): self.floatPercentJTextField: JTextField = None
        if "jComboBox1" not in vars(self): self.jComboBox1: JComboBox[str] = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "jLabel3" not in vars(self): self.jLabel3: JLabel = None
        if "jTextField1" not in vars(self): self.jTextField1: JTextField = None
        if "jTextField2" not in vars(self): self.jTextField2: JTextField = None
        if "updateJButton" not in vars(self): self.updateJButton: JButton = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        super().__init__()
        __class__._init_fields(self)
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
        from java.io.File import File
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        from org.allbinary.media.image.ImageUtil import ImageUtil
        _java_listener_owner = self
        class _JavaListenerN66834(Thread):
            
            

            def run(self) -> None:
                from java.io.File import File
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
                from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
                from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
                from org.allbinary.media.image.ImageUtil import ImageUtil
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    imageUtil: ImageUtil = ImageUtil.getInstance()
                    percent: int = str(_java_listener_owner.jComboBox1.getSelectedItem())
                    percentAsFloat: float = float(_java_listener_owner.floatPercentJTextField.getText())
                    imageProcessorInput: ImageProcessorInput = _java_listener_owner.getImageProcessorInput()
                    files: list[File] = imageProcessorInput.getFiles()
                    generatedBufferedImageArray: list[BufferedImage] = None
                    if int(percentAsFloat) != -1:
                        generatedBufferedImageArray = imageUtil.createBufferedImage2(imageProcessorInput.getBufferedImageArray(), percentAsFloat, True)
                    elif int(percent) != -1:
                        generatedBufferedImageArray = imageUtil.createBufferedImageForResize(imageProcessorInput.getBufferedImageArray(), percent, True)
                    else:
                        width: int = str(_java_listener_owner.jTextField1.getText())
                        height: int = str(_java_listener_owner.jTextField2.getText())
                        generatedBufferedImageArray = imageUtil.createBufferedImage3(imageProcessorInput.getBufferedImageArray(), width, height, True)
                    araster: Raster = generatedBufferedImageArray[0].getAlphaRaster()
                    if araster is None:
                        print("No Alpha Channel In Result")
                    else:
                        print("Found Alpha Channel In Result")
                    imagePersistanceUtil: ImagePersistanceUtil = ImagePersistanceUtil.getInstance()
                    for index in range(0, len(generatedBufferedImageArray)):
                        imagePersistanceUtil.saveWithBatik(FileWrapperUtil.wrapFile(files[index]), generatedBufferedImageArray[index])
                    _java_listener_owner.getParent().repaint()
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN66834()
            .start()
    

    def update(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        _java_listener_owner = self
        class _JavaListenerN68307(Thread):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    imageProcessorInput: ImageProcessorInput = _java_listener_owner.getImageProcessorInput()
                    size: int = len(imageProcessorInput.getBufferedImageArray())
                    bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
                    bufferedImage: BufferedImage = None
                    for index in range(0, size):
                        bufferedImage = bufferedImageArray[0]
                        _java_listener_owner.jTextField1.setText(str(bufferedImage.getWidth()))
                        _java_listener_owner.jTextField2.setText(str(bufferedImage.getHeight()))
                    _java_listener_owner.getParent().repaint()
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN68307()
            .start()
    

    def updateFor16Above(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        _java_listener_owner = self
        class _JavaListenerN69006(Thread):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    imageProcessorInput: ImageProcessorInput = _java_listener_owner.getImageProcessorInput()
                    size: int = len(imageProcessorInput.getBufferedImageArray())
                    bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
                    bufferedImage: BufferedImage = None
                    for index in range(0, size):
                        bufferedImage = bufferedImageArray[0]
                        _java_listener_owner.jTextField1.setText(str(java_divide(bufferedImage.getWidth(), 16)
             * 16))
                        _java_listener_owner.jTextField2.setText(str(java_divide(bufferedImage.getHeight(), 16)
             * 16))
                    _java_listener_owner.getParent().repaint()
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN69006()
            .start()
    

    def updateFor16Below(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        _java_listener_owner = self
        class _JavaListenerN69741(Thread):
            
            

            def run(self) -> None:
                from org.allbinary.logic.communication.log.LogUtil import LogUtil
                from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    imageProcessorInput: ImageProcessorInput = _java_listener_owner.getImageProcessorInput()
                    size: int = len(imageProcessorInput.getBufferedImageArray())
                    bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
                    bufferedImage: BufferedImage = None
                    for index in range(0, size):
                        bufferedImage = bufferedImageArray[0]
                        _java_listener_owner.jTextField1.setText(str(((java_divide(bufferedImage.getWidth(), 16)
            ) + 1) * 16))
                        _java_listener_owner.jTextField2.setText(str(((java_divide(bufferedImage.getHeight(), 16)
            ) + 1) * 16))
                    _java_listener_owner.getParent().repaint()
                except Exception as e:
                    logUtil.put(_java_listener_owner.commonStrings.EXCEPTION, self, _java_listener_owner.commonStrings.RUN, e)
        _JavaListenerN69741()
            .start()
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        self.imageProcessorInput = imageProcessorInput
    

    def initComponents(self) -> None:
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
        _java_listener_owner = self
        class _JavaListenerN71139(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "aboveJButtonActionPerformed") else _java_listener_owner).aboveJButtonActionPerformed(evt)
        self.aboveJButton.addActionListener(_JavaListenerN71139()
            )
        self.jLabel2.setText("Width:")
        self.jLabel3.setText("Height:")
        self.updateJButton.setText("Update")
        _java_listener_owner = self
        class _JavaListenerN71338(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "updateJButtonActionPerformed") else _java_listener_owner).updateJButtonActionPerformed(evt)
        self.updateJButton.addActionListener(_JavaListenerN71338()
            )
        self.floatPercentJTextField.setText("-1.000000")
        self.floatPercentJTextField.setMinimumSize(Dimension(120, 22))
        self.adjustFor16AboveJButton.setText("Adjust for 16 Above")
        _java_listener_owner = self
        class _JavaListenerN71556(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "adjustFor16AboveJButtonActionPerformed") else _java_listener_owner).adjustFor16AboveJButtonActionPerformed(evt)
        self.adjustFor16AboveJButton.addActionListener(_JavaListenerN71556()
            )
        self.adjustFor16BelowJButton.setText("Adjust for 16 Below")
        _java_listener_owner = self
        class _JavaListenerN71695(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "adjustFor16BelowJButtonActionPerformed") else _java_listener_owner).adjustFor16BelowJButtonActionPerformed(evt)
        self.adjustFor16BelowJButton.addActionListener(_JavaListenerN71695()
            )
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.jLabel1).addComponent(self.jLabel2).addComponent(self.jLabel3)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING, False).addComponent(self.jComboBox1, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.jTextField1).addComponent(self.jTextField2)).addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.floatPercentJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.adjustFor16AboveJButton).addComponent(self.adjustFor16BelowJButton)).addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)).addGroup(layout.createSequentialGroup().addComponent(self.updateJButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.aboveJButton).addGap(0, 250, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.jComboBox1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.floatPercentJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jTextField1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel2).addComponent(self.adjustFor16AboveJButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel3).addComponent(self.jTextField2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addComponent(self.adjustFor16BelowJButton)).addGap(18, 18, 18).addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.aboveJButton).addComponent(self.updateJButton)).addContainerGap(175, Short.MAX_VALUE)))
    

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
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
# from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageUtil import ImageUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.DefaultComboBoxModel import DefaultComboBoxModel
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JComboBox import JComboBox
# from javax.swing.JLabel import JLabel
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle


