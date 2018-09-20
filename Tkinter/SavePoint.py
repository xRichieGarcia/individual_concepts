#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import datetime
import os
import numpy as np


# In[2]:


class UploadPoint:
    """Used to create data point instances
    """
    def __init__(self):
        #time and moisture content
        self.t = datetime.datetime.now()
        self.m = np.random.normal(24, 8)
    def f(self):
        return 'yo'


# In[52]:


class Application(object):
    """Main class containing Tkinter application
    """
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Moisture Monitor')
        self.createWidgets()
        
    # --- commands
    
    
    # ---- buttons
    def createWidgets(self):
        
        self.savePoint = tk.Button(self.parent,
            text='Record Point',
            relief=tk.RAISED,
            background='#C0C0C0',
            command=self.parent.destroy
            )
                            
        self.quitButton = tk.Button(self.parent,
            text='Quit',
            relief=tk.RAISED, 
            background='#ff0000',
            command=self.parent.destroy)
                                            
    # --- placing onto root frame
        self.savePoint.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.quitButton.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)


# In[53]:


def main():
    root = tk.Tk()
    root.geometry('200x200')
    app = Application(root)
    root.mainloop()


# In[56]:


if __name__ =='__main__':
    main()


# In[ ]:




