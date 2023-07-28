import click
import csv

@click.command
@click.option('--csv_file', help='csv file containing all records')

def convert(csv_file):
    with open(csv_file, 'r') as source:
        reader = csv.DictReader(source, delimiter=',')
        vcf_file = open('nextcloud.vcf', 'w')
        i = 0
        for row in reader:
            vcf_file.write(f"BEGIN:VCARD\n")
            vcf_file.write(f"VERSION:4.0\n")
            vcf_file.write(f"FN:{row['first_name']} {row['last_name']}\n")
            vcf_file.write(f"EMAIL;TYPE=HOME:{row['email']}\n")
            vcf_file.write(f"TEL;TYPE=CELL:{row['mobile']}\n")
            vcf_file.write(f"BDAY;VALUE=DATE:{row['birthday']}\n")
            vcf_file.write(f"ADR;TYPE=HOME:;;{row['street']};{row['city']};{row['state']};{row['postal_code']};{row['country']}\n")
            vcf_file.write( 'END:VCARD' + "\n")
            vcf_file.write( "\n")
            i += 1
    
        vcf_file.close()
        print(f"{str(i)} vcf cards were generated")

if __name__ == '__main__':
    convert()
