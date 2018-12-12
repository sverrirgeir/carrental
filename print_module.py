from win32com.client import Dispatch
MYDIR = './data/cars.txt'

def simple():
    myWord = Dispatch('Word.Application')
    myWord.Visible = 1 # comment out for production

    myDoc = myWord.Documents.Add()
    myRange = myDoc.Range(0,0)
    with open('./data/cars.txt', "r") as printf:
        for line in printf:
            myRange.InsertBefore(line)

    #uncomment these for a full script
    #myDoc.SaveAs(MYDIR + '\\python01.doc')
    myDoc.PrintOut()
    #myDoc.Close()
simple()