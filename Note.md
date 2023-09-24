# Data Structure

## List (ex. ['a','b','cd'])
- mutable (can make changes)

## Tuples (ex. (1,2,'a','b'))
- immutable (cannot make changes after creating it)

## Set (ex. {1,2,3,'hello'})
- mutable 
- have no duplicate elements

## Dictionary (ex. {'key1:'value1', 'key2':'value2})
- mutable
- no duplicates key
- type of key can be anything
- 특정 key의 value값을 가져오려면 (to see indivisual values)
    - DictName.get('key1') -> value1
    - DictName['key1']
- 새로운 key, value를 넣으려면 (inserting new key:value pair)
    - DictName['newKey'] = 'newValue'
- DictName.items() returns a view object
### 응용
``` python
d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}
keys = [k for k, v in d.items() if v == 'aaa']
print(keys) # ['key1', 'key2']
```
- list(DictName) will return a list of keys as a list
