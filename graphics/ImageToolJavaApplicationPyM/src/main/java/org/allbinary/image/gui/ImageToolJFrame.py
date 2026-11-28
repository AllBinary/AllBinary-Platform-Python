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
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.gui.dialog.FileJDialogListenerInterface import FileJDialogListenerInterface
# from javax.swing.JFrame import JFrame


@java_inherited_overloads
class ImageToolJFrame(*java_bases(JFrame, FileJDialogListenerInterface)):
    imageProcessorInputCompositeInterface: ImageProcessorInputCompositeInterface = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("fileJDialog", None)
        vars(self).setdefault("imageProcessorInput", None)
        vars(self).setdefault("analysisActionJDialog", None)
        vars(self).setdefault("analyzeJMenuItem", None)
        vars(self).setdefault("blueJLabel", None)
        vars(self).setdefault("colorRangeJLabel", None)
        vars(self).setdefault("createStripImageJMenuItem", None)
        vars(self).setdefault("fileJMenu", None)
        vars(self).setdefault("generateSpriteSplitterMenuItem", None)
        vars(self).setdefault("generateRotationMenuItem", None)
        vars(self).setdefault("generateMirrorSpriteMenuItem", None)
        vars(self).setdefault("generateRotationSpriteJMenuItem", None)
        vars(self).setdefault("greenJLabel", None)
        vars(self).setdefault("jPanel1", None)
        vars(self).setdefault("mainJMenuBar", None)
        vars(self).setdefault("maxBlueJTextField", None)
        vars(self).setdefault("maxGreenJTextField", None)
        vars(self).setdefault("maxJLabel", None)
        vars(self).setdefault("maxRedJTextField", None)
        vars(self).setdefault("minBlueJTextField", None)
        vars(self).setdefault("minGreenJTextField", None)
        vars(self).setdefault("minJLabel", None)
        vars(self).setdefault("minRedJTextField", None)
        vars(self).setdefault("mirrorJMenuItem", None)
        vars(self).setdefault("okJButton", None)
        vars(self).setdefault("openImageJMenuItem", None)
        vars(self).setdefault("processingJMenu", None)
        vars(self).setdefault("redJLabel", None)
        vars(self).setdefault("scaleImagesJMenuItem", None)
        vars(self).setdefault("canvasImagesJMenuItem", None)
        vars(self).setdefault("createIconImagesJMenuItem", None)
        vars(self).setdefault("titleJLabel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "fileJDialog" not in vars(self): self.fileJDialog: FileJDialog = None
        if "imageProcessorInput" not in vars(self): self.imageProcessorInput: ImageProcessorInput = None
        if "analysisActionJDialog" not in vars(self): self.analysisActionJDialog: JDialog = None
        if "analyzeJMenuItem" not in vars(self): self.analyzeJMenuItem: JMenuItem = None
        if "blueJLabel" not in vars(self): self.blueJLabel: JLabel = None
        if "colorRangeJLabel" not in vars(self): self.colorRangeJLabel: JLabel = None
        if "createStripImageJMenuItem" not in vars(self): self.createStripImageJMenuItem: JMenuItem = None
        if "fileJMenu" not in vars(self): self.fileJMenu: JMenu = None
        if "generateSpriteSplitterMenuItem" not in vars(self): self.generateSpriteSplitterMenuItem: JMenuItem = None
        if "generateRotationMenuItem" not in vars(self): self.generateRotationMenuItem: JMenuItem = None
        if "generateMirrorSpriteMenuItem" not in vars(self): self.generateMirrorSpriteMenuItem: JMenuItem = None
        if "generateRotationSpriteJMenuItem" not in vars(self): self.generateRotationSpriteJMenuItem: JMenuItem = None
        if "greenJLabel" not in vars(self): self.greenJLabel: JLabel = None
        if "jPanel1" not in vars(self): self.jPanel1: JPanel = None
        if "mainJMenuBar" not in vars(self): self.mainJMenuBar: JMenuBar = None
        if "maxBlueJTextField" not in vars(self): self.maxBlueJTextField: JTextField = None
        if "maxGreenJTextField" not in vars(self): self.maxGreenJTextField: JTextField = None
        if "maxJLabel" not in vars(self): self.maxJLabel: JLabel = None
        if "maxRedJTextField" not in vars(self): self.maxRedJTextField: JTextField = None
        if "minBlueJTextField" not in vars(self): self.minBlueJTextField: JTextField = None
        if "minGreenJTextField" not in vars(self): self.minGreenJTextField: JTextField = None
        if "minJLabel" not in vars(self): self.minJLabel: JLabel = None
        if "minRedJTextField" not in vars(self): self.minRedJTextField: JTextField = None
        if "mirrorJMenuItem" not in vars(self): self.mirrorJMenuItem: JMenuItem = None
        if "okJButton" not in vars(self): self.okJButton: JButton = None
        if "openImageJMenuItem" not in vars(self): self.openImageJMenuItem: JMenuItem = None
        if "processingJMenu" not in vars(self): self.processingJMenu: JMenu = None
        if "redJLabel" not in vars(self): self.redJLabel: JLabel = None
        if "scaleImagesJMenuItem" not in vars(self): self.scaleImagesJMenuItem: JMenuItem = None
        if "canvasImagesJMenuItem" not in vars(self): self.canvasImagesJMenuItem: JMenuItem = None
        if "createIconImagesJMenuItem" not in vars(self): self.createIconImagesJMenuItem: JMenuItem = None
        if "titleJLabel" not in vars(self): self.titleJLabel: JLabel = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.gui.dialog.FileJDialog import FileJDialog
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        super().__init__()
        __class__._init_fields(self)
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
        _java_listener_owner = self
        class _JavaListenerN68221(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "okJButtonActionPerformed") else _java_listener_owner).okJButtonActionPerformed(evt)
        self.okJButton.addActionListener(_JavaListenerN68221()
            )
        analysisActionJDialogLayout: GroupLayout = GroupLayout(self.analysisActionJDialog.getContentPane())
        self.analysisActionJDialog.getContentPane().setLayout(analysisActionJDialogLayout)
        analysisActionJDialogLayout.setHorizontalGroup(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(analysisActionJDialogLayout.createSequentialGroup().addContainerGap().add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(analysisActionJDialogLayout.createSequentialGroup().add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(self.blueJLabel).add(self.greenJLabel).add(self.redJLabel).add(self.colorRangeJLabel)).add(29, 29, 29).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING, self.minJLabel, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, 58, Short.MAX_VALUE).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING, False).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, self.minBlueJTextField).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, self.minGreenJTextField).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, self.minRedJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, 42, Short.MAX_VALUE).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, self.okJButton))).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, analysisActionJDialogLayout.createSequentialGroup().add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING, False).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, self.maxRedJTextField).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, analysisActionJDialogLayout.createSequentialGroup().add(1, 1, 1).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(self.maxBlueJTextField).add(self.maxGreenJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, 43, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE)))).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED, 17, Short.MAX_VALUE)).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING, self.maxJLabel, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, 61, Short.MAX_VALUE)).addContainerGap()).add(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING, analysisActionJDialogLayout.createSequentialGroup().add(self.titleJLabel).add(25, 25, 25)))))
        analysisActionJDialogLayout.setVerticalGroup(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.LEADING).add(analysisActionJDialogLayout.createSequentialGroup().add(self.titleJLabel).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.BASELINE).add(self.minJLabel).add(self.colorRangeJLabel).add(self.maxJLabel)).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING).add(self.redJLabel).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.BASELINE).add(self.minRedJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).add(self.maxRedJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE))).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING).add(self.greenJLabel).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.BASELINE).add(self.minGreenJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).add(self.maxGreenJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE))).addPreferredGap(__import__("org.jdesktop.layout.LayoutStyle", fromlist=["LayoutStyle"]).LayoutStyle.RELATED).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.TRAILING).add(self.blueJLabel).add(analysisActionJDialogLayout.createParallelGroup(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.BASELINE).add(self.minBlueJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE).add(self.maxBlueJTextField, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, __import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.PREFERRED_SIZE))).add(16, 16, 16).add(self.okJButton).addContainerGap(__import__("org.jdesktop.layout.GroupLayout", fromlist=["GroupLayout"]).GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        self.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        self.getContentPane().setLayout(GridLayout(1, 0))
        self.jPanel1.setLayout(GridLayout(1, 0))
        self.getContentPane().add(self.jPanel1)
        self.fileJMenu.setText("File")
        _java_listener_owner = self
        class _JavaListenerN72402(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "fileJMenuActionPerformed") else _java_listener_owner).fileJMenuActionPerformed(evt)
        self.fileJMenu.addActionListener(_JavaListenerN72402()
            )
        self.openImageJMenuItem.setText("Open")
        _java_listener_owner = self
        class _JavaListenerN72541(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "openImageJMenuItemActionPerformed") else _java_listener_owner).openImageJMenuItemActionPerformed(evt)
        self.openImageJMenuItem.addActionListener(_JavaListenerN72541()
            )
        self.fileJMenu.add(self.openImageJMenuItem)
        self.mainJMenuBar.add(self.fileJMenu)
        self.processingJMenu.setText("Processing")
        _java_listener_owner = self
        class _JavaListenerN72754(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "processingJMenuActionPerformed") else _java_listener_owner).processingJMenuActionPerformed(evt)
        self.processingJMenu.addActionListener(_JavaListenerN72754()
            )
        self.analyzeJMenuItem.setText("Image Analyze")
        _java_listener_owner = self
        class _JavaListenerN72893(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "analyzeJMenuItemActionPerformed") else _java_listener_owner).analyzeJMenuItemActionPerformed(evt)
        self.analyzeJMenuItem.addActionListener(_JavaListenerN72893()
            )
        self.processingJMenu.add(self.analyzeJMenuItem)
        self.generateMirrorSpriteMenuItem.setText("Mirror Sprite Generator")
        _java_listener_owner = self
        class _JavaListenerN73069(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateMirrorSpriteMenuItemActionPerformed") else _java_listener_owner).generateMirrorSpriteMenuItemActionPerformed(evt)
        self.generateMirrorSpriteMenuItem.addActionListener(_JavaListenerN73069()
            )
        self.processingJMenu.add(self.generateMirrorSpriteMenuItem)
        self.generateRotationSpriteJMenuItem.setText("Rotation Sprite Generator")
        _java_listener_owner = self
        class _JavaListenerN73245(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateRotationSpriteJMenuItemActionPerformed") else _java_listener_owner).generateRotationSpriteJMenuItemActionPerformed(evt)
        self.generateRotationSpriteJMenuItem.addActionListener(_JavaListenerN73245()
            )
        self.processingJMenu.add(self.generateRotationSpriteJMenuItem)
        self.generateSpriteSplitterMenuItem.setText("Sprite Splitter Generator")
        _java_listener_owner = self
        class _JavaListenerN73421(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateSpriteSplitterMenuItemActionPerformed") else _java_listener_owner).generateSpriteSplitterMenuItemActionPerformed(evt)
        self.generateSpriteSplitterMenuItem.addActionListener(_JavaListenerN73421()
            )
        self.processingJMenu.add(self.generateSpriteSplitterMenuItem)
        self.generateRotationMenuItem.setText("Rotate Image Generator")
        _java_listener_owner = self
        class _JavaListenerN73597(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "generateRotationMenuItemActionPerformed") else _java_listener_owner).generateRotationMenuItemActionPerformed(evt)
        self.generateRotationMenuItem.addActionListener(_JavaListenerN73597()
            )
        self.processingJMenu.add(self.generateRotationMenuItem)
        self.createStripImageJMenuItem.setText("Multi Image Unifier")
        _java_listener_owner = self
        class _JavaListenerN73773(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "createStripImageJMenuItemActionPerformed") else _java_listener_owner).createStripImageJMenuItemActionPerformed(evt)
        self.createStripImageJMenuItem.addActionListener(_JavaListenerN73773()
            )
        self.processingJMenu.add(self.createStripImageJMenuItem)
        self.mirrorJMenuItem.setText("Mirror Image(s)")
        _java_listener_owner = self
        class _JavaListenerN73949(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "mirrorJMenuItemActionPerformed") else _java_listener_owner).mirrorJMenuItemActionPerformed(evt)
        self.mirrorJMenuItem.addActionListener(_JavaListenerN73949()
            )
        self.processingJMenu.add(self.mirrorJMenuItem)
        self.scaleImagesJMenuItem.setText("Scale Image(s)")
        _java_listener_owner = self
        class _JavaListenerN74125(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "scaleImagesJMenuItemActionPerformed") else _java_listener_owner).scaleImagesJMenuItemActionPerformed(evt)
        self.scaleImagesJMenuItem.addActionListener(_JavaListenerN74125()
            )
        self.processingJMenu.add(self.scaleImagesJMenuItem)
        self.canvasImagesJMenuItem.setText("Canvas Image(s)")
        _java_listener_owner = self
        class _JavaListenerN74301(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "canvasImagesJMenuItemActionPerformed") else _java_listener_owner).canvasImagesJMenuItemActionPerformed(evt)
        self.canvasImagesJMenuItem.addActionListener(_JavaListenerN74301()
            )
        self.processingJMenu.add(self.canvasImagesJMenuItem)
        self.createIconImagesJMenuItem.setText("Create Icon Image(s)")
        _java_listener_owner = self
        class _JavaListenerN74477(ActionListener):
            
            

            def actionPerformed(self, evt: ActionEvent) -> None:
                (self if hasattr(self, "createIconsJMenuItemActionPerformed") else _java_listener_owner).createIconsJMenuItemActionPerformed(evt)
        self.createIconImagesJMenuItem.addActionListener(_JavaListenerN74477()
            )
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
        from org.allbinary.media.image.analysis.ImageAnalysis import ImageAnalysis
        from org.allbinary.media.image.analysis.ImageAnalysisResults import ImageAnalysisResults
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
        from java.io.File import File
        from java.util.Comparator import Comparator
        from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
        try:
            self.logUtil.putF("Reading " + str(len(files)) + " files.", self, "onFiles")
            _java_listener_owner = self
            class _JavaListenerN75892(Comparator):
            
                

                def compare(self, file1: File, file2: File) -> int:
                    from java.io.File import File
                    fileNameIndexValue1: int = (self if hasattr(self, "extractIndexNumberIfAnyFromFileName") else _java_listener_owner).extractIndexNumberIfAnyFromFileName(file1.getName())
                    fileNameIndexValue2: int = (self if hasattr(self, "extractIndexNumberIfAnyFromFileName") else _java_listener_owner).extractIndexNumberIfAnyFromFileName(file2.getName())
                    return fileNameIndexValue1 - fileNameIndexValue2
                

                def extractIndexNumberIfAnyFromFileName(self, name: str) -> int:
                    i: int = 0
                    try:
                        start: int = name.rfind('_') + 1
                        end: int = name.rfind('.')
                        number: str = name[start:end]
                        i = int(number)
                    except Exception as e:
                        i = 0
                    return i
            Arrays.sort(files, _JavaListenerN75892()
            )
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
        from org.allbinary.media.image.analysis.ColorRange import ColorRange
        from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
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
# from org.allbinary.gui.dialog.FileJDialog import FileJDialog
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.media.image.ImageProcessorInput import ImageProcessorInput
# from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface
# from org.allbinary.media.image.analysis.ColorRange import ColorRange
# from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
# from org.allbinary.media.image.analysis.ImageAnalysis import ImageAnalysis
# from org.allbinary.media.image.analysis.ImageAnalysisResults import ImageAnalysisResults
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonStrings import CommonStrings
# from java.awt.Dimension import Dimension
# from java.awt.GridLayout import GridLayout
# from java.awt.event.ActionEvent import ActionEvent
# from java.awt.event.ActionListener import ActionListener
# from javax.swing.JButton import JButton
# from javax.swing.JDialog import JDialog
# from javax.swing.JLabel import JLabel
# from javax.swing.JMenu import JMenu
# from javax.swing.JMenuBar import JMenuBar
# from javax.swing.JMenuItem import JMenuItem
# from javax.swing.JPanel import JPanel
# from javax.swing.JTextField import JTextField
# from javax.swing.WindowConstants import WindowConstants


