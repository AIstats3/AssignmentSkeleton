import matplotlib.pyplot as plt
import numpy as np
def Draw():
    fig, ax = plt.subplots() ##Create the axis
    ax.clear() ##Clear any existing images
    ax.axis([-30,30,-10,50]) ##Set axis size
    plt.rcParams['figure.figsize'] = [10, 10]##Make figure square
    ax.axis("off")##Makes axes invisible because who wants to look at those

    court=plt.Rectangle((-25,-6),50,47,fill=False)
    ax.add_patch(court)
    backboard=plt.Rectangle((-3,-2.25),6,0.25,fill=True,color='Red')
    ax.add_patch(backboard)
    rim=plt.Circle((0,0),2,fill=False,lw=2,color='Orange')
    ax.add_patch(rim)
    key=plt.Rectangle((-8,-6),16,19,fill=False)
    ax.add_patch(key)
    inner_key=plt.Rectangle((-6,-6),12,19,fill=False)
    ax.add_patch(inner_key)
    top_of_key=plt.Circle((0,13),6,fill=False)
    ax.add_patch(top_of_key)
    half_court_inner=plt.Circle((0,41),2,fill=False,color='Black')
    ax.add_patch(half_court_inner)
    half_court_outer=plt.Circle((0,41),6,fill=False,color='Black')
    ax.add_patch(half_court_outer)

    ##Adding 3p line
    threeP_L=plt.plot([-22,-22],[-6,9],color='Black',lw=1.5)
    threeP_R=plt.plot([22,22],[-6,9],color='Black',lw=1.5)
    theta=np.linspace(np.pi/8,7*np.pi/8) ##Setting for a bottom open arc
    threeP_radius=23.75
    plt.plot(threeP_radius*np.cos(theta),threeP_radius*np.sin(theta),color='Black')

    ##Adding distance ranges
    epsilon=np.linspace(0,np.pi)
    ##0-3ft range
    plt.plot(3*np.cos(epsilon),3*np.sin(epsilon),color='Black')
    plt.plot([-3,-3],[-6,0],color='Black',lw=1.5)
    plt.plot([3,3],[-6,0],color='Black',lw=1.5)
    ##3-10ft range
    plt.plot(10*np.cos(epsilon),10*np.sin(epsilon),color='Black')
    plt.plot([-10,-10],[-6,0],color='Black',lw=1.5)
    plt.plot([10,10],[-6,0],color='Black',lw=1.5)
    ##10-16ft range
    plt.plot(16*np.cos(epsilon),16*np.sin(epsilon),color='Black')
    plt.plot([-16,-16],[-6,0],color='Black',lw=1.5)
    plt.plot([16,16],[-6,0],color='Black',lw=1.5)
    ##16-3pft range and 3p range are defined by the three point line

    return plt.show()