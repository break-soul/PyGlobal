# -*- coding: utf-8 -*-
# Src/Utils/Global/GlobalDo.py

from .GlobalData import get_global_dict


# region global var
def get_global_var(key: str, default: str | None = None) -> str:
    """
    获取全局变量

    Args:
        key (str): 变量名

    Returns:
        object: 变量值
    """
    return get_global_dict()["var"].get(key, default)


def set_global_var(key: str, value: object):
    """
    设置全局变量

    Args:
        key (str): 变量名
        value (object): 变量值
    """
    get_global_dict()["var"][key] = value


# endregion

# region lang
def init_lang_dict():
    """
    初始化语言字典
    """
    get_global_dict()["lang"] = dict()

def get_lang_dict() -> dict:
    """
    获取语言字典

    Returns:
        dict: 语言字典
    """
    if(get_global_dict()["lang"] == None):
        init_lang_dict()
    return get_global_dict()["lang"]

# endregion