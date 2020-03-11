# Консольная утилита для поиска всех ссылок по запросу

## Установка
```python
python setup.py bdist_wheel
cd dist
pip install outs-0.1-py-none-any.whl
```
### Использование
```python
find -t, --text "searchtext"
     -s, --system searchsystem [google.com, ya.ru, bing.com]
     -c, --count result_count [1, 100, 1000]
     -o, --output outputformat [cmd, json, cvs]
     -r, --recursion is_recursion
```
