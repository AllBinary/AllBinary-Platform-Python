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
# package org.allbinary.image.gui

from __future__ import annotations

from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
from org.allbinary.image.gui.JPanel import JPanel


class ImageUnifierJPanel(JPanel, ImageProcessorInputCompositeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageStrings: ImageStrings = ImageStrings.getInstance()
        self.imagesRatioUtil: ImagesRatioUtil = ImagesRatioUtil.getInstance()
        self.imageProcessorInput: ImageProcessorInput = None
        self.icon: list[ImageIconUnique] = None
        self.imageUnifierProperties: ImageUnifierProperties = None
        self.result: BufferedImage = None
        self.isImageFillIn: bool = True
        self.avgRatioJTextField: JTextField = None
        self.cellHeightJTextField: JTextField = None
        self.cellRatioJTextField: JTextField = None
        self.cellWidthJTextField: JTextField = None
        self.columnsJTextField: JTextField = None
        self.downJButton: JButton = None
        self.fudgeItJButton: JButton = None
        self.imageJList: JList = None
        self.jButton1: JButton = None
        self.jButton2: JButton = None
        self.jButtonOrder: JButton = None
        self.jLabel1: JLabel = None
        self.jLabel2: JLabel = None
        self.jLabel3: JLabel = None
        self.jLabel4: JLabel = None
        self.jLabel5: JLabel = None
        self.jLabel6: JLabel = None
        self.jPanel1: JPanel = None
        self.jScrollPane1: JScrollPane = None
        self.jScrollPane2: JScrollPane = None
        self.rowsJTextField: JTextField = None
        self.upJButton: JButton = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        self.setImageProcessorInput(imageProcessorInput)
    

    def init(self) -> None:
        from org.allbinary.image.gui.DefaultListModel import DefaultListModel
        from org.allbinary.image.gui.ImageIconUnique import ImageIconUnique
        try:
            imageProcessorInput: ImageProcessorInput = self.getImageProcessorInput()
            bufferedImageArray: list[BufferedImage] = imageProcessorInput.getBufferedImageArray()
            self.icon = [None] * (len(bufferedImageArray))
            defaultListModel: DefaultListModel = DefaultListModel()
            for index in range(0, len(bufferedImageArray)):
                width: float = bufferedImageArray[index].getWidth()
                height: float = bufferedImageArray[index].getHeight()
                newWidth: int = 52
                oldRatio: float = width / height
                newHeight: int = int((float(newWidth) / oldRatio))
                iconBufferedImage: BufferedImage = ImageUtil.getInstance().createBufferedImage(bufferedImageArray[index], newWidth, newHeight, True)
                self.icon[index] = ImageIconUnique(iconBufferedImage, index)
                defaultListModel.addElement(self.icon[index])
            self.imageJList.setModel(defaultListModel)
            self.updateOnPropertiesChange()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
    

    def updateImage(self) -> None:
        try:
            bufferedImageArray: list[BufferedImage] = self.getImageProcessorInput().getBufferedImageArray()
            tempBufferedImageArray: list[BufferedImage] = [None] * (len(bufferedImageArray))
            for index in range(0, len(bufferedImageArray)):
                indexedImageIcon: ImageIconUnique = self.imageJList.getModel().getElementAt(index)
                bufferedImage: BufferedImage = ImageUtil.getInstance().createBufferedImage(bufferedImageArray[indexedImageIcon.getId()], self.imageUnifierProperties.getImageUnifierCell().getWidth(), self.imageUnifierProperties.getImageUnifierCell().getHeight(), False)
                tempBufferedImageArray[index] = bufferedImage
            totalImages: int = self.imageUnifierProperties.getRows() * self.imageUnifierProperties.getColumns()
            averageRatio: float = self.imagesRatioUtil.getAverage(tempBufferedImageArray, totalImages)
            averageRatioString: str = str(float(averageRatio))
            if len(averageRatioString) > 4:
                averageRatioString = averageRatioString[0:4]
            self.avgRatioJTextField.setText(averageRatioString)
            self.fudgeItJButton.setEnabled(False)
            if not self.imagesRatioUtil.isEqual(tempBufferedImageArray, totalImages):
                if self.isImageFillIn:
                    self.fudgeItJButton.setEnabled(True)
            self.updateImage(tempBufferedImageArray)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateImage", e)
    

    def updateImageWithFudgedImages(self) -> None:
        try:
            bufferedImageArray: list[BufferedImage] = self.getImageProcessorInput().getBufferedImageArray()
            tempBufferedImageArray: list[BufferedImage] = [None] * (len(bufferedImageArray))
            for index in range(0, len(bufferedImageArray)):
                indexedImageIcon: ImageIconUnique = self.imageJList.getModel().getElementAt(index)
                bufferedImage: BufferedImage = ImageUtil.getInstance().createBufferedImage(bufferedImageArray[indexedImageIcon.getId()], self.imageUnifierProperties.getImageUnifierCell().getWidth(), self.imageUnifierProperties.getImageUnifierCell().getHeight(), False)
                tempBufferedImageArray[index] = bufferedImage
            totalImages: int = self.imageUnifierProperties.getRows() * self.imageUnifierProperties.getColumns()
            averageRatio: float = self.imagesRatioUtil.getAverage(tempBufferedImageArray, totalImages)
            fudgedBufferedImageArray: list[BufferedImage] = self.imagesRatioUtil.fudge(tempBufferedImageArray, totalImages, averageRatio)
            self.updateImage(fudgedBufferedImageArray)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateImageWithFudgedImages", e)
    

    # Java overloaded method: Python keeps the last definition
    def updateImage(self, tempBufferedImageArray: list[BufferedImage]) -> None:
        from org.allbinary.image.gui.ImageIcon import ImageIcon
        from org.allbinary.image.gui.JLabel import JLabel
        self.result = ImageUnifierUtil.getInstance().getImage(tempBufferedImageArray, self.imageUnifierProperties)
        image: Icon = ImageIcon(self.result)
        label: JLabel = JLabel(image)
        self.jScrollPane2.getViewport().add(label)
        self.updateUI()
    

    def updateOnPropertiesChange(self) -> None:
        if self.rowsJTextField.getText().length() > 0 and self.columnsJTextField.getText().length() > 0 and self.cellWidthJTextField.getText().length() > 0 and self.cellHeightJTextField.getText().length() > 0:
            self.imageUnifierProperties = ImageUnifierProperties()
            self.imageUnifierProperties.setRows(int(self.rowsJTextField.getText()))
            self.imageUnifierProperties.setColumns(int(self.columnsJTextField.getText()))
            imageUnifierCell: ImageUnifierCell = ImageUnifierCell(int(self.cellWidthJTextField.getText()), int(self.cellHeightJTextField.getText()))
            self.imageUnifierProperties.setImageUnifierCell(imageUnifierCell)
            cellRatio: float = (float(imageUnifierCell.getWidth()) / imageUnifierCell.getHeight())
            cellRatioString: str = str(float(cellRatio))
            if len(cellRatioString) > 4:
                cellRatioString = cellRatioString[0:4]
            self.cellRatioJTextField.setText(cellRatioString)
            self.updateImage()
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.JScrollPane import JScrollPane
        from org.allbinary.image.gui.JList import JList
        from org.allbinary.image.gui.JScrollPane import JScrollPane
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.Dimension import Dimension
        from org.allbinary.image.gui.Dimension import Dimension
        from org.allbinary.image.gui.Dimension import Dimension
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.PropertyChangeListener import PropertyChangeListener
        from org.allbinary.image.gui.KeyAdapter import KeyAdapter
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        self.jScrollPane1 = JScrollPane()
        self.imageJList = JList()
        self.jScrollPane2 = JScrollPane()
        self.jPanel1 = JPanel()
        self.jButton1 = JButton()
        self.upJButton = JButton()
        self.downJButton = JButton()
        self.fudgeItJButton = JButton()
        self.jLabel2 = JLabel()
        self.columnsJTextField = JTextField()
        self.jLabel1 = JLabel()
        self.rowsJTextField = JTextField()
        self.jLabel3 = JLabel()
        self.cellWidthJTextField = JTextField()
        self.jLabel4 = JLabel()
        self.cellHeightJTextField = JTextField()
        self.jLabel5 = JLabel()
        self.cellRatioJTextField = JTextField()
        self.jLabel6 = JLabel()
        self.avgRatioJTextField = JTextField()
        self.jButton2 = JButton()
        self.jButtonOrder = JButton()
        self.setMinimumSize(Dimension(500, 375))
        self.setPreferredSize(Dimension(0, 0))
        self.imageJList.setMinimumSize(Dimension(50, 0))
        self.jScrollPane1.setViewportView(self.imageJList)
        self.jButton1.setText("Save")
        self.jButton1.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jButton1ActionPerformed(evt)
))
        self.upJButton.setText("Up")
        self.upJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.upJButtonActionPerformed(evt)
))
        self.downJButton.setText("Down")
        self.downJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.downJButtonActionPerformed(evt)
))
        self.fudgeItJButton.setText("Fudge It!")
        self.fudgeItJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.fudgeItJButtonActionPerformed(evt)
))
        self.jLabel2.setText("Columns:")
        self.columnsJTextField.setText(commonPhoneStrings.TWO)
        self.columnsJTextField.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.columnsJTextFieldActionPerformed(evt)
))
        self.columnsJTextField.addPropertyChangeListener((PropertyChangeListener()  # Java anonymous class body:
#             
# 
#             def propertyChange(self, evt: PropertyChangeEvent) -> None:
#                 self.columnsJTextFieldPropertyChange(evt)
))
        self.columnsJTextField.addKeyListener((KeyAdapter()  # Java anonymous class body:
#             
# 
#             def keyPressed(self, evt: KeyEvent) -> None:
#                 self.columnsJTextFieldKeyPressed(evt)
#             
# 
#             def keyTyped(self, evt: KeyEvent) -> None:
#                 self.columnsJTextFieldKeyTyped(evt)
))
        self.jLabel1.setText("Rows:")
        self.rowsJTextField.setText(commonPhoneStrings.TWO)
        self.rowsJTextField.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.rowsJTextFieldActionPerformed(evt)
))
        self.jLabel3.setText("Cell Width:")
        self.cellWidthJTextField.setText("200")
        self.cellWidthJTextField.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.cellWidthJTextFieldActionPerformed(evt)
))
        self.jLabel4.setText("Cell Height:")
        self.cellHeightJTextField.setText("150")
        self.cellHeightJTextField.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.cellHeightJTextFieldActionPerformed(evt)
))
        self.jLabel5.setText("Cell Ratio:")
        self.cellRatioJTextField.setEditable(False)
        self.jLabel6.setText("Avg Image Ratio:")
        self.avgRatioJTextField.setEditable(False)
        self.jButton2.setText(self.commonStrings.UPDATE)
        self.jButton2.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jButton2ActionPerformed(evt)
))
        self.jButtonOrder.setText("Order")
        self.jButtonOrder.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.jButtonOrderActionPerformed(evt)
))
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup().addContainerGap().addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addComponent(self.jButton1, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.upJButton, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 10, Short.MAX_VALUE).addComponent(self.downJButton, javax.swing.GroupLayout.PREFERRED_SIZE, 70, javax.swing.GroupLayout.PREFERRED_SIZE)).addComponent(self.fudgeItJButton, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addGroup(javax.swing.GroupLayout.Alignment.LEADING, jPanel1Layout.createSequentialGroup().addComponent(self.jLabel3).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 99, javax.swing.GroupLayout.PREFERRED_SIZE)).addGroup(javax.swing.GroupLayout.Alignment.LEADING, jPanel1Layout.createSequentialGroup().addComponent(self.jLabel4).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 96, javax.swing.GroupLayout.PREFERRED_SIZE)).addComponent(self.avgRatioJTextField, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.jLabel6, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.cellRatioJTextField, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.jLabel5, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.cellHeightJTextField, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.cellWidthJTextField, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.jButton2, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addGroup(javax.swing.GroupLayout.Alignment.LEADING, jPanel1Layout.createSequentialGroup().addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jLabel2).addComponent(self.jLabel1)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.rowsJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 103, Short.MAX_VALUE).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.columnsJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 102, Short.MAX_VALUE).addGap(1, 1, 1)))).addComponent(self.jButtonOrder, javax.swing.GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE)).addContainerGap()))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addContainerGap().addComponent(self.jButton1).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.upJButton).addComponent(self.downJButton)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jButtonOrder).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.fudgeItJButton).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel2).addComponent(self.columnsJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.rowsJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel3).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.cellWidthJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel4).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.cellHeightJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jButton2).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel5).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.cellRatioJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addGap(7, 7, 7).addComponent(self.jLabel6).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.avgRatioJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addGap(66, 66, 66)))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 84, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jScrollPane2, javax.swing.GroupLayout.DEFAULT_SIZE, 527, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addComponent(self.jPanel1, javax.swing.GroupLayout.Alignment.LEADING, 0, 445, Short.MAX_VALUE).addComponent(self.jScrollPane2, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 445, Short.MAX_VALUE).addComponent(self.jScrollPane1, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 445, Short.MAX_VALUE)).addContainerGap()))
    

    def jButton2ActionPerformed(self, evt: ActionEvent) -> None:
        self.updateOnPropertiesChange()
    

    def columnsJTextFieldKeyPressed(self, evt: KeyEvent) -> None:
        pass
    

    def columnsJTextFieldKeyTyped(self, evt: KeyEvent) -> None:
        pass
    

    def columnsJTextFieldPropertyChange(self, evt: PropertyChangeEvent) -> None:
        pass
    

    def fudgeItJButtonActionPerformed(self, evt: ActionEvent) -> None:
        self.updateImageWithFudgedImages()
    

    def cellHeightJTextFieldActionPerformed(self, evt: ActionEvent) -> None:
        self.updateOnPropertiesChange()
    

    def cellWidthJTextFieldActionPerformed(self, evt: ActionEvent) -> None:
        self.updateOnPropertiesChange()
    

    def columnsJTextFieldActionPerformed(self, evt: ActionEvent) -> None:
        self.updateOnPropertiesChange()
    

    def rowsJTextFieldActionPerformed(self, evt: ActionEvent) -> None:
        self.updateOnPropertiesChange()
    

    def jButton1ActionPerformed(self, evt: ActionEvent) -> None:
        try:
            fileArray: list[File] = self.imageProcessorInput.getFiles()
            file: File = fileArray[0]
            filePath: str = file.getAbsolutePath()
            extensionIndex: int = filePath.find(self.imageStrings.PNG_EXTENSION)
            filePath = str(StringMaker().append(filePath[0:extensionIndex]).append(CommonSeps.getInstance().UNDERSCORE).appendint(int(self.imageUnifierProperties.getColumns())).append("_By_").appendint(int(self.imageUnifierProperties.getRows())).append("_Unified").append(self.imageStrings.PNG_EXTENSION))
            self.logUtil.putF("New File Path: " + filePath, self, StringUtil.getInstance().EMPTY_STRING)
            outputFile: File = File(filePath)
            ImagePersistanceUtil.getInstance().saveWithBatik(FileWrapperUtil.wrapFile(outputFile), self.result)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "jButton1ActionPerformed", e)
    

    def downJButtonActionPerformed(self, evt: ActionEvent) -> None:
        index: int = self.imageJList.getSelectedIndex()
        defaultListModel: DefaultListModel = self.imageJList.getModel()
        if index >= 0 and index + 1 < defaultListModel.size():
            indexedImageIcon: ImageIconUnique = defaultListModel.remove(index)
            defaultListModel.insertElementAt(indexedImageIcon, index + 1)
            self.imageJList.setSelectedIndex(index + 1)
            self.updateImage()
    

    def upJButtonActionPerformed(self, evt: ActionEvent) -> None:
        index: int = self.imageJList.getSelectedIndex()
        if index > 0:
            defaultListModel: DefaultListModel = self.imageJList.getModel()
            indexedImageIcon: ImageIconUnique = defaultListModel.remove(index)
            defaultListModel.insertElementAt(indexedImageIcon, index - 1)
            self.imageJList.setSelectedIndex(index - 1)
            self.updateImage()
    

    def jButtonOrderActionPerformed(self, evt: ActionEvent) -> None:
        defaultListModel: DefaultListModel = self.imageJList.getModel()
        size: int = defaultListModel.size()
        last: int = size - 1
        for index in range(last, 0 - 1, -1):
            indexedImageIcon: ImageIconUnique = defaultListModel.remove(last)
            defaultListModel.insertElementAt(indexedImageIcon, last - index)
        if size > 0:
            self.imageJList.setSelectedIndex(0)
            self.updateImage()
    

    def getImageProcessorInput(self) -> ImageProcessorInput:
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        self.imageProcessorInput = imageProcessorInput
        self.init()
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.File import File
# from javax.swing import *
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
from org.allbinary.media.image.ImageStrings import ImageStrings
from org.allbinary.media.image.ImageUnifierCell import ImageUnifierCell
from org.allbinary.media.image.ImageUnifierProperties import ImageUnifierProperties
from org.allbinary.media.image.ImageUnifierUtil import ImageUnifierUtil
from org.allbinary.media.image.ImageUtil import ImageUtil
from org.allbinary.media.image.ImagesRatioUtil import ImagesRatioUtil
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


