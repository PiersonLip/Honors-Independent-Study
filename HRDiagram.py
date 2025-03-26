# functions for making all of the graphs, saves them all with file names corrpsonding to the var used and conditons

# color_map_HR (variable, name_of_var, Log1 = 'F', S_R = 'T', minR = 1.5, maxR = 6.5)
#                
# variable = name of var in column to use for color
# name_of_var = variable name to be displayed  on the color bar
# log1 = whether or not to log it 
# S_R = whether or not to use the star radius, if not using one, replace with number to use for size
# minR = minimum y limit
# maxR = max y limit

import matplotlib.pyplot as plt
import numpy as np
def color_map_HR (DB, variable, name_of_var, title, saveLoc, Log1 = 'F', S_R = 'T', minR = 1.5, maxR = 6.5, ylimit = 'T', style = 'dark_background'):
    plt.figure(figsize = (8,8))
    cm = plt.colormaps['RdYlBu']  #This is the color map for the stars

    if S_R == 'T':
        r_dot= 10 ** DB['S2_log_R']
        plt.suptitle("Size of dot corresponds to Donor radius", fontsize=10, family="monospace", color='.5')
    else:
        r_dot = S_R
        
    plt.style.use(style) #graph style

    # assings axis
    Temp = np.log10((((10 ** DB['S2_log_L'])/(10 ** DB['S2_log_R'])**2)**.25) * 5772)
  
    Lum = DB['S2_log_L']

    # binds the color of the scatter points to the x location (temp) of the star
    if Log1 == 'T':
        c = np.log10(DB[variable])
    else:
        c = (DB[variable])
    colors = c

    # labels
    plt.title(title)
    plt.xlabel(r'$log_{10}$ Temperature [K]')
    plt.ylabel(r'$log_{10}$ Luminosity [$L_{\odot}$]')
    
    if ylimit == 'T':
        plt.ylim(minR, maxR)
    # axis scaling
    #plt.xscale('log')
    #plt.yscale('log')

    #scatter points. "cmap" is setting the colormap to use, "c" is setting the color itself (based on location), "s" is setting the size of the dot based off of star radii
    plt.scatter(Temp, Lum, cmap = cm, c = colors, s = r_dot)
    #set limits of graph (tada much better funciton then redefining limits manually)
    plt.gca().invert_xaxis()

    # color bar stuff
    cbar = plt.colorbar(orientation='vertical', label = name_of_var) #sets the colorbar to be horizontal instead of default
    
    #cbar.ax.invert_xaxis() #invert the color bar  (to match the inverted x scaling)
    #cbar.set_ticks([np.min(c),numpy.median,np.max(c),]) # remove the annoying ticks and labels
    if S_R == 'T':
        S_R_STR = str(S_R)
    else:
        S_R_T = int(S_R)
        S_R_STR = str(S_R_T) 
    F_Name = saveLoc, title, name_of_var, 'log10', Log1, 'star radius', S_R_STR
    F_Name_str = ' '.join(F_Name)
    print(F_Name_str)
    plt.savefig(F_Name_str, dpi=200)
    plt.style.use('default')