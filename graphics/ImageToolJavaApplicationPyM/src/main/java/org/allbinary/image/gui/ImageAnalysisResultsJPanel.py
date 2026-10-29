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

from org.allbinary.image.gui.JPanel import JPanel


class ImageAnalysisResultsJPanel(JPanel):

    def _init_fields(self) -> None:
        self.avgBlueJTextField: JTextField = None
        self.avgGreenJTextField: JTextField = None
        self.avgRedJTextField: JTextField = None
        self.jComboBox1: JComboBox = None
        self.jLabel1: JLabel = None
        self.jLabel10: JLabel = None
        self.jLabel11: JLabel = None
        self.jLabel12: JLabel = None
        self.jLabel13: JLabel = None
        self.jLabel2: JLabel = None
        self.jLabel3: JLabel = None
        self.jLabel4: JLabel = None
        self.jLabel5: JLabel = None
        self.jLabel6: JLabel = None
        self.jLabel7: JLabel = None
        self.jLabel8: JLabel = None
        self.jLabel9: JLabel = None
        self.matchingPixelsJTextField: JTextField = None
        self.maxBlueJTextField: JTextField = None
        self.maxGreenJTextField: JTextField = None
        self.maxRedJTextField: JTextField = None
        self.minBlueJTextField: JTextField = None
        self.minGreenJTextField: JTextField = None
        self.minRedJTextField: JTextField = None
        self.percentMatchingJTextField: JTextField = None
        self.totalPixelsJTextField: JTextField = None
    

    def __init__(self, imageAnalysisResultsArray: list[ImageAnalysisResults]) -> None:
        super().__init__()
        self._init_fields()
        self.initComponents()
        imageAnalysisResults: ImageAnalysisResults = imageAnalysisResultsArray[0]
        self.updateImageColorRangeResults(imageAnalysisResults)
    

    def initComponents(self) -> None:
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JComboBox import JComboBox
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JLabel import JLabel
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.JTextField import JTextField
        from org.allbinary.image.gui.DefaultComboBoxModel import DefaultComboBoxModel
        from org.allbinary.image.gui.GroupLayout import GroupLayout
        self.jLabel1 = JLabel()
        self.jLabel2 = JLabel()
        self.jLabel3 = JLabel()
        self.percentMatchingJTextField = JTextField()
        self.totalPixelsJTextField = JTextField()
        self.matchingPixelsJTextField = JTextField()
        self.jComboBox1 = JComboBox()
        self.jLabel4 = JLabel()
        self.jLabel5 = JLabel()
        self.jLabel6 = JLabel()
        self.jLabel7 = JLabel()
        self.avgRedJTextField = JTextField()
        self.avgGreenJTextField = JTextField()
        self.avgBlueJTextField = JTextField()
        self.minGreenJTextField = JTextField()
        self.jLabel8 = JLabel()
        self.jLabel9 = JLabel()
        self.jLabel10 = JLabel()
        self.minRedJTextField = JTextField()
        self.minBlueJTextField = JTextField()
        self.jLabel11 = JLabel()
        self.jLabel12 = JLabel()
        self.jLabel13 = JLabel()
        self.maxRedJTextField = JTextField()
        self.maxGreenJTextField = JTextField()
        self.maxBlueJTextField = JTextField()
        self.jLabel1.setText("Matching Pixels:")
        self.jLabel2.setText("Total Pixels:")
        self.jLabel3.setText("Percent Matching:")
        self.percentMatchingJTextField.setEditable(False)
        self.totalPixelsJTextField.setEditable(False)
        self.matchingPixelsJTextField.setEditable(False)
        self.jComboBox1.setModel(DefaultComboBoxModel([CommonPhoneStrings.getInstance().ONE]))
        self.jComboBox1.setEnabled(False)
        self.jLabel4.setText("Image:")
        self.jLabel5.setText("Average Red:")
        self.jLabel6.setText("Average Green:")
        self.jLabel7.setText("Average Blue:")
        self.avgRedJTextField.setEditable(False)
        self.avgGreenJTextField.setEditable(False)
        self.avgBlueJTextField.setEditable(False)
        self.minGreenJTextField.setEditable(False)
        self.jLabel8.setText("Min Red:")
        self.jLabel9.setText("Min Green:")
        self.jLabel10.setText("Min Blue:")
        self.minRedJTextField.setEditable(False)
        self.minBlueJTextField.setEditable(False)
        self.jLabel11.setText("Max Red:")
        self.jLabel12.setText("Max Green:")
        self.jLabel13.setText("Max Blue:")
        self.maxRedJTextField.setEditable(False)
        self.maxGreenJTextField.setEditable(False)
        self.maxBlueJTextField.setEditable(False)
        layout: GroupLayout = GroupLayout(self)
        self.setLayout(layout)
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addContainerGap().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jLabel3).addComponent(self.jLabel2).addComponent(self.jLabel1).addComponent(self.jLabel5).addComponent(self.jLabel6).addComponent(self.jLabel7).addComponent(self.jLabel4)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jComboBox1, javax.swing.GroupLayout.PREFERRED_SIZE, 81, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.avgBlueJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 81, Short.MAX_VALUE).addComponent(self.avgGreenJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 81, Short.MAX_VALUE).addComponent(self.avgRedJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 81, Short.MAX_VALUE).addComponent(self.totalPixelsJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 81, Short.MAX_VALUE).addComponent(self.percentMatchingJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 81, Short.MAX_VALUE).addComponent(self.matchingPixelsJTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 81, Short.MAX_VALUE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.jLabel12).addComponent(self.jLabel13).addComponent(self.jLabel8).addComponent(self.jLabel9).addComponent(self.jLabel10).addComponent(self.jLabel11)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(self.minRedJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 82, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.maxGreenJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 82, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.minGreenJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 82, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.minBlueJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 82, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.maxRedJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 82, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.maxBlueJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, 82, javax.swing.GroupLayout.PREFERRED_SIZE)).addContainerGap(18, Short.MAX_VALUE)))
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel4).addComponent(self.jComboBox1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel1).addComponent(self.matchingPixelsJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel8).addComponent(self.minRedJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel2).addComponent(self.totalPixelsJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel9).addComponent(self.minGreenJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel3).addComponent(self.percentMatchingJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel10).addComponent(self.minBlueJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel5).addComponent(self.avgRedJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel11).addComponent(self.maxRedJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel6).addComponent(self.avgGreenJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.maxGreenJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel12)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(self.jLabel7).addComponent(self.avgBlueJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE).addComponent(self.jLabel13).addComponent(self.maxBlueJTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))))
    

    def updateImageColorRangeResults(self, imageAnalysisResults: ImageAnalysisResults) -> None:
        imageColorRangeResults: ImageColorRangeResults = imageAnalysisResults.getImageColorRangeResults()
        self.matchingPixelsJTextField.setText(str(int(imageColorRangeResults.getMatchingPixelsChecked())))
        self.totalPixelsJTextField.setText(str(int(imageColorRangeResults.getTotalPixelsChecked())))
        self.percentMatchingJTextField.setText(str(float(imageColorRangeResults.getPercent())))
        imageColorResults: ImageColorResults = imageAnalysisResults.getImageColorResults()
        self.avgRedJTextField.setText(str(float(imageColorResults.getColorAverage().getAvgRed())))
        self.avgGreenJTextField.setText(str(float(imageColorResults.getColorAverage().getAvgGreen())))
        self.avgBlueJTextField.setText(str(float(imageColorResults.getColorAverage().getAvgBlue())))
        self.minRedJTextField.setText(str(int(imageColorResults.getColorRange().getMinRed())))
        self.minGreenJTextField.setText(str(int(imageColorResults.getColorRange().getMinGreen())))
        self.minBlueJTextField.setText(str(int(imageColorResults.getColorRange().getMinBlue())))
        self.maxRedJTextField.setText(str(int(imageColorResults.getColorRange().getMaxRed())))
        self.maxGreenJTextField.setText(str(int(imageColorResults.getColorRange().getMaxGreen())))
        self.maxBlueJTextField.setText(str(int(imageColorResults.getColorRange().getMaxBlue())))
from org.allbinary.media.image.analysis.ImageAnalysisResults import ImageAnalysisResults
from org.allbinary.media.image.analysis.ImageColorRangeResults import ImageColorRangeResults
from org.allbinary.media.image.analysis.ImageColorResults import ImageColorResults
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings


