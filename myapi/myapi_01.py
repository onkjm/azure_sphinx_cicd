from typing import Union
import pandas as pd
from .utils import myapi_02


class PrintHello:
    """Helloを表示するクラス

    Args:
        data: Optional, 時系列のデータ（使わない）
        index: Optional, 時系列のIndex(使わない)

    標準的な使い方

    Example:
        >>> import myapi
        >>> ph = myapi.PrintHello()
        >>> ret = ph.execute()
        Hello, world.

    引数を与える使い方

    Example:
        >>> ret = ph.execute(input_str='Hi!')
        Hi!

    """

    def __init__(
        self, data: pd.DataFrame = None, index: Union[pd.Index, pd.DatetimeIndex] = None
    ):
        """コンストラクタ

        Args:
            data (pd.DataFrame, optional): データ. Defaults to None.
            index (Union[pd.Index, pd.DatetimeIndex], optional): 時系列のindex. Defaults to None.
        """
        self.data = data
        self.index = index

    def _dammy(self):
        """この関数は隠しなので、APIドキュメントには表示されない"""
        pass

    def execute(self, input_str: str = None) -> str:
        """Hello, world.を表示する。

        Args:
            input_str: Optional, 表示する文字列をinput_strで入力した値に変更

        Return:
            表示した文字列

        """
        if input_str is None:
            print_str = "Hello, world."
        else:
            print_str = input_str
        print(print_str)

        return print_str

    def get_sum(self, list_int: list[int]) -> int:
        """長さ2のintの要素の和を返す

        Args:
            list_int: 長さ2のintのlist

        Return:
            長さ2のintの要素の和、長さが2以外のときは0

        """

        ret = 0
        if len(list_int) == 2:
            ret = myapi_02.utils01(list_int[0], list_int[1])

        return ret
