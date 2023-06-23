import pandas as pd
from typing import Union, Optional
from pathlib import Path, PosixPath
import numpy as np
import re

def _is_null_cell(cell: str) -> bool:
    if cell is None:
        return True
    cell = str(cell)
    if len(cell) == 0:
        return True
    else:
        return False


def _is_int(cell:str)->bool:
    if _is_null_cell(cell):
        return False
    
    cell = str(cell)
    try:
        int(cell)
        return True
    except:
        return False


def _is_float(cell:str)->bool:
    if _is_null_cell(cell):
        return False
    
    cell = str(cell)
    try:
        float(cell)
        return True
    except:
        return False

def _judge_SDN(e:str) -> str:
    e = str(e)
    if len(e) != 1:
        raise ValueError('Invalid input')
    if _is_int(e):
        return "N"
    else:
        if e == ".":
            return "D"
        else:
            return "S"


def _make_dict(values: Union[list, tuple], keys: Union[list, tuple]=None) -> dict:

    if keys is None:
        keys = _make_tmp_rowname(len(values))
    
    if len(keys) != len(values):
        return None
    
    ret = {}
    for k, v in zip(keys, values):
        ret[k] = v.replace(k, '')
    
    return ret


def _make_tmp_rowname(n):
    return [f'c{i}' for i in range(n)]


def parse_single(filename: Union[str, PosixPath], delimiter: str="_", filenameformat:str=None) -> dict:
    """単一ファイルのパース

    Args:
        filename (Union[str, PosixPath]): [description]
        delimiter (str, optional): [description]. Defaults to "_".
        filenameformat (str, optional): [description]. Defaults to None.

    Returns:
        dict: [description]
    """
    filename = Path(filename)
    filename_stem = filename.stem
    ret = None
    if filenameformat is None:
        ret = _make_dict(filename_stem.split(delimiter))
    else:
        ret = _make_dict(filename_stem.split(delimiter), filenameformat.split(delimiter))

    if ret is None:
        return None

    ret['nelems'] = len(ret.values())
    ret['original'] = str(filename)
    return ret


def parse_multiple(files: Union[list, tuple, pd.core.series.Series], delimiter: str="_", filenameformat:str=None) -> pd.core.frame.DataFrame:
    """複数ファイルを受け取り，パースした結果をデータフレームで返す

    Args:
        files (Union[list, tuple, pd.core.series.Series]): 一連のファイル名
        delimiter (str, optional): デリミタ. Defaults to "_".
        filenameformat (str, optional): フォーマットが決まっている場合は入力する. Defaults to None.

    Returns:
        pd.core.frame.DataFrame: 結果のデータフレーム

    """
    df = pd.DataFrame()
    results = {}
    for i, f in enumerate(files):
        ret = parse_single(f, delimiter, filenameformat)
        if ret is not None:
            results[i] = ret
            # df = df.append(ret, ignore_index=True)
    return pd.DataFrame(results).T
