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

from org.allbinary.gui.dialog.FileJDialogListenerInterface import FileJDialogListenerInterface
from org.allbinary.image.gui.JFrame import JFrame


class ImageToolJFrame(JFrame, FileJDialogListenerInterface):
    imageProcessorInputCompositeInterface: ImageProcessorInputCompositeInterface = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.fileJDialog: FileJDialog = None
        self.imageProcessorInput: ImageProcessorInput = None
        self.analysisActionJDialog: JDialog = None
        self.analyzeJMenuItem: JMenuItem = None
        self.blueJLabel: JLabel = None
        self.colorRangeJLabel: JLabel = None
        self.createStripImageJMenuItem: JMenuItem = None
        self.fileJMenu: JMenu = None
        self.generateSpriteSplitterMenuItem: JMenuItem = None
        self.generateRotationMenuItem: JMenuItem = None
        self.generateMirrorSpriteMenuItem: JMenuItem = None
        self.generateRotationSpriteJMenuItem: JMenuItem = None
        self.greenJLabel: JLabel = None
        self.jPanel1: JPanel = None
        self.mainJMenuBar: JMenuBar = None
        self.maxBlueJTextField: JTextField = None
        self.maxGreenJTextField: JTextField = None
        self.maxJLabel: JLabel = None
        self.maxRedJTextField: JTextField = None
        self.minBlueJTextField: JTextField = None
        self.minGreenJTextField: JTextField = None
        self.minJLabel: JLabel = None
        self.minRedJTextField: JTextField = None
        self.mirrorJMenuItem: JMenuItem = None
        self.okJButton: JButton = None
        self.openImageJMenuItem: JMenuItem = None
        self.processingJMenu: JMenu = None
        self.redJLabel: JLabel = None
        self.scaleImagesJMenuItem: JMenuItem = None
        self.canvasImagesJMenuItem: JMenuItem = None
        self.createIconImagesJMenuItem: JMenuItem = None
        self.titleJLabel: JLabel = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        self.setSize(640, 480)
        self.getMaxRedJTextField().setText("255")
        self.getMaxGreenJTextField().setText("255")
        self.getMaxBlueJTextField().setText("255")
        self.getMinRedJTextField().setText(commonPhoneStrings.ZERO)
        self.getMinGreenJTextField().setText(commonPhoneStrings.ZERO)
        self.getMinBlueJTextField().setText(commonPhoneStrings.ZERO)
        self.fileJDialog = FileJDialog()
        self.fileJDialog.addFinishedListener(self)
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.JDialog import JDialog
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JButton import JButton
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JPanel import JPanel
        from org.allbinary.image.gui.JMenuBar import JMenuBar
        from org.allbinary.image.gui.JMenu import JMenu
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenu import JMenu
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.JMenuItem import JMenuItem
        from org.allbinary.image.gui.Dimension import Dimension
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        from org.allbinary.image.gui.GridLayout import GridLayout
        from org.allbinary.image.gui.GridLayout import GridLayout
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        from org.allbinary.image.gui.ActionListener import ActionListener
        self.analysisActionJDialog = JDialog()
        self.titleJLabel = JLabel()
        self.colorRangeJLabel = JLabel()
        self.redJLabel = JLabel()
        self.minJLabel = JLabel()
        self.maxJLabel = JLabel()
        self.greenJLabel = JLabel()
        self.blueJLabel = JLabel()
        self.minRedJTextField = JTextField()
        self.maxRedJTextField = JTextField()
        self.maxGreenJTextField = JTextField()
        self.minBlueJTextField = JTextField()
        self.maxBlueJTextField = JTextField()
        self.okJButton = JButton()
        self.minGreenJTextField = JTextField()
        self.jPanel1 = JPanel()
        self.mainJMenuBar = JMenuBar()
        self.fileJMenu = JMenu()
        self.openImageJMenuItem = JMenuItem()
        self.processingJMenu = JMenu()
        self.analyzeJMenuItem = JMenuItem()
        self.generateSpriteSplitterMenuItem = JMenuItem()
        self.generateRotationMenuItem = JMenuItem()
        self.generateMirrorSpriteMenuItem = JMenuItem()
        self.generateRotationSpriteJMenuItem = JMenuItem()
        self.createStripImageJMenuItem = JMenuItem()
        self.mirrorJMenuItem = JMenuItem()
        self.scaleImagesJMenuItem = JMenuItem()
        self.canvasImagesJMenuItem = JMenuItem()
        self.createIconImagesJMenuItem = JMenuItem()
        self.analysisActionJDialog.setMinimumSize(Dimension(350, 250))
        self.titleJLabel.setText("              Color At Action Options            ")
        self.colorRangeJLabel.setText("Color Range")
        self.redJLabel.setText("Red:")
        self.minJLabel.setText("Minimum")
        self.maxJLabel.setText("Maximum")
        self.greenJLabel.setText("Green:")
        self.blueJLabel.setText("Blue:")
        self.okJButton.setText("OK")
        self.okJButton.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.okJButtonActionPerformed(evt)
))
        analysisActionJDialogLayout: GroupLayout = GroupLayout(self.analysisActionJDialog.getContentPane())
        self.analysisActionJDialog.getContentPane().setLayout(analysisActionJDialogLayout)
        analysisActionJDialogLayout.setHorizontalGroup(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(analysisActionJDialogLayout.createSequentialGroup().addContainerGap().add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(analysisActionJDialogLayout.createSequentialGroup().add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(self.blueJLabel).add(self.greenJLabel).add(self.redJLabel).add(self.colorRangeJLabel)).add(29, 29, 29).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(org.jdesktop.layout.GroupLayout.TRAILING, self.minJLabel, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, 58, Short.MAX_VALUE).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.TRAILING, False).add(org.jdesktop.layout.GroupLayout.LEADING, self.minBlueJTextField).add(org.jdesktop.layout.GroupLayout.LEADING, self.minGreenJTextField).add(org.jdesktop.layout.GroupLayout.LEADING, self.minRedJTextField, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, 42, Short.MAX_VALUE).add(org.jdesktop.layout.GroupLayout.LEADING, self.okJButton))).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.TRAILING).add(org.jdesktop.layout.GroupLayout.LEADING, analysisActionJDialogLayout.createSequentialGroup().add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.TRAILING, False).add(org.jdesktop.layout.GroupLayout.LEADING, self.maxRedJTextField).add(org.jdesktop.layout.GroupLayout.LEADING, analysisActionJDialogLayout.createSequentialGroup().add(1, 1, 1).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(self.maxBlueJTextField).add(self.maxGreenJTextField, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, 43, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)))).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED, 17, Short.MAX_VALUE)).add(org.jdesktop.layout.GroupLayout.LEADING, self.maxJLabel, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, 61, Short.MAX_VALUE)).addContainerGap()).add(org.jdesktop.layout.GroupLayout.TRAILING, analysisActionJDialogLayout.createSequentialGroup().add(self.titleJLabel).add(25, 25, 25)))))
        analysisActionJDialogLayout.setVerticalGroup(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING).add(analysisActionJDialogLayout.createSequentialGroup().add(self.titleJLabel).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.BASELINE).add(self.minJLabel).add(self.colorRangeJLabel).add(self.maxJLabel)).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.TRAILING).add(self.redJLabel).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.BASELINE).add(self.minRedJTextField, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).add(self.maxRedJTextField, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE))).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.TRAILING).add(self.greenJLabel).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.BASELINE).add(self.minGreenJTextField, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).add(self.maxGreenJTextField, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE))).addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.TRAILING).add(self.blueJLabel).add(analysisActionJDialogLayout.createParallelGroup(org.jdesktop.layout.GroupLayout.BASELINE).add(self.minBlueJTextField, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE).add(self.maxBlueJTextField, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE))).add(16, 16, 16).add(self.okJButton).addContainerGap(org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        self.setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE)
        self.getContentPane().setLayout(GridLayout(1, 0))
        self.jPanel1.setLayout(GridLayout(1, 0))
        self.getContentPane().add(self.jPanel1)
        self.fileJMenu.setText("File")
        self.fileJMenu.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.fileJMenuActionPerformed(evt)
))
        self.openImageJMenuItem.setText("Open")
        self.openImageJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.openImageJMenuItemActionPerformed(evt)
))
        self.fileJMenu.add(self.openImageJMenuItem)
        self.mainJMenuBar.add(self.fileJMenu)
        self.processingJMenu.setText("Processing")
        self.processingJMenu.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.processingJMenuActionPerformed(evt)
))
        self.analyzeJMenuItem.setText("Image Analyze")
        self.analyzeJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.analyzeJMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.analyzeJMenuItem)
        self.generateMirrorSpriteMenuItem.setText("Mirror Sprite Generator")
        self.generateMirrorSpriteMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.generateMirrorSpriteMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.generateMirrorSpriteMenuItem)
        self.generateRotationSpriteJMenuItem.setText("Rotation Sprite Generator")
        self.generateRotationSpriteJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.generateRotationSpriteJMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.generateRotationSpriteJMenuItem)
        self.generateSpriteSplitterMenuItem.setText("Sprite Splitter Generator")
        self.generateSpriteSplitterMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.generateSpriteSplitterMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.generateSpriteSplitterMenuItem)
        self.generateRotationMenuItem.setText("Rotate Image Generator")
        self.generateRotationMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.generateRotationMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.generateRotationMenuItem)
        self.createStripImageJMenuItem.setText("Multi Image Unifier")
        self.createStripImageJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.createStripImageJMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.createStripImageJMenuItem)
        self.mirrorJMenuItem.setText("Mirror Image(s)")
        self.mirrorJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.mirrorJMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.mirrorJMenuItem)
        self.scaleImagesJMenuItem.setText("Scale Image(s)")
        self.scaleImagesJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.scaleImagesJMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.scaleImagesJMenuItem)
        self.canvasImagesJMenuItem.setText("Canvas Image(s)")
        self.canvasImagesJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.canvasImagesJMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.canvasImagesJMenuItem)
        self.createIconImagesJMenuItem.setText("Create Icon Image(s)")
        self.createIconImagesJMenuItem.addActionListener((ActionListener()  # Java anonymous class body:
#             
# 
#             def actionPerformed(self, evt: ActionEvent) -> None:
#                 self.createIconsJMenuItemActionPerformed(evt)
))
        self.processingJMenu.add(self.createIconImagesJMenuItem)
        self.mainJMenuBar.add(self.processingJMenu)
        self.setJMenuBar(self.mainJMenuBar)
        self.pack()
    

    def createStripImageJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.ImageUnifierJPanel import ImageUnifierJPanel
        try:
            imageUnifierJPanel: ImageUnifierJPanel = ImageUnifierJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(imageUnifierJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = imageUnifierJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "createStripImageJMenuItemActionPerformed", e)
    

    def okJButtonActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.ImageAnalysisResultsJPanel import ImageAnalysisResultsJPanel
        try:
            self.logUtil.putF("Starting", self, "okJButtonActionPerformed")
            imageAnalysisResultsArray: list[ImageAnalysisResults] = ImageAnalysis.getInstance().process(self.imageProcessorInput.getBufferedImageArray(), self.getColorRangeInterface())
            self.jPanel1.removeAll()
            self.jPanel1.add(ImageAnalysisResultsJPanel(imageAnalysisResultsArray))
            self.jPanel1.updateUI()
            self.analysisActionJDialog.setVisible(False)
            ImageToolJFrame.imageProcessorInputCompositeInterface = None
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "okJButtonActionPerformed", e)
    

    def processingJMenuActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def openImageJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.logUtil.putF("Starting", self, "openImageJMenuItemActionPerformed")
            self.fileJDialog.setVisible(True)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "openImageJMenuItemActionPerformed", e)
    

    def onFiles(self, files: list[File]) -> None:
        try:
            self.logUtil.putF("Reading " + str(len(files)) + " files.", self, "onFiles")
            Arrays.sort(files, (Comparator()  # Java anonymous class body:
#                 
# 
#                 def compare(self, file1: File, file2: File) -> int:
#                     fileNameIndexValue1: int = self.extractIndexNumberIfAnyFromFileName(file1.getName())
#                     fileNameIndexValue2: int = self.extractIndexNumberIfAnyFromFileName(file2.getName())
#                     return fileNameIndexValue1 - fileNameIndexValue2
#                 
# 
#                 def extractIndexNumberIfAnyFromFileName(self, name: str) -> int:
#                     i: int = 0
#                     try:
#                         start: int = name.rfind('_') + 1
#                         end: int = name.rfind('.')
#                         number: str = name[start:end]
#                         i = int(number)
#                     except Exception as e:
#                         i = 0
#                     return i
))
            bufferedImageArray: list[BufferedImage] = [None] * (len(files))
            for index in range(0, len(files)):
                bufferedImageArray[index] = ImageIO.read(files[index])
                if bufferedImageArray[index] is None:
                    raise Exception("Unable to read file: " + str(files[index].getPath()))
            self.imageProcessorInput = ImageProcessorInput(files, bufferedImageArray)
            self.fileJDialog.setVisible(False)
            if ImageToolJFrame.imageProcessorInputCompositeInterface is not None:
                ImageToolJFrame.imageProcessorInputCompositeInterface.setImageProcessorInput(self.imageProcessorInput)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onFiles", e)
    

    def fileJMenuActionPerformed(self, evt: ActionEvent) -> None:
        pass
    

    def analyzeJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        try:
            self.logUtil.putF("Starting", self, "analyzeJMenuItemActionPerformed")
            self.analysisActionJDialog.setVisible(True)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "analyzeJMenuItemActionPerformed", e)
    

    def generateRotationSpriteJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.RotationSpriteImageJPanel import RotationSpriteImageJPanel
        try:
            self.logUtil.putF("Starting", self, "generateRotationSpriteJMenuItemActionPerformed")
            spriteImageJPanel: RotationSpriteImageJPanel = RotationSpriteImageJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(spriteImageJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = spriteImageJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateRotationSpriteJMenuItemActionPerformed", e)
    

    def generateSpriteSplitterMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.SpriteSplitterImageJPanel import SpriteSplitterImageJPanel
        try:
            self.logUtil.putF("Starting", self, "generateRotationSpriteJMenuItemActionPerformed")
            imageJPanel: SpriteSplitterImageJPanel = SpriteSplitterImageJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(imageJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = imageJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateRotationMenuItemActionPerformed", e)
    

    def generateRotationMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.RotationImageJPanel import RotationImageJPanel
        try:
            self.logUtil.putF("Starting", self, "generateRotationSpriteJMenuItemActionPerformed")
            rotationImageJPanel: RotationImageJPanel = RotationImageJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(rotationImageJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = rotationImageJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateRotationMenuItemActionPerformed", e)
    

    def scaleImagesJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.ResizeImageJPanel import ResizeImageJPanel
        try:
            self.logUtil.putF(self.commonStrings.START, self, "scaleImagesJMenuItemActionPerformed")
            resizeImageJPanel: ResizeImageJPanel = ResizeImageJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(resizeImageJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = resizeImageJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "scaleImagesJMenuItemActionPerformed", e)
    

    def createIconsJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.CreateIconImagesJPanel import CreateIconImagesJPanel
        try:
            self.logUtil.putF(self.commonStrings.START, self, "createIconsJMenuItemActionPerformed")
            createIconImagesJPanel: CreateIconImagesJPanel = CreateIconImagesJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(createIconImagesJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = createIconImagesJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "scaleImagesJMenuItemActionPerformed", e)
    

    def canvasImagesJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.CanvasImageJPanel import CanvasImageJPanel
        try:
            self.logUtil.putF(self.commonStrings.START, self, "canvasImagesJMenuItemActionPerformed")
            resizeImageJPanel: CanvasImageJPanel = CanvasImageJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(resizeImageJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = resizeImageJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "scaleImagesJMenuItemActionPerformed", e)
    

    def generateMirrorSpriteMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.MirrorSpriteImageJPanel import MirrorSpriteImageJPanel
        try:
            self.logUtil.putF("Starting", self, "generateMirrorSpriteJMenuItemActionPerformed")
            spriteImageJPanel: MirrorSpriteImageJPanel = MirrorSpriteImageJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(spriteImageJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = spriteImageJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateMirrorSpriteJMenuItemActionPerformed", e)
    

    def mirrorJMenuItemActionPerformed(self, evt: ActionEvent) -> None:
        from org.allbinary.image.gui.MirrorImageJPanel import MirrorImageJPanel
        try:
            self.logUtil.putF("Starting", self, "generateMirrorJMenuItemActionPerformed")
            mirrorImageJPanel: MirrorImageJPanel = MirrorImageJPanel(self.imageProcessorInput)
            self.jPanel1.removeAll()
            self.jPanel1.add(mirrorImageJPanel)
            self.jPanel1.updateUI()
            ImageToolJFrame.imageProcessorInputCompositeInterface = mirrorImageJPanel
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateMirrorJMenuItemActionPerformed", e)
    

    def getColorRangeInterface(self) -> ColorRangeInterface:
        colorRangeInterface: ColorRangeInterface = ColorRange()
        colorRangeInterface.setMinRed(int(int(self.getMinRedJTextField().getText())))
        colorRangeInterface.setMaxRed(int(int(self.getMaxRedJTextField().getText())))
        colorRangeInterface.setMinGreen(int(int(self.getMinGreenJTextField().getText())))
        colorRangeInterface.setMaxGreen(int(int(self.getMaxGreenJTextField().getText())))
        colorRangeInterface.setMinBlue(int(int(self.getMinBlueJTextField().getText())))
        colorRangeInterface.setMaxBlue(int(int(self.getMaxBlueJTextField().getText())))
        return colorRangeInterface
    

    def getMaxBlueJTextField(self) -> JTextField:
        return self.maxBlueJTextField
    

    def setMaxBlueJTextField(self, maxBlueJTextField: JTextField) -> None:
        self.maxBlueJTextField = self.maxBlueJTextField
    

    def getMaxGreenJTextField(self) -> JTextField:
        return self.maxGreenJTextField
    

    def setMaxGreenJTextField(self, maxGreenJTextField: JTextField) -> None:
        self.maxGreenJTextField = self.maxGreenJTextField
    

    def getMaxRedJTextField(self) -> JTextField:
        return self.maxRedJTextField
    

    def setMaxRedJTextField(self, maxRedJTextField: JTextField) -> None:
        self.maxRedJTextField = self.maxRedJTextField
    

    def getMinBlueJTextField(self) -> JTextField:
        return self.minBlueJTextField
    

    def setMinBlueJTextField(self, minBlueJTextField: JTextField) -> None:
        self.minBlueJTextField = self.minBlueJTextField
    

    def getMinGreenJTextField(self) -> JTextField:
        return self.minGreenJTextField
    

    def setMinGreenJTextField(self, minGreenJTextField: JTextField) -> None:
        self.minGreenJTextField = self.minGreenJTextField
    

    def getMinRedJTextField(self) -> JTextField:
        return self.minRedJTextField
    

    def setMinRedJTextField(self, minRedJTextField: JTextField) -> None:
        self.minRedJTextField = self.minRedJTextField
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.File import File
# from java.util.Arrays import Arrays
# from java.util.Comparator import Comparator
# from javax.imageio.ImageIO import ImageIO
from org.allbinary.gui.dialog.FileJDialog import FileJDialog
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
from org.allbinary.media.image.analysis.ColorRange import ColorRange
from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
from org.allbinary.media.image.analysis.ImageAnalysis import ImageAnalysis
from org.allbinary.media.image.analysis.ImageAnalysisResults import ImageAnalysisResults
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonStrings import CommonStrings


