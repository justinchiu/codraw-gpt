# codraw-gpt

## Installation
Requires poetry.
```
poetry install
poetry shell
pip install -e .
```

## Preliminary experiment: Drawing a bicycle
We experiment with drawing a bicycle via reflection,
inspired by this [tweet](https://twitter.com/evanthebouncy/status/1712590544919245265).

Execute the following from the root of this repository.
```
# generate the chalk code, which will save in `outputs/bicycle.py`
python codraw/bicycle.py
# generate `bicycle.svg`
python outputs/bicycle.py
open bicycle.svg
```
![alt text](httphttps://github.com/justinchiu/codraw-gpt/blob/main/bicycle.svg?raw=true)
