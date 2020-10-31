#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:36:13 2020

@author: creed
"""

import pandas as pd
import matplotlib.pyplot as plt
import PyGnuplot as pgnu

drop1 = pd.read_table("flat_240_350_gnu/100-0.03-344.0.gnu",sep = ' ', header=None)

plt.plot(drop1.iloc[:,0], drop1.iloc[:,1],linewidth=0.5)
plt.gca().set_xlim(-2,238)
plt.gca().set_ylim(0,4)
plt.gca().set_aspect(aspect = 'equal')
plt.show()

pgnu.c("set size ratio -1")
pgnu.c(" plot 'flat_240_350_gnu/100-0.03-344.0.gnu' using 1:2 with lines")


