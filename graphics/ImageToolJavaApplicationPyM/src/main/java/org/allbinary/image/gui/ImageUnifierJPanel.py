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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
# from javax.swing.JPanel import JPanel


@java_inherited_overloads
class ImageUnifierJPanel(*java_bases(JPanel, ImageProcessorInputCompositeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("imageStrings", None)
        vars(self).setdefault("imagesRatioUtil", None)
        vars(self).setdefault("imageProcessorInput", None)
        vars(self).setdefault("icon", None)
        vars(self).setdefault("imageUnifierProperties", None)
        vars(self).setdefault("result", None)
        vars(self).setdefault("isImageFillIn", False)
        vars(self).setdefault("avgRatioJTextField", None)
        vars(self).setdefault("cellHeightJTextField", None)
        vars(self).setdefault("cellRatioJTextField", None)
        vars(self).setdefault("cellWidthJTextField", None)
        vars(self).setdefault("columnsJTextField", None)
        vars(self).setdefault("downJButton", None)
        vars(self).setdefault("fudgeItJButton", None)
        vars(self).setdefault("imageJList", None)
        vars(self).setdefault("jButton1", None)
        vars(self).setdefault("jButton2", None)
        vars(self).setdefault("jButtonOrder", None)
        vars(self).setdefault("jLabel1", None)
        vars(self).setdefault("jLabel2", None)
        vars(self).setdefault("jLabel3", None)
        vars(self).setdefault("jLabel4", None)
        vars(self).setdefault("jLabel5", None)
        vars(self).setdefault("jLabel6", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("jScrollPane1", None)
        vars(self).setdefault("jScrollPane2", None)
        vars(self).setdefault("rowsJTextField", None)
        vars(self).setdefault("upJButton", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.ImageStrings import ImageStrings
        from org.allbinary.media.image.ImagesRatioUtil import ImagesRatioUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageStrings: ImageStrings = ImageStrings.getInstance()
        self.imagesRatioUtil: ImagesRatioUtil = ImagesRatioUtil.getInstance()
        if "imageProcessorInput" not in vars(self): self.imageProcessorInput: ImageProcessorInput = None
        if "icon" not in vars(self): self.icon: list[ImageIconUnique] = None
        if "imageUnifierProperties" not in vars(self): self.imageUnifierProperties: ImageUnifierProperties = None
        if "result" not in vars(self): self.result: BufferedImage = None
        self.isImageFillIn: bool = True
        if "avgRatioJTextField" not in vars(self): self.avgRatioJTextField: JTextField = None
        if "cellHeightJTextField" not in vars(self): self.cellHeightJTextField: JTextField = None
        if "cellRatioJTextField" not in vars(self): self.cellRatioJTextField: JTextField = None
        if "cellWidthJTextField" not in vars(self): self.cellWidthJTextField: JTextField = None
        if "columnsJTextField" not in vars(self): self.columnsJTextField: JTextField = None
        if "downJButton" not in vars(self): self.downJButton: JButton = None
        if "fudgeItJButton" not in vars(self): self.fudgeItJButton: JButton = None
        if "imageJList" not in vars(self): self.imageJList: JList = None
        if "jButton1" not in vars(self): self.jButton1: JButton = None
        if "jButton2" not in vars(self): self.jButton2: JButton = None
        if "jButtonOrder" not in vars(self): self.jButtonOrder: JButton = None
        if "jLabel1" not in vars(self): self.jLabel1: JLabel = None
        if "jLabel2" not in vars(self): self.jLabel2: JLabel = None
        if "jLabel3" not in vars(self): self.jLabel3: JLabel = None
        if "jLabel4" not in vars(self): self.jLabel4: JLabel = None
        if "jLabel5" not in vars(self): self.jLabel5: JLabel = None
        if "jLabel6" not in vars(self): self.jLabel6: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "jScrollPane1" not in vars(self): self.jScrollPane1: JScrollPane = None
        if "jScrollPane2" not in vars(self): self.jScrollPane2: JScrollPane = None
        if "rowsJTextField" not in vars(self): self.rowsJTextField: JTextField = None
        if "upJButton" not in vars(self): self.upJButton: JButton = None
    

    def __init__(self, imageProcessorInput: ImageProcessorInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        super().__init__()
        __class__._init_fields(self)
        self.initComponents()
        self.setImageProcessorInput(imageProcessorInput)
    

    def init(self) -> None:
        from org.allbinary.image.gui.ImageIconUnique import ImageIconUnique
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        from org.allbinary.media.image.ImageUtil import ImageUtil
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
    

    def updateImage_j0(self) -> None:
        from org.allbinary.media.image.ImageUtil import ImageUtil
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
            if not (self.imagesRatioUtil.isEqual(tempBufferedImageArray, totalImages)):
                if self.isImageFillIn:
                    self.fudgeItJButton.setEnabled(True)
            self.updateImage(tempBufferedImageArray)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "updateImage", e)
    

    def updateImageWithFudgedImages(self) -> None:
        from org.allbinary.media.image.ImageUtil import ImageUtil
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
    

    def updateImage_j1(self, tempBufferedImageArray: list[BufferedImage]) -> None:
        from org.allbinary.media.image.ImageUnifierUtil import ImageUnifierUtil
        self.result = ImageUnifierUtil.getInstance().getImage(tempBufferedImageArray, self.imageUnifierProperties)
        image: Icon = ImageIcon(self.result)
        label: JLabel = JLabel(image)
        self.jScrollPane2.getViewport().add(label)
        self.updateUI()

    def updateImage(self, *args):
        implementation = __class__.__dict__.get("updateImage_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().updateImage(*args)
    

    def updateOnPropertiesChange(self) -> None:
        from org.allbinary.media.image.ImageUnifierCell import ImageUnifierCell
        from org.allbinary.media.image.ImageUnifierProperties import ImageUnifierProperties
        if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.rowsJTextField.getText()) > 0 and __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.columnsJTextField.getText()) > 0 and __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.cellWidthJTextField.getText()) > 0 and __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.cellHeightJTextField.getText()) > 0:
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
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
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
        _java_listener_owner = self
        class _JavaListenerN71869(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jButton1ActionPerformed") else _java_listener_owner).jButton1ActionPerformed(evt)
        self.jButton1.addActionListener(_JavaListenerN71869()
            )
        self.upJButton.setText("Up")
        _java_listener_owner = self
        class _JavaListenerN72008(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "upJButtonActionPerformed") else _java_listener_owner).upJButtonActionPerformed(evt)
        self.upJButton.addActionListener(_JavaListenerN72008()
            )
        self.downJButton.setText("Down")
        _java_listener_owner = self
        class _JavaListenerN72147(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "downJButtonActionPerformed") else _java_listener_owner).downJButtonActionPerformed(evt)
        self.downJButton.addActionListener(_JavaListenerN72147()
            )
        self.fudgeItJButton.setText("Fudge It!")
        _java_listener_owner = self
        class _JavaListenerN72286(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "fudgeItJButtonActionPerformed") else _java_listener_owner).fudgeItJButtonActionPerformed(evt)
        self.fudgeItJButton.addActionListener(_JavaListenerN72286()
            )
        self.jLabel2.setText("Columns:")
        self.columnsJTextField.setText(commonPhoneStrings.TWO)
        _java_listener_owner = self
        class _JavaListenerN72467(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "columnsJTextFieldActionPerformed") else _java_listener_owner).columnsJTextFieldActionPerformed(evt)
        self.columnsJTextField.addActionListener(_JavaListenerN72467()
            )
        _java_listener_owner = self
        class _JavaListenerN72576(PropertyChangeListener):
            
            

            def propertyChange(self, evt: PropertyChangeEvent) -> None:
                (self if hasattr(self, "columnsJTextFieldPropertyChange") else _java_listener_owner).columnsJTextFieldPropertyChange(evt)
        self.columnsJTextField.addPropertyChangeListener(_JavaListenerN72576()
            )
        _java_listener_owner = self
        class _JavaListenerN72685(KeyAdapter):
            
            

            def keyPressed(self, evt: KeyEvent) -> None:
                (self if hasattr(self, "columnsJTextFieldKeyPressed") else _java_listener_owner).columnsJTextFieldKeyPressed(evt)
            

            def keyTyped(self, evt: KeyEvent) -> None:
                (self if hasattr(self, "columnsJTextFieldKeyTyped") else _java_listener_owner).columnsJTextFieldKeyTyped(evt)
        self.columnsJTextField.addKeyListener(_JavaListenerN72685()
            )
        self.jLabel1.setText("Rows:")
        self.rowsJTextField.setText(commonPhoneStrings.TWO)
        _java_listener_owner = self
        class _JavaListenerN72934(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "rowsJTextFieldActionPerformed") else _java_listener_owner).rowsJTextFieldActionPerformed(evt)
        self.rowsJTextField.addActionListener(_JavaListenerN72934()
            )
        self.jLabel3.setText("Cell Width:")
        self.cellWidthJTextField.setText("200")
        _java_listener_owner = self
        class _JavaListenerN73103(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "cellWidthJTextFieldActionPerformed") else _java_listener_owner).cellWidthJTextFieldActionPerformed(evt)
        self.cellWidthJTextField.addActionListener(_JavaListenerN73103()
            )
        self.jLabel4.setText("Cell Height:")
        self.cellHeightJTextField.setText("150")
        _java_listener_owner = self
        class _JavaListenerN73272(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "cellHeightJTextFieldActionPerformed") else _java_listener_owner).cellHeightJTextFieldActionPerformed(evt)
        self.cellHeightJTextField.addActionListener(_JavaListenerN73272()
            )
        self.jLabel5.setText("Cell Ratio:")
        self.cellRatioJTextField.setEditable(False)
        self.jLabel6.setText("Avg Image Ratio:")
        self.avgRatioJTextField.setEditable(False)
        self.jButton2.setText(self.commonStrings.UPDATE)
        _java_listener_owner = self
        class _JavaListenerN73546(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jButton2ActionPerformed") else _java_listener_owner).jButton2ActionPerformed(evt)
        self.jButton2.addActionListener(_JavaListenerN73546()
            )
        self.jButtonOrder.setText("Order")
        _java_listener_owner = self
        class _JavaListenerN73685(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "jButtonOrderActionPerformed") else _java_listener_owner).jButtonOrderActionPerformed(evt)
        self.jButtonOrder.addActionListener(_JavaListenerN73685()
            )
        jPanel1Layout: GroupLayout = GroupLayout(self.jPanel1)
        self.jPanel1.setLayout(jPanel1Layout)
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup().addContainerGap().addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.TRAILING).addComponent(self.jButton1, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.upJButton, GroupLayout.PREFERRED_SIZE, 71, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 10, Short.MAX_VALUE).addComponent(self.downJButton, GroupLayout.PREFERRED_SIZE, 70, GroupLayout.PREFERRED_SIZE)).addComponent(self.fudgeItJButton, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addGroup(GroupLayout.Alignment.LEADING, jPanel1Layout.createSequentialGroup().addComponent(self.jLabel3).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 99, GroupLayout.PREFERRED_SIZE)).addGroup(GroupLayout.Alignment.LEADING, jPanel1Layout.createSequentialGroup().addComponent(self.jLabel4).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, 96, GroupLayout.PREFERRED_SIZE)).addComponent(self.avgRatioJTextField, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.jLabel6, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.cellRatioJTextField, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.jLabel5, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.cellHeightJTextField, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.cellWidthJTextField, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addComponent(self.jButton2, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE).addGroup(GroupLayout.Alignment.LEADING, jPanel1Layout.createSequentialGroup().addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.jLabel2).addComponent(self.jLabel1)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addComponent(self.rowsJTextField, GroupLayout.DEFAULT_SIZE, 103, Short.MAX_VALUE).addGroup(jPanel1Layout.createSequentialGroup().addComponent(self.columnsJTextField, GroupLayout.DEFAULT_SIZE, 102, Short.MAX_VALUE).addGap(1, 1, 1)))).addComponent(self.jButtonOrder, GroupLayout.DEFAULT_SIZE, 151, Short.MAX_VALUE)).addContainerGap()))
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(jPanel1Layout.createSequentialGroup().addContainerGap().addComponent(self.jButton1).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.upJButton).addComponent(self.downJButton)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jButtonOrder).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.fudgeItJButton).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel2).addComponent(self.columnsJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addGroup(jPanel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.rowsJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel3).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.cellWidthJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel4).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.cellHeightJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jButton2).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jLabel5).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE).addComponent(self.cellRatioJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addGap(7, 7, 7).addComponent(self.jLabel6).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.avgRatioJTextField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addGap(66, 66, 66)))
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addComponent(self.jScrollPane1, GroupLayout.PREFERRED_SIZE, 84, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jPanel1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE).addPreferredGap(LayoutStyle.ComponentPlacement.RELATED).addComponent(self.jScrollPane2, GroupLayout.DEFAULT_SIZE, 527, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING).addGroup(GroupLayout.Alignment.TRAILING, layout.createSequentialGroup().addGroup(layout.createParallelGroup(GroupLayout.Alignment.TRAILING).addComponent(self.jPanel1, GroupLayout.Alignment.LEADING, 0, 445, Short.MAX_VALUE).addComponent(self.jScrollPane2, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 445, Short.MAX_VALUE).addComponent(self.jScrollPane1, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 445, Short.MAX_VALUE)).addContainerGap()))
    

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
        from java.io.File import File
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
        from org.allbinary.string.CommonSeps import CommonSeps
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
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        return self.imageProcessorInput
    

    def setImageProcessorInput(self, imageProcessorInput: ImageProcessorInput) -> None:
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        self.imageProcessorInput = imageProcessorInput
        self.init()
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.File import File
# from javax.swing.DefaultListModel import DefaultListModel
# from javax.swing.ImageIcon import ImageIcon
# from javax.swing.Icon import Icon
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.media.image.ImagePersistanceUtil import ImagePersistanceUtil
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageStrings import ImageStrings
# from org.allbinary.media.image.ImageUnifierCell import ImageUnifierCell
# from org.allbinary.media.image.ImageUnifierProperties import ImageUnifierProperties
# from org.allbinary.media.image.ImageUnifierUtil import ImageUnifierUtil
# from org.allbinary.media.image.ImageUtil import ImageUtil
# from org.allbinary.media.image.ImagesRatioUtil import ImagesRatioUtil
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from java.awt.event.KeyAdapter import KeyAdapter
# from java.awt.event.KeyEvent import KeyEvent
# from java.beans.PropertyChangeEvent import PropertyChangeEvent
# from java.beans.PropertyChangeListener import PropertyChangeListener
# from javax.swing.GroupLayout import GroupLayout
# from javax.swing.JButton import JButton
# from javax.swing.JLabel import JLabel
# from javax.swing.JList import JList
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.JTextField import JTextField
# from javax.swing.LayoutStyle import LayoutStyle


