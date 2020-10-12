# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:34:44 2020

@author: Charles Gras-Najjar
"""
import ast
import numpy as np
import matplotlib.pyplot as plt

joint_entries = "Joint #2, Joint #3, Joint #4, Joint #5, Joint #6, Joint #7, Joint #8, Joint #9, Joint #10, Joint #12, Joint #13"
joint = input(joint_entries +"Enter one of the above joints (case sensitive): ") 

if joint not in joint_entries:
    joint = input("Try again. Enter one of the following (case sensitive): Joint #2, Joint #3, Joint #4, Joint #5, Joint #6, Joint #7, Joint #8, Joint #9, Joint #10, Joint #12, Joint #13")
    
def Render_Coordinates(joint):
    
    reset_data = "New motion!"
    joint_coords = []
    count = 0
    
    coords = ""
    
    with open("coords.txt","r") as source:
        for line in source:
            line = line.strip()
            
            if joint in line:
                length = len(line)
                
                # Pinpoint x,y coordinates by finding index of  first parentheses and second comma, since they are in format (xx,yy,zz) 
                comma_index_1  = line.index(",")
                comma_index_1 = comma_index_1+1
                comma_index_2  = line.index(",",comma_index_1,length)
                paren_index_1 = line.index("(")
                paren_index_1 = paren_index_1+1
                coords = line[paren_index_1:comma_index_2]
                
                #Format from str to int
                coords = ast.literal_eval(coords)
                
                #append to list
                joint_coords.append(coords)
                count = count+1
                    
            if reset_data in line:
                
                if count == 0:
                    continue
                
                #if list empty for some reason, skip to next motion
                if len(joint_coords) < 2:
                    continue
                
                #Format to NP array and plot
                joint_coords = np.array(joint_coords)
                x,y = joint_coords.T
                plt.xlabel('X coordintes - '+joint)
                plt.ylabel('Y coordintes - '+joint)
                plt.plot(x,y)
                filename = joint+" "+str(count)+".png"
                plt.show()
                
                filepath = "insert filepath here"
                plt.savefig(filepath+filename)
                plt.clf()
                
                #Resest array
                joint_coords = []
                
Render_Coordinates(joint)