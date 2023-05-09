def utils01(i1:int, i2:int)->int:
    """引数の和を計算して返す
    
    Args:
        i1: 和を取る第一項目
        i2: 和を取る第二項目
        
    Return:
        i1とi2の和
        
    Example:
        >>> import utils01
        >>> i1 = 1
        >>> i2 = 2
        >>> utils01(i1, i2)
        3
    """
    ret = i1 + i2
    
    if ret == 8:
        raise InvalidListError('和が8にならないようにしてください')
    
    return i1 + i2

class InvalidListError(Exception):
    """与えられた引数の和が8の時に返すエラー

    """
    pass