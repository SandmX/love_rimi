from pathlib import Path

from . import LANG_F_DIR
from .crypto import check_sign


def where() -> Path:
    """
    返回包 this_un 语言文件根目录路径
    Returns:
        Path: 绝对路径
    """
    return LANG_F_DIR

def lang_list(checked=True) -> dict[str, bool]:
    """
    返回已有的语言包列表 名称和可用性

    Args:
        checked (bool, optional): 是否检查语言包可用性
    Returns:
        dict[str, bool]: 已有语言包列表
            For example:
                checked=True: {'de': True, 'fr': False}
                checked=False: {'de': False, 'fr': False}
    """
    __lang_list = {}
    for f in LANG_F_DIR.iterdir():
        if not f.is_file() or f.suffix != '.lang':
            continue
        if checked:
            __lang_list[f.stem] = check_sign(f)
        else:
            __lang_list[f.stem] = False

    return __lang_list
