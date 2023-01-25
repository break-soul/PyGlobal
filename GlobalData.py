# -*- coding: utf-8 -*-
# GlobalData.py

from logging import getLogger

from typing import Any

logger = getLogger("Global.GlobalData")


def init_global_dict() -> dict[str, Any]:
    global global_dict
    try:
        global_dict: dict[str, Any]
        if global_dict != None:
            logger.warning("Global dict has been initialized!")
        else:
            logger.info("Global dict will init...")
            raise Exception
    except:
        # init
        global_dict = dict()
        global_dict["var"] = dict()
        global_dict["lang"] = dict()
    finally:
        return global_dict


def get_global_dict() -> dict[str, Any]:
    global global_dict
    try:
        global_dict: dict[str, Any]
    except:
        logger.warning("Global dict has not been initialized!")
        init_global_dict()
    finally:
        return global_dict