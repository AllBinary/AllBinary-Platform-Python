# 
# To change this license header, choose License Headers in Project Properties. 
# To change this template file, choose Tools | Templates 
# and open the template in the editor.  
# Generated Code Do Not Modify
# package org.allbinary.input.motion.button

from __future__ import annotations



class TouchButtonResource:

    def _init_fields(self) -> None:
        if "RESOURCE" not in vars(self): self.RESOURCE: str = None
        if "HINT" not in vars(self): self.HINT: str = None
    

    def __init__(self, resource: str, hint: str) -> None:
        __class__._init_fields(self)
        self.RESOURCE = resource
        self.HINT = hint


