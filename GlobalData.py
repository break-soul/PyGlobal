# -*- coding: utf-8 -*-
# GlobalData.py

from logging import getLogger

logger = getLogger("Global.GlobalData")

def init_global_dict() -> dict:
    global global_dict
    try:
        if global_dict != None:
            logger.warning("Global dict has been initialized!")
            return global_dict
    except:
        ...
    # init 
    global_dict = dict()
    global_dict["var"] = dict()
    global_dict["lang"] = dict()

    return global_dict

def get_global_dict() -> dict:
    global global_dict
    try:
        global_dict
    except:
        logger.warning("Global dict has not been initialized!")
        init_global_dict()
    return global_dict