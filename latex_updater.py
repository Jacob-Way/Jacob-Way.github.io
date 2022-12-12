import os
#from pdf2image import convert_from_path
from hashlib import md5

def update_equations(folder,page):
    html = ""
    with open(folder+r"/"+page+"_.html","r") as file:
        html = file.read()
    i = 0
    j=0
    while True:
        i = html.find("$",j+1)
        if i==-1:
            break
        j = html.find("$",i+1)
        equation = html[i+1:j]
        id = eqhash(equation)
        if not os.path.exists(folder+"/equations/"+id+".svg"):
            print("Latex Equation is: "+equation)
            tex2svg(equation,id,folder+"/equations/")
        replacement_tag = '<img class="latex-inline" src="equations/'+id+'.svg" alt="'+equation+'">'
        html = html[:i]+replacement_tag+html[j+1:]
    with open(folder+r"/"+page+".html","w") as file:
        file.write(html)
def tex2svg(latex_markup,id,folder):
    os.system('tex2svg "'+latex_markup+'" > '+folder+id+'.svg')
def eqhash(s):
    return md5(s.encode()).hexdigest()[-10:]
update_equations("projects/reviews/hearellipse","main")

