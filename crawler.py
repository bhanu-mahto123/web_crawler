import urllib.request
import re
import requests
from google_drive_downloader import GoogleDriveDownloader as gdd
from bs4 import BeautifulSoup
from pydrive.auth import GoogleAuth
#connect to a URL
website = urllib.request.urlopen('https://www.pythonforbeginners.com/code/regular-expression-re-findall')
url = "https://www.gate2016.info/ies-electrical-previous-years-objective-papers/"
#print(website)
#html = getPagehtml(url);
#read html code
html = website.read().decode('utf-8')
#print(html)
#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
# for i in range(len(links)):
#  print(links[i])

def get_pdf_links(url,end_type): 
      
    # create response object 
    r = requests.get(url) 
      
    # create beautiful-soup object 
    soup = BeautifulSoup(r.content,'lxml') 
      
    # find all links on web-page 
    links = soup.findAll('a') 
    # print(link
    # s)
    # filter the link sending with .mp4 
    pdf_links = [ link['href'] for link in links if link['href'].endswith(end_type)] 

    return pdf_links 

pdf_links = get_pdf_links(url,'?usp=sharing')
print(type(pdf_links))
print(len(pdf_links))  
# file1 = open("link.txt","w") 
# for i in range(len(pdf_links)):
#     pdf_links[i].replace("https://www.gate2016.info/download.php#https://drive.google.com/file/d",'')
# # r = get_pdf_links(pdf_links[0],'pdf')
# print(r)
year = 2019
bin=0
file1 = open("link.txt","w") 
for i in range(len(pdf_links)):
    filename = "IES_QUESTION_PAPER"+str(i)+".pdf"
    pdf_links[i]=pdf_links[i].replace("https://www.gate2016.info/download.php#",'')
    pdf_links[i]=pdf_links[i].replace("https://drive.google.com/file/d/",'')
    pdf_links[i]=pdf_links[i].replace("/view?usp=sharing",'')
    pdf_links[i]="https://drive.google.com/uc?authuser=0&id="+pdf_links[i]+"&export=download"     
    r1 = requests.get(pdf_links[i], stream = True)
    with open(filename,"wb") as pdf:
        for chunk in r1.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
    file1.write(pdf_links[i]+'\n')
# file2 = open("link.txt","r")
# print(type(file2.readlines()))
# # b = file2.readlines()with open("python.pdf","wb") as pdf: 
#     for chunk in r.iter_content(chunk_size=1024): 
  
#          # writing one chunk at a time to pdf file 
#          if chunk: 
#              pdf.write(chunk) 
# print(len(b))
#gdd.download_file_from_google_drive(file_id=pdf_links[0],dest_path='./mnist.zip',unzip=True)
ab = pdf_links[0].replace("https://drive.google.com/file/d/",'')
ab = ab.replace("/view?usp=sharing",'')
print("https://drive.google.com/uc?authuser=0&id="+ab+"&export=download")
#https://drive.google.com/uc?authuser=0&id=1Wy3zSr1JtKrs1-ZNifhq65xeVgHZ9-cc&export=download