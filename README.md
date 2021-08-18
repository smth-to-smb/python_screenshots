# Screenshot tools

This repository contains Python scripts which automate repeated actions
a technical writer need to take while working with lots of screenshots.

Currently, this repository contains the following files:

* `json_config.json` contains settings and discussed in the **Configuration** section of this document
* `config_parsing.py` is the universal configuration parser of the `json_config.json` file
* `filerename.py` contains the script which moves screenshot files, renames them, and returns a Markdown-formatted link in the CLI. Functionality of this script is discussed in the **Renaming files** section of this document

## Confniguration

Currently, `json_config.json` contains several configuration parameters listed
in the table below:


|Parameter name |Description  |Example|
--- | --- | ---
|`imagesfoldername`|Specifies the folder in the current project folder.|`python_images`|
|`imagesfolderpath`|Contains the absolute path to the project folder prior to the `imagesfoldername` parameter.|`/home/anton/Desktop/`|
|`imagesnamingpattern`|Pattern for screenshot file naming.|`test_screenshot_`|
|`defaultcaption`|Default name for markdown captions used with the skip option.|`Image`|
|`screenshotstartswith`|The first word of the source screenshot filename.|`Screenshot`|
|`screenshotsourcefolderpath`|Source folder all screenshot files should be moved from.|`/home/anton/Pictures/`|

Using configuration examples from this table, running the `filerename.py` script
you will be able to automatically move
screenshot files with names starting from the `Screenshot` word from the
`/home/anton/Pictures/` folder to the `/home/anton/Desktop/python_images`
folder. After moving,
each screenshot file will be named like `test_screenshot_1.png`,
`test_screenshot_2.png`, and so on.

Choosing the *skip* option of the `filerename.py` script, you will get the
Markdown links of the following format:

```
![Image](/home/anton/Desktop/python_images/test_screenshot_1.png)
```

If you specify the caption (like `This is the caption text`) while running this
script, it will produce the following output:

```
![This is the caption text](/home/anton/Desktop/python_images/test_screenshot_1.png)
```