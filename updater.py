from matplotlib import pyplot as plt
import pandas as pd
import os, sys

#Personal Modules
from prefs import projects_path

os.chdir(projects_path)
#Add something to the path
sys.path.insert(0, projects_path)
from Schedule import templates


#Globals
schedule_csv_path = r"data_files/schedule_data.csv"


def update_figures():
    data = pd.read_csv(schedule_csv_path)
    data = data.fillna(0)
    dates = data.iloc[:,0]
    levels = data.iloc[:,11:33].sum(1)

    #Activity Graph
    fig1 = templates.activity_tracker(dates,levels)
    fig1.savefig("Jacob-Way.github.io/images/fig1.svg")
    
def stage_commit_push():
    os.chdir("Jacob-Way.github.io")
    os.system('git commit -a -m "Updated Graphs"')
    os.system('git push origin main')
update_figures()
stage_commit_push()