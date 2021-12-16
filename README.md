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

## Bibliography

### https://github.com/xnohat/wordwisecreator
PHP code to add WordWise to ebooks in any format. All I need is to create a CSV for German. 

### https://github.com/xnohat/wordwise-dict
Create a `CSV` from the Kindle WordWise dabatase. This is available only for English, so it's of no direct use to me.

### https://github.com/tmilovanov/wisecreator
Add (embed) WordWise in MOBI and AZW3 files. Utility for adding word wise information to non amazon books.

I'll have a look later after I solved the German CSV dictionary thing. For the moment, I can live with the PHP.

### https://github.com/xxyzz/WordDumb
In this folder (https://github.com/xxyzz/WordDumb/tree/master/klld), it has code to generate WordWise in other languages but always from English: instead of displaying the explanation in english, it displays it in another language but the base is always english so it doesn't work if the book language is not English.

Useful code to read from the Kindle Oxford dictionaries though.

### https://github.com/pettarin/penelope
It works nice converting kobo dicts to csv but can only convert the index and not the actual definition. So, useless.


https://pgaskin.net/dictutil/dicthtml/format.html

https://github.com/pgaskin/dictutil/releases/tag/v0.3.2
