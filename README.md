# CSV2VCF

Convert a CSV file to a VCF contacts file. 

The VCF format was defined for importing contacts into a [nextcloud](https://nextcloud.com) instance.

Having a CSV file in following format:

```csv
first_name,last_name,email,mobile,birthday,street,city,state,postal_code,country
yahuar,locro,yahuar@locro.com,012345678909,1990-09-09,Mystreet Av. 69,mycity,mystate,555555,mycountry
```

Returns it into

```bash
BEGIN:VCARD
VERSION:4.0
FN: yahuar locro
EMAIL;TYPE=HOME:yahuar@locro.com
TEL;TYPE=CELL:12345678909
BDAY;VALUE=DATE:1990-09-09
ADR;TYPE=HOME:;;Mystree Av. 69;mycity;mystate;55555;mycountry
END:VCARD
``````

# Usage

1. Create a python virtual ennvironment
```bash
    $ virtualenv -p python3.11 venv
```

2. Install requirements
```bash
    $ pip install -r requirements.txt
```

3. Run the program. As *csv_file* argument pass the path to the CSV file

```bash
    $ python main.py --csv_file ./contact.csv
```

4. Get some help
```bash
    $ python main.py --help
```


The program returns a file named *nextcloud.csv* within the same directory