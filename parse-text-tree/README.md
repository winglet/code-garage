# parse a text tree
### example file inp_file contents:
```
+--- A
+--- B
|    +--- C
|    +--- D
|    +--- E
|    \--- F
+--- G
|    +--- H
|    +--- I
|    +--- J
|    \--- K
```
### command line: 
`python3 parse_text_tree.py inp_file`

### expected output:
```
B >>> C (i.e. B bears C)
B >>> D
B >>> E
B >>> F
G >>> H
G >>> I
G >>> J
G >>> K
```

### Credits:
Started off from code found here: https://stackoverflow.com/questions/6075974/python-file-parsing-build-tree-from-text-file

