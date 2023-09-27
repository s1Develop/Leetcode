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


- Creating a Counter object: 
        - The Counter function takes a string s as input and returns a Counter object, 
        - which is a dictionary where keys are the characters in s
        - and values are the counts of each character.
        - with a given str s, 대충 각 alphabet을 key로 잡고 그 애들의 count를 value로 잡는 dictionary를 만든다
        - ```python
            count = collections.Counter(s)
          ```

- The enumerate function is used to get both the index (idx) and character (c) of the string s.
```python
for idx, c in enumerate(s):
```
