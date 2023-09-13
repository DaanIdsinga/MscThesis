import numpy as np
import matplotlib.pyplot as plt
from Weigfun import Weigfun

def HBVMod(Par,forcing,Sin,hydrograph):
    #HBVpareto Calculates values of 3 objective functions for HBV model

    Imax=Par[0]
    Ce=Par[1]
    Sumax=Par[2]
    beta=Par[3]
    Pmax=Par[4]
    Tlag=Par[5]
    Kf=Par[6]
    Ks=Par[7]    
    
    Qo=forcing[1]
    Prec=forcing[2]
    Etp=forcing[3]
    
    tmax=len(Prec)
    Si=np.zeros(tmax)
    Su=np.zeros(tmax)
    Sf=np.zeros(tmax)
    Ss=np.zeros(tmax) 
    Eidt=np.zeros(tmax)
    Eadt=np.zeros(tmax)
    Qtotdt=np.zeros(tmax)
    
    Si[0]=Sin[0]
    Su[0]=Sin[1]
    Sf[0]=Sin[2]
    Ss[0]=Sin[3]
    
    dt=1

    # Model 1 SOF1
    for i in range(0,tmax):
        Pdt=Prec[i]*dt
        Epdt=Etp[i]*dt
        # Interception Reservoir
        if Pdt>0:
            Si[i]=Si[i]+Pdt
            Pedt=max(0,Si[i]-Imax)
            Si[i]=Si[i]-Pedt
            Eidt[i]=0
        else:
            # Evaporation only when there is no rainfall
            Pedt=0
            Eidt[i]=min(Epdt,Si[i])
            Si[i]=Si[i]-Eidt[i]
                
        if i<tmax-1:
            Si[i+1]=Si[i]       
                
            # Unsaturated Reservoir
        if Pedt>0:
            rho=(Su[i]/Sumax)**beta            
            Su[i]=Su[i]+(1-rho)*Pedt
            Qufdt=rho*Pedt
        else:
            Qufdt=0
                
            # Transpiration
        Epdt=max(0,Epdt-Eidt[i])
        Eadt[i]=Epdt*(Su[i]/(Sumax*Ce))
        Eadt[i]=min(Eadt[i],Su[i])
        Su[i]=Su[i]-Eadt[i]
            # Percolation
        Qusdt=(Su[i]/Sumax)*Pmax*dt
        Su[i]=Su[i]-min(Qusdt,Su[i])
        if i<tmax-1:
            Su[i+1]=Su[i]
                
            # Fast Reservoir
        Sf[i]=Sf[i]+Qufdt
        Qfdt= dt*Kf*Sf[i]
        Sf[i]=Sf[i]-min(Qfdt,Sf[i])
        if i<tmax-1:
            Sf[i+1]=Sf[i]
                
            # Slow Reservoir
        Ss[i]=Ss[i]+Qusdt
        Qsdt= dt*Ks*Ss[i]
        Ss[i]=Ss[i]-min(Qsdt,Ss[i])
        if i<tmax-1:
            Ss[i+1]=Ss[i]
            
        Qtotdt[i]=Qsdt+Qfdt
       
    # Check Water Balance
    Sf=Si[-1]+Ss[-1]+Sf[-1]+Su[-1]
    Sin=sum(Sin)
    WB=sum(Prec)-sum(Eidt)-sum(Eadt)-sum(Qtotdt)-Sf+Sin
    
    # Offset Q
    
    Weigths=Weigfun(Tlag)
    
    Qm = np.convolve(Qtotdt,Weigths)
    Qm=Qm[0:tmax]
    Qm=Qm/3.6*338
 
    # Calculate objective
    ind=np.where(Qo>=0)
    QoAv=np.mean(Qo[ind])
    ErrUp=np.sum((Qo-Qm)**2)
    ErrDo=np.sum((Qo-QoAv)**2)
    Obj=1-(ErrUp/ErrDo)
    
    QoAvlog=np.mean(np.log(Qo[ind]))
    ErrUplog=np.sum((np.log(Qo)-np.log(Qm))**2)
    ErrDolog=np.sum((np.log(Qo)-QoAvlog)**2)
    Objlog=1-(ErrUplog/ErrDolog)
 
    if hydrograph == 'True':
        ## Plot
        # hour=1:tmax\
        plt.plot(forcing[0],Qo,label='Qobs')
        plt.plot(forcing[0],Qm,label='Qmod')
        plt.legend(loc='best')
        plt.show()
    
    return(Obj,Objlog)
