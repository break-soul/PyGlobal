# -*- coding: utf-8 -*-
# Language.py

from . import GlobalDo


def get_status() -> bool:
    """
    Get status

    Returns:
        bool: Status
    """
    return GlobalDo.get_global_var("LANG_STATUS", False)


def pre_translate(text: str) -> None:
    ...

def get_translate(text: str) -> str:
    """
    Get translate

    Args:
        text (str): Text

    Returns:
        str: Translated text
    """
    return text

def translate(text: str) -> str:
    """
    Translate text

    Args:
        text (str): Text

    Returns
        str: Translated text
    """
    if (get_status() == True):
        pre_translate(text)
        return text
    return get_translate(text)