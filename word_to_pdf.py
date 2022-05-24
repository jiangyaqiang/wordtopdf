#coding=utf-8
import os
from win32com import client
import re
def doc2pdf(wordpath,pdfpath):
    # testfile = "C:\\Users\Administrator\Desktop\pdf"
    for root,dirs,files in os.walk(wordpath,topdown=False):#遍历文件夹
        for name in files:
            if name.find('doc') > 0 or name.find('docx') > 0:
                doc_name = os.path.join(root,name)
                # pdf_name = doc_name.split('.docx',)[0] + '.pdf'
                (filename,extension) = os.path.splitext(name)#filename文件名，extension后缀名
                #pdf_name为pdf文件名，此处不加.pdf也可以，但是word名中有‘.’的时候会发生转化失败
                r = root.replace('word','pdf')
                pdf_name = os.path.join(root,filename)+'.pdf'
                print(pdf_name)
                try:
                    word = client.DispatchEx('Word.Application')
                    if os.path.exists(pdf_name):
                        os.remove(pdf_name)
                    worddoc = word.Documents.Open(doc_name,ReadOnly = 1)
                    worddoc.SaveAs(pdf_name,FileFormat = 17)
                    worddoc.Close(True)
                    word.Quit()#切记，这步必须加，要不然线程不会杀死，电脑会卡死
                    print("success")
                except Exception as e:
                    print(e)
                    print("error")
                    return 1
if __name__ == '__main__':
    wordpath = input('[+] 请给出word文档所在路径：')
    # wordpath = "C:\\Users\Administrator\Desktop\word"#word存放路径
    pdfpath = "C:\\Users\Administrator\Desktop\pdf"#word转PDF后存放路径
    doc2pdf(wordpath,pdfpath)
