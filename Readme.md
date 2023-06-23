# Filename Parser
ファイル名にファイルの属性を記述したとき、それを分解して、辞書形式やPandas形式に変換するユーティリティ。

# Installation
1. git cloneする
2. `pip install /path/to/repository`

# Usage
## Import
```python
from fnparser import parser
```

## １つだけパースする
```python
file = "Tokyo_0001_0_1.wav"
parser.parse_single(file, delimiter="_", filenameformat="City_SubID_TestID_repetition")
# filenameformatで、ファイル名のどの位置に何の情報が入っているかを指定できる。

# {'City': 'Tokyo',
#  'SubID': '0001',
#  'TestID': '0',
#  'repetition': '1',
#  'nelems': 4,
#  'original': 'Tokyo_0001_0_1.wav'}
```

## 複数をまとめてパースする
```python
files = list(Path(".").glob("**/*.wav"))
print(files)
# "Tokyo_0001_0_1.wav"
# "Osaka_0002_1_1.wav"
# "Hiroshima_0003_2_1.wav"
parser.parse_multiple(files, delimiter="_", filenameformat="City_SubID_TestID_repetition")

#         City SubID TestID repetition nelems              original
# 0      Tokyo  0001      0          1    4      Tokyo_0001_0_1.wav
# 1      Osaka  0002      1          1    4      Osaka_0002_1_1.wav
# 2  Hiroshima  0003      2          1    4  Hiroshima_0003_2_1.wav
```

# License

"Filename Parser" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

