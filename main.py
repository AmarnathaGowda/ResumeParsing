from typing import Union
import time
from fastapi import FastAPI,File,UploadFile
import uvicorn
import sys
import shutil
# import fitz
import textract
import textextracter


timestr = time.strftime("%Y-%m-%d-%H:%M:%S")

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello world"}

@app.post("/upload")
def upload_file(upload_file: UploadFile = File(...)):
    path =  F"files/{upload_file.filename}"
    with open(path, 'w+b') as file:
        shutil.copyfileobj(upload_file.file, file)

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

    text = textextracter.textextracterfromfile(filepath=path,text='')

    # text = text + getdatafromfile(path)

    
    
    return {
        'file': upload_file.content_type,
        'path': path,
        'content': text
    }
    

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)




                        