# wordwisecreator

## Generate a `csv` dictionary of the language wanted from Amazon Kindle free dictionaries

Install or build mobitool
```
$ brew install libmobi
```

Download dictionary from Amazon and dump dictionary rawml text record
```
$ mobitool -d -o output_folder -P device_serival_number path_of_dict_azw 
```

Create `csv` from the `rawml`
```
python rawmp_to_csv.py
```

## Generate Kindle Wordwise for All type of Ebook (EPUB, MOBI, PRC, AZW3, PDF...)

You need to have [calibre](https://calibre-ebook.com/) on your device.

```
usage: php wordwisecreator.php input_file hint_level
input_file : path to file need to generate wordwise
hint_level : from 1 to 5 default is 5, 1 is less wordwise hint show - only hard word will have definition,
              5 is all wordwise hints show 
```
