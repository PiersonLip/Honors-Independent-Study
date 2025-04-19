import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from pathlib import Path


# functions for making all of the graphs, saves them all with file names corrpsonding to the var used and conditons

# color_map_HR (variable, name_of_var, Log1 = 'F', S_R = 'T', minR = 1.5, maxR = 6.5)
#                
# variable = name of var in column to use for color
# name_of_var = variable name to be displayed  on the color bar
# log1 = whether or not to log it 
# S_R = whether or not to use the star radius, if not using one, replace with number to use for size
# minR = minimum y limit
# maxR = max y limit

def color_map_HR (DB, variable, name_of_var, title, saveLoc,  examplePoint = 'F', examplePointRange = 'F', exampleLum = 0, exampleTemp = 0, exampleTempMin = 0, exampleTempMax = 0, exampleLumMin =0, exampleLumMax = 0, Log1 = 'F', S_R = 'T', minR = 1.5, maxR = 6.5, ylimit = 'T', style = 'dark_background', fileName ='Default'):
    plt.style.use(style) #graph style
    fig, ax = plt.subplots(figsize = (8,8))  # create figure and axis
    ax.grid(True)  # turn on grid
    ax.set_axisbelow(True)  # make grid lines draw below plotted points
    ax.yaxis.grid(color='gray', linestyle='dashed')  # customize grid style
    
    cm = plt.colormaps['RdYlBu']  #This is the color map for the stars
    
    if S_R == 'T':
        r_dot= 10 ** DB['S2_log_R']
        # plt.suptitle("Size of dot corresponds to Donor radius", fontsize=10, family="monospace", color='.5')
    else:
        r_dot = S_R

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
    ax.set_title(title)
    ax.set_xlabel(r'$log_{10}$ Temperature [K]')
    ax.set_ylabel(r'$log_{10}$ Luminosity [$L_{\odot}$]')
    
    if ylimit == 'T':
        ax.set_ylim(minR, maxR)
    # axis scaling
    #plt.xscale('log')
    #plt.yscale('log')

    #scatter points. "cmap" is setting the colormap to use, "c" is setting the color itself (based on location), "s" is setting the size of the dot based off of star radii
    scatter = ax.scatter(Temp, Lum, cmap = cm, c = colors, s = r_dot)

    #set limits of graph (tada much better funciton then redefining limits manually)
    ax.invert_xaxis()

    # color bar stuff
    cbar = fig.colorbar(scatter, ax=ax, orientation='vertical')  # <-- link colorbar to that scatter
    cbar.set_label(name_of_var)  # <-- set the colorbar label separately
    
    #cbar.ax.invert_xaxis() #invert the color bar  (to match the inverted x scaling)
    #cbar.set_ticks([np.min(c),numpy.median,np.max(c),]) # remove the annoying ticks and labels

    if examplePoint == 'T':
        scatter = ax.scatter(np.log10(exampleTemp), np.log10(exampleLum),
         color = 'black', s = 100, marker = '*')
        if examplePointRange == 'T':

            log_temp_min = np.log10(exampleTempMin)
            log_temp_max = np.log10(exampleTempMax)
            log_lum_min = np.log10(exampleLumMin)
            log_lum_max = np.log10(exampleLumMax)

            # Calculate overlap (if any) — just to be explicit
            overlap_temp_min = log_temp_min
            overlap_temp_max = log_temp_max
            overlap_lum_min = log_lum_min
            overlap_lum_max = log_lum_max

            # Draw the rectangle for the overlapping region
            width = overlap_temp_max - overlap_temp_min
            height = overlap_lum_max - overlap_lum_min

            rect = patches.Rectangle(
                (overlap_temp_min, overlap_lum_min), width, height,
                linewidth=1, edgecolor='Black', facecolor='gray', alpha=0.2
            )
            ax.add_patch(rect)

    if S_R == 'T':
        S_R_STR = str(S_R)
    else:
        S_R_T = int(S_R)
        S_R_STR = str(S_R_T) 

    if fileName == 'Default':
        # Build a filename from components
        file_parts = [title, name_of_var, 'log10' if Log1 == 'T' else 'linear', 'star_radius' if S_R == 'T' else f'radius_{S_R_STR}']
        file_name = '_'.join(file_parts) + '.png'
    else:
        file_name = fileName if fileName.endswith('.png') else f"{fileName}.png"

    save_path = Path(saveLoc) / file_name
    plt.savefig(save_path, dpi=200)
    plt.style.use('default')
    plt.close() 