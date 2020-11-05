# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:34:44 2020
@author: Charles Gras-Najjar
"""
import ast
import numpy as np
import matplotlib.pyplot as plt

joint_entries = ["Joint #1","Joint #2", "Joint #3", "Joint #4", "Joint #5", "Joint #6", "Joint #7", "Joint #8", "Joint #9", "Joint #10","Joint #11", "Joint #12", "Joint #13","Joint #14","Joint #15","Joint #16","Joint #17","Joint #18"]

start_button= input("Hit enter to generate plots... ") 

def Render_Coordinates(joint_entries):
    
    for i in joint_entries:
    
        
        print("Generating plots for " +i+"...")
       
        reset_data = "New motion!"
        joint_coords = []
        count = 0
        coords = ""
        
        with open("Group_Box.txt","r") as source:
            for line in source:
                line = line.strip()
                
                if i in line:
                    
                    # Pinpoint x,y coordinates by finding index of  first parentheses and second comma, since they are in format (xx,yy,zz) 
                    comma_index_1  = line.index(",")
                    comma_index_1 = comma_index_1+2
                    paren_index_1 = line.index(")")
                    
                    coords = line[comma_index_1:paren_index_1]
                    
                    #Format from str to int
                    coords = ast.literal_eval(coords)
                    
                    #append to list
                    joint_coords.append(coords)
                    count = count+1
                        
                if reset_data in line:
                    
                    if count == 0:
                        continue
                    
                    #if list empty for some reason, skip to next frame
                    if len(joint_coords) < 2:
                        continue
                    
                    filepath = "insert path here\\"+i+"\\"
                    filename = i+" "+str(count)+".png"
                    
                    #Format to NP array and plot
                    joint_coords = np.array(joint_coords)
                    x,y = joint_coords.T
                    plt.plot(x,y,color = "black")
                    plt.axis("off")
                    figure = plt.gcf()
                    figure.set_size_inches(3.56,3.56)
                    figure.savefig(filepath+filename)
                    figure.clf()
                    plt.close(figure)
                    
                    #Resest array
                    joint_coords = []
        # plt.show()

                
# Render_Coordinates(joint_entries)
