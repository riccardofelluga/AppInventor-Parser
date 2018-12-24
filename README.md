# AppInventor_Parser

Simple and effective parser for the analysis of projects made with AppInventor.

## How it works

The python script take as input the path an AppInventor proect file(`.aia`) and outputs a `.csv` file with the following strucure:

| Index | Screen name | Block type | Depth | Attribute 1 | Value 1 | ... | Attribute n | Value n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | screenName.bky | block | 5 | type | component_set_get | ... | id | 27 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

The [results.csv](./results.csv) file is a sample extraction done on the December [app of the month](http://ai2.appinventor.mit.edu/?galleryId=5606663420772352).

## Future work

The current script is fairly simple in its structure, it can be improved by adding some analysis features in the future.

## References

* [AppInventor](http://appinventor.mit.edu/explore/)
* [AppInventor developers' page](http://appinventor.mit.edu/appinventor-sources/#documentation)
