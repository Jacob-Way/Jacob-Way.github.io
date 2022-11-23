import os
#from pdf2image import convert_from_path
from hashlib import md5

def update_equations(filepath):
    html = ""
    with open(filepath,"r") as file:
        html = file.read()
    i = 0
    j=0
    while True:
        i = html.find("<latex>",j)
        if i==-1:
            break
        j = html.find("</latex>",j)
        equation = html[i+7:j]
        print("Latex Equation is: "+equation)
        id = eqhash(equation)
        tex2svg(equation,id,filepath+"/../equations/")
        replacement_tag = '<img class="latex-inline" src="equations/'+id+'.svg" alt="'+equation+'">'
        html = html[:i]+replacement_tag+html[j+8:]
    with open(filepath,"w") as file:
        file.write(html)
def tex2svg(latex_markup,id,folder):
    os.system('tex2svg "'+latex_markup+'" > '+folder+id+'.svg')
def eqhash(s):
    return md5(s.encode()).hexdigest()[-10:]
update_equations("projects/notes/notes.html")

