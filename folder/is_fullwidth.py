import unicodedata
import re

# 判定関数


def is_fullwidth(char):
    # 基本の全角・半角判定（F、Wなら全角と判定）
    if unicodedata.east_asian_width(char) in ('F', 'W'):
        return True

    # 絵文字やその他のシンボル範囲も全角扱いとする場合
    symbol_pattern = re.compile("["
                                u"\U0001F300-\U0001F5FF"  # 絵文字、シンボルなど
                                u"\U0001F600-\U0001F64F"  # 顔の絵文字
                                u"\U0001F680-\U0001F6FF"  # 乗り物・地図
                                u"\U0001F900-\U0001F9FF"  # デコ顔文字
                                u"\U0001FA70-\U0001FAFF"  # アイテム類
                                u"\U0001F780-\U0001F7FF"  # 図形記号
                                "]+", flags=re.UNICODE)

    # シンボルパターンに一致すれば「全角」と同様に扱う
    return symbol_pattern.match(char) is not None
