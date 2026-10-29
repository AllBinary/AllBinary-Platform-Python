# 
# To change this license header, choose License Headers in Project Properties. 
# To change this template file, choose Tools | Templates 
# and open the template in the editor.  
# Generated Code Do Not Modify
# package org.allbinary.input.motion.button

from __future__ import annotations



class TouchButtonResource:

    def _init_fields(self) -> None:
        self.RESOURCE: str = None
        self.HINT: str = None
    

    def __init__(self, resource: str, hint: str) -> None:
        self._init_fields()
        self.RESOURCE = resource
        self.HINT = hint


