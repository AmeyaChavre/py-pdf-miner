import csv
import gdown
import PyPDF2
import re

f = open('C:\\Users\\acer\\Desktop\\find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(f)
extracted_data = list(csv_data)


url=""
for letter in range(len(extracted_data)):
    url+=(extracted_data[letter][letter])
print(f"The extracted/hidden URL in find_the_link.csv is : {url}")



mod_url = url.replace("open","uc")

gdown.download(mod_url,'C:\\Users\\acer\\Desktop\\Find_the_Phone_Number.pdf',quiet=False)
print("File : Find_the_Phone_Number.pdf has been downloaded.")
#Make sure that other programs are not accessing this .pdf or else program will throw OS error (Permission Denied)
f.close()

f_pdf = open('C:\\Users\\acer\\Desktop\\Find_the_Phone_Number.pdf','rb')

read_pdf = PyPDF2.PdfFileReader(f_pdf)

print(f"Number of pages in .pdf file : {read_pdf.numPages}")

all_content=[]

for page_num in range(read_pdf.numPages):
    all_content.append((read_pdf.getPage(page_num)).extractText())

#print(f"Entire Content : {all_content}")

content_str = ""

for c in all_content:
    content_str+=str(c)
#print(content_str)

count=0
for phone_no in re.finditer(r'(\d{3}).(\d{3}).(\d{4})',content_str):
    count+=1
    print(f"\tPhone Number {count}: {phone_no.group()}\n")
    print(f"\tPhone Number Area Code : {phone_no.group(1)}\n")
print(f"\tThere is/are {count} phone number(s) in the pdf file.")

f_pdf.close()
