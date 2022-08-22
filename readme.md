# web fuzzing in Python
Simple fuzzing tool for web requests in Python.

## usage
`FUZZ` will be replaced with your input list.

``` bash
python3 webfuzz.py -i wordlist.txt -url 'http://www.domain.com/?param=FUZZ'
```

## setup
``` bash
pip3 install requests
```