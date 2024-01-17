import textract

class textextracterfromfile:

    def __init__(self, filepath,text):
        self.filepath = filepath
        self.text = text

        if '.pdf' in filepath:
            self.text = textract.process(self.filepath)
            print(self.text)

            self.text = self.text.decode()
            self.text = self.text.split('\n')
            self.text = "".join(self.text)
        else:
            self.text='not a valid PDF file'

    def __str__(self):
        return self.text