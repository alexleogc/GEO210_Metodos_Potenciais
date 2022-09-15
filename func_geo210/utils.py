def curl(F):
    """
    Calcula o rotacional de uma função vetorial

    Ex: 

    F = [(x/(x**2 + y**2)**(1/2)),y/(x**2 + y**2)**(1/2),0]

    fr_x,fr_y,fr_z = curl(F)
    """
    c1 = diff(F[2],y) - diff(F[1],z)
    c2 = diff(F[0],z) - diff(F[2],x)
    c3 = diff(F[1],x) - diff(F[0],y)
    return [c1,c2,c3]

#============================================ Funções de Plotagem ==========================================

def plot_grav_map(X,Y,gz,y_max=None,y_perf=None,x_perf=None,
                  figsize=(12,6),cmap='nipy_spectral',location='bottom',
                 levels=50,perfil='horizontal',cbar_label= r'$g_z$ (mGal)'):
    
    fig, axes= plt.subplots(ncols=2,figsize=figsize)
    
    axes[0].set_aspect('equal')
    
    if perfil=='horizontal':
        axes[0].hlines(y=y_perf,xmin=X.min(),xmax=X.max(),color='white',ls='--',lw=1)
        axes[1].plot(X[Y==y_perf],gz[Y==y_perf],color='black')
        axes[1].set_xlabel('X')
        axes[1].set_ylabel(cbar_label)
    elif perfil=='vertical':
        axes[0].vlines(x=x_perf,ymin=Y.min(),ymax=Y.max(),color='white',ls='--',lw=1)
        axes[1].plot(Y[X==x_perf],gz[X==x_perf],color='black')
        axes[1].set_xlabel('Y')
        axes[1].set_ylabel(cbar_label)
    else:
        pass
    
    axes[0].set_xlim(X.min(),X.max())
    axes[0].set_ylim(Y.min(),Y.max())
    axes[0].set_aspect('equal')

    
    c_bar_ticks = np.linspace(gz.min(),gz.max(),4)
    
    ax = axes[0].contourf(X,Y,gz,cmap=cmap,levels=levels)
    
    cbar = fig.colorbar(ax,ax=axes[0],label=cbar_label,ticks=c_bar_ticks)
    return fig,axes