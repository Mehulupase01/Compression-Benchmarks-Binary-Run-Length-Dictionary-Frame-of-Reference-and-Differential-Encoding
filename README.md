# ADM Assignment 3
We have 26 programs with the following break up:
24 programs for 
- Binary
- Frame of Reference
- Differential

For these programs we have 8 individual programs for each, 4 encoding and 4 decoding programs for int8, int16, int32, int64 respectively
To run these programs we would run the following commands:
### Encode
```
python <program-en-for|bin|dif-int8|16|32|64.py> <Filename.csv> 
```

### Decode
```
python <program-de-for|bin|dif-int8|16|32|64.py> <Filename.csv.for|dif|bin> 
```

2 programs for
- run length encoding
- Dictionary

To run these programs we have to run the following command
### Run Length Encoding (rle.py)
#### Encode
```
python rle.py en|de rle int8|16|32|64 file_path
```
#### Decode
```
python rle.py en|de rle int8|16|32|64 file_path
```

### Dictionary (program-dic.py)
#### Encode
```
python program-dic.py en|de dic int8|16|32|64 file_path
```
#### Decode
```
python program-dic.py en|de dic int8|16|32|64 file_path
```
