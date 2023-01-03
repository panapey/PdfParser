import glob
import os
from pdf2docx import parse

docx_file = 'PdfToWord.docx'


class PdfParser:
    @staticmethod
    def pars(pdf, docx):
        try:
            parse(pdf, docx)
        except:
            print('Conversion Failed')

        else:
            print('File Converted Successfully')

    @staticmethod
    def find_file(direct):
        try:
            os.chdir(direct)
            for file in glob.glob("*.pdf"):
                return file
        except:
            print('Failed')


if __name__ == '__main__':
    parser = PdfParser()
    parser.pars(parser.find_file('Files/'), docx_file)
