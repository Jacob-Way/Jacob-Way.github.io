import os
from pdf2image import convert_from_path
from hashlib import md5

def update_equations(filepath):
    html = ""
    with open(filepath,"r") as file:
        html = file.read()
    i = 0
    while True:
        i = html.find("<latex>",i)
        j = html.find("</latex>",i)
        equation = html[i+7:j]
        print("Latex Equation is: "+equation)
        id = eqhash(equation)
        print("Hash of this equation is: "+str(id))
        html = html[:i]+html[j+8:]
        latex_code =  r"\documentclass[border=0cm]{standalone}\usepackage{tikz}\begin{document}\begin{tikzpicture}\node at (0,0) {\Huge $"+equation+r"$};\end{tikzpicture}\end{document}"
        latex2png(latex_code,id,"filepath/../equations/")
        break
def latex2pdf(latex_markup,filename,folder):
    f = open(filename+".tex","w")
    f.write(latex_markup)
    f.close()

    os.system("pdflatex "+filename+".tex")
    os.remove(filename+".aux")
    os.remove(filename+".log")
    os.remove(filename+".tex")
    if os.path.exists(folder+filename+".pdf"):
        os.remove(folder+filename+".pdf")
    os.rename(filename+".pdf", folder+filename+".pdf")
def latex2png(latex_markup,filename,folder):
    latex2pdf(latex_markup,filename,folder)
    image = convert_from_path(folder+filename+".pdf")
    image[0].save(folder+filename+".png","PNG")
    os.remove(folder+filename+".pdf")
def eqhash(s):
    return md5(s.encode()).hexdigest()[-10:]
def main():
    markup = r"\documentclass[border=0cm]{standalone}\usepackage{tikz}\begin{document}\begin{tikzpicture}\node at (0,0) {\Huge $e^{i\pi}=-1$};\end{tikzpicture}\end{document}"
    latex2png(markup,eqhash(markup),"projects/testproject/equations/")
update_equations("projects/testproject/test.html")