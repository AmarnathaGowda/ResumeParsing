from typing import Union
import time
from fastapi import FastAPI,File,UploadFile
import uvicorn
import sys
import shutil
# import fitz
import textract
import textextracter
import spacy
import Entitys


timestr = time.strftime("%Y-%m-%d-%H:%M:%S")



app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello world"}

@app.post("/upload")
def upload_file(upload_file: UploadFile = File(...)):
    path =  F"files/{upload_file.filename}"
    print("1")
    print("Uploading file")
    with open(path, 'w+b') as file:
        shutil.copyfileobj(upload_file.file, file)

    print("2")
    print("Copied file")

    # return {
    #     'file': upload_file.file,
    #     'content': upload_file.content_type,
    #     'path': path
    # }

    # print(path)
    # data =" "
    # doc = fitz.open(path)

    # for page in doc:
    #     data = data + str(page.get_text())
    #     data = data.strip()
    #     data = ''.join(data.split())
    # return {"content ": data,"filename": file.filename}
        
    # def getdatafromfile(path):
    #     textdata = textract.process(path)
    #     print(textdata)

    #     textdata = textdata.decode()
    #     textdata = textdata.split('\n')
    #     textdata = "".join(textdata)

    #     return textdata
        
    # print(getdatafromfile(path))
    # text = getdatafromfile.getdatafromfile(path)

    print("3")
    print("passing data to fit")

    text = textextracter.textextracterfromfile(filepath=path,text='')

    # text = text + getdatafromfile(path)

    print(text.text)

    print("4")
    print("Loding Module")

   
    nlp = spacy.load("/Users/amarnathgowda/Desktop/ML_Project/ResumeParsing/SpacyProject/modeloutput/model-best")

    print("NLP Module is loded\n")
    print("Passing text to NLP Module\n")
    doc=nlp(text.text)

    print("5")
    print("Entity Creations")

    _Name=""
    EmailID=""
    PhoneNumber=""
    Location=""
    Organization=""
    Designation=""
    Duration=""
    Project1=""
    Project2=""
    Skills=""
    Qualifications=""
    Collage=""
    G_year=""
    Excperience=""

    for ent in doc.ents:
        print(ent.text, " ->>>>> ", ent.label_)
        if ent.label_ == "NAME":
            _Name = ent.text
        if ent.label_ == 'EMAILID':
            EmailID = ent.text
        if ent.label_ == 'PHONENUMBER':
            PhoneNumber = ent.text
        if ent.label_ == 'LOCATION':
            Location = ent.text
        if ent.label_ == 'ORGANIZATION':
            Organization = ent.text
        if ent.label_ == 'DESIGNATION':
            Designation = ent.text
        if ent.label_ == 'DURATION':
            Duration = ent.text
        if ent.label_ == 'PROJECT1':
            Project1 = ent.text
        if ent.label_ == 'PROJECT2':
            Project2 = ent.text
        if ent.label_ == "QUALIFICATION":
            Qualifications = ent.text
        if ent.label_ == 'COLLAGE':
            Collage = ent.text
        if ent.label_ == 'G_YEAR':
            G_year = ent.text
        if ent.label_ == 'EXPERIENCE':
            Excperience = ent.text
        if ent.label_ == 'SKILLS':
            Skills = Skills+ent.text


    # en = Entitys(_Name,EmailID,PhoneNumber,Location,Organization,Designation,Duration,Project1,Project2,Skills,Qualifications,Collage,G_year,Excperience)
        
    print("6")
    print("sending respoce of entry")

    return {
        'file': upload_file.content_type,
        'path': path,
        'content': text.text,
        'Name':_Name,
        'EmailID':EmailID,
        'PhoneNumber':PhoneNumber,
        'Location': Location,
        'Excperience': Excperience,
        'Organization': Organization,
        'Designation': Designation,
        'Duration': Duration,
        'Project1': Project1,
        'Project2': Project2,
        'Qualifications':Qualifications,
        'Collage': Collage,
        'G_year': G_year,
        'Skills': Skills
    }
    

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)




                        