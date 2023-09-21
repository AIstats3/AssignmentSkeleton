def Polo_Draw():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.patches import RegularPolygon
    import matplotlib.image as image
    plt.rcParams['figure.figsize'] = [8, 12]
    fig, ax = plt.subplots() ##Create the axis
    ax.axis([-300,300,-200,500]) ##Set axis size
    ax.clear() ##Clear any existing images
    ax.axis("off")##Makes axes invisible because who wants to look at those
    file="Willie Mays Small.png" ##Importing picture of Willie Mays
    Willie=image.imread(file)

    theta_back=np.linspace(np.pi,2*np.pi) ##Setting for a top open semi-circle
    back_radius=135
    plt.plot(back_radius*np.cos(theta_back),back_radius*np.sin(theta_back),color='Green')##Adds semi-circle behind home plate
    diamond=RegularPolygon((0,0),numVertices=4,radius=60.5, color='Brown')##Creates baseball diamond
    ax.add_patch(diamond) ##Adds baseball diamond
    ##Bases
    fB=RegularPolygon((57.5,0),numVertices=4,radius=2, color='White')
    ax.add_patch(fB) 
    sB=RegularPolygon((0,57.5),numVertices=4,radius=2, color='White')
    ax.add_patch(sB)
    tB=RegularPolygon((-57.5,0),numVertices=4,radius=2, color='White')
    ax.add_patch(tB)
    hB=RegularPolygon((0,-57.5),numVertices=4,radius=2, color='White')
    ax.add_patch(hB)
    
    ##Adding field boundaries
    plt.plot([-135,-135],[0,60.5],color='Green')
    plt.plot([135,135],[0,60],color='Green')
    plt.plot([-135,-198],[60.5,60.5],color='Green')
    plt.plot([135,182.5],[60,60],color='Green')
    plt.plot([0,-198],[-60.5,137.5],color='Green')
    plt.plot([0,182.5],[-60.5,122],color='Green')
    plt.plot([-198,-198],[60.5,415],color='Green')
    plt.plot([182.5,182.5],[60,415],color='Green')
    plt.plot([-188,-30],[425,425],color='Green')
    plt.plot([30,172.5],[425,425],color='Green')
    plt.plot([-30,-30],[425,475],color='Green')
    plt.plot([30,30],[425,475],color='Green')
    plt.plot([-30,30],[475,475],color='Green')
    
    ##Outfield curved wall boundaries
    top_radius=10
    theta_top_L=np.linspace(np.pi/2,np.pi)
    plt.plot((-198+top_radius)+top_radius*np.cos(theta_top_L),(425-top_radius)+top_radius*np.sin(theta_top_L),color='Green')
    theta_top_R=np.linspace(0,np.pi/2)
    plt.plot((182.5-top_radius)+top_radius*np.cos(theta_top_R),(425-top_radius)+top_radius*np.sin(theta_top_R),color='Green')
    
    ##Adds picture of Willie and annotates
    from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
    imagebox = OffsetImage(Willie, zoom = 0.15)
    ab = AnnotationBbox(imagebox, (45, 400), frameon = False)
    ax.add_artist(ab)
    plt.text(0,350,"Willie Mays: 'The Catch'",fontsize=10)
    plt.text(0,360,"September 9th, 1954",fontsize=10)
    plt.arrow(20,250,20,100,shape='full',length_includes_head=True,head_width=0.2,color='Green',linestyle=(5, (3,9)))
    starting_point=plt.Circle((20,250),radius=2,color='Green')
    ax.add_patch(starting_point)
    plt.text(0,240,"Where Willie Mays was when the ball was hit",fontsize=8)
    plt.text(35,300,"Dist. covered ~115 ft. Time ~5.7s",fontsize=8)
    plt.text(40,294,"*Expected catch probability:<=0.02",fontsize=6)
    plt.text(40,286,"*per Foolish Baseball",fontsize=6)
    ##Adds distances to each boundary
    plt.text(-200,430,"455",fontsize=10)
    plt.text(160,430,"450",fontsize=10)
    plt.text(35,430,"425",fontsize=10)
    plt.text(-65,430,"425",fontsize=10)
    plt.text(-15,480,"475",fontsize=10)
    plt.text(-235,125,"280",fontsize=10)
    plt.text(185,125,"258",fontsize=10)
    
    ##Titles
    plt.title('The Polo Grounds: 1880-1963', color='Green')
    
    plt.show()  ##Show the image
    return fig.savefig('Polo_Grounds.png', dpi=300) ##Save the image