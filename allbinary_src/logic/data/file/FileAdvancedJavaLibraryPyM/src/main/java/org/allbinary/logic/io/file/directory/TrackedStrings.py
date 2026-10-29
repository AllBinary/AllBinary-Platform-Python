# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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
# package org.allbinary.logic.io.file.directory

from __future__ import annotations



class TrackedStrings:
    instance: TrackedStrings = None

    def _init_fields(self) -> None:
        self.TARGET_PATH_WINDOWS: str = "\\target\\"
        self.TARGET_PATH_UNIX: str = "/target/"
        self.HTML_TEMP: str = "HTMLTemp"
        self.APPLICATION: str = "Application"
        self.APP: str = "\\app"
        self.GIT_COMMAND: str = "git"
        self.CHANGE_DIRECTORY_OPTION: str = "-C"
        self.LIST_FILES_COMMAND: str = "ls-files"
        self.ERROR_UNMATCH_OPTION: str = "--error-unmatch"
        self.PATHSPEC_SEPARATOR: str = "--"
        self.SEP_BY_NULL_CHAR_INSTEAD_OF_NEW_LINE: str = "-z"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TrackedStrings:
        return TrackedStrings.instance


TrackedStrings.instance = TrackedStrings()

