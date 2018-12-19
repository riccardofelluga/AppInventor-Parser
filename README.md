# AppInventor_Parser

Simple and effective parser for the analysis of projects made with AppInventor

## How it works

The python script take as input the path an AppInventor proect file(`.aia`) and outputs a `.csv` file with the following strucure:

| Index | Screen name | Block type | Depth | Attribute 1 | Value 1 | ... | Attribute n | Value n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | screenName.bky | block | 5 | type | component_set_get | id | 27 | inline | FALSE
| ... | ... | ... | ... | ... | ... | ... | ... | ... |