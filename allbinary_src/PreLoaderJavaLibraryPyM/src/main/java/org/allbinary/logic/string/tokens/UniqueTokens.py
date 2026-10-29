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
# package org.allbinary.logic.string.tokens

from __future__ import annotations



class UniqueTokens:

    def _init_fields(self) -> None:
        self.specialCharacters: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
        self.specialCharacters.add("!")
        self.specialCharacters.add("@")
        self.specialCharacters.add(CommonPhoneStrings.getInstance().POUND)
        self.specialCharacters.add("$")
        self.specialCharacters.add("%")
        self.specialCharacters.add("^")
        self.specialCharacters.add(CommonSeps.getInstance().AMPERSAND)
        self.specialCharacters.add(CommonPhoneStrings.getInstance().STAR)
        self.specialCharacters.add("(")
        self.specialCharacters.add(")")
        self.specialCharacters.add("-")
        self.specialCharacters.add("_")
        self.specialCharacters.add("+")
        self.specialCharacters.add("=")
        self.specialCharacters.add("\\")
        self.specialCharacters.add("|")
        self.specialCharacters.add(AbPathData.getInstance().EXTENSION_SEP)
        self.specialCharacters.add(",")
        self.specialCharacters.add("<")
        self.specialCharacters.add(">")
        self.specialCharacters.add("?")
        self.specialCharacters.add("/")
        self.specialCharacters.add("~")
        self.specialCharacters.add("`")
    

    # throws Exception
    def getWhithoutDashesAndSkipNumberOnlyTokens(self, stringVector: BasicArrayList) -> HashSet:
        from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
        from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
        try:
            hashSet: HashSet = HashSet()
            index: int = 0
            commonSeps: CommonSeps = CommonSeps.getInstance()
            while index < stringVector.size():
                keywords: str = stringVector.get(index)
                tokenizer: Tokenizer = Tokenizer(commonSeps.COMMA)
                keywordVector: BasicArrayList = tokenizer.getTokensFromString(keywords, BasicArrayListD())
                for forIndex in range(0, keywordVector.size()):
                    cleanString: str = keywordVector.get(forIndex)
                    cleanString = cleanString.strip()
                    if cleanString.find('-') != -1:
                        cleanString = Replace("-", commonSeps.SPACE).all(cleanString)
                    hashSet.add(cleanString)
                    if cleanString.find(' ') != -1:
                        spaceTokenizer: Tokenizer = Tokenizer(commonSeps.SPACE)
                        subKeywordVector: BasicArrayList = spaceTokenizer.getTokensFromString(cleanString, BasicArrayListD())
                        for spaceIndex in range(0, subKeywordVector.size()):
                            subCleanString: str = subKeywordVector.get(spaceIndex)
                            if not self.isSpecialCharacter(subCleanString) and not self.numberOnly(subCleanString):
                                hashSet.add(subCleanString)
                index += 1
            return hashSet
        except Exception as e:
            raise e
    

    def numberOnly(self, subCleaningString: str) -> bool:
        try:
            int(subCleaningString)
            return True
        except ValueError as e:
            return False
    

    def isSpecialCharacter(self, subCleaningString: str) -> bool:
        for index in range(0, self.specialCharacters.size()):
            if ((subCleaningString > self.specialCharacters.get(index)) - (subCleaningString < self.specialCharacters.get(index))) == 0:
                return True
        return False
# from java.util.HashSet import HashSet
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


