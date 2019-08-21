
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import PyPDF2



class App(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.label_frame = tk.Frame(self.master)
        self.label_frame.grid()

        self.label_list = []
        self.pdfFiles = []

        self.label_list.append(tk.ttk.Button(self.label_frame, text="Browse file to combine", command=self.add_new_data))
        self.label_list.append(tk.Entry(self.label_frame, text='Name of combined file'))
        self.label_list.append(tk.ttk.Button(self.label_frame, text="Combine!", command=self.combine))
        self.label_list[0].grid(row=0)
        self.label_list[1].grid(row=1, column=1)
        tk.Label(self.label_frame,text="Combine file name").grid(row=1)
        self.label_list[2].grid(row=2)

    def add_new_data(self):
        filename = tk.filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
        if filename != None:
            self.pdfFiles.append(filename)
            self.label_list.append(tk.Label(self.label_frame, text=str(filename.name)))

            for widget in self.label_frame.children.values():
                widget.grid_forget() 

            for ndex, i in enumerate(self.label_list):
                i.grid(row=ndex)

    def combine(self):
        pdfWriter = PyPDF2.PdfFileWriter()

        # Loop through all the PDF files.
        for filename in self.pdfFiles:
                #pdfFileObj = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(filename)

                # Loop through all the pages and add them.
                for pageNum in range(0, pdfReader.numPages):
                        pageObj = pdfReader.getPage(pageNum)
                        pdfWriter.addPage(pageObj)

        # Save the resulting PDF to a file.
        pdfOutput = open(self.label_list[1].get()+'.pdf', 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()


if __name__ == "__main__":
    root = tk.Tk() 
    my_app = App(root)
    my_app.mainloop()