import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

class Calperiod_plot(object):
    
    def __init__(self,cal,run,calperiod,subcatchment):
        
        index = cal.C[:,10].argmin()        
        
        plt.figure(figsize=(12,6))
        plt.plot(run.Q['Qobs'],label='Observed')
        plt.plot(run.Q['Qmod'],label='Modelled')
        plt.axvline(datetime.strptime(calperiod[1], '%Y-%m-%d %H:%M:%S'),color='red',label='Start calibration')
        plt.xlabel('Time')
        plt.ylabel('Discharge [$m^3/s$]')
        plt.title(f"{subcatchment}, Calibration NSE = {round(cal.C[index,8],3)}")
        plt.legend()
        plt.savefig(f'Calperiod_plot_{subcatchment}.png');
        
class Cal_plot(object):
    
    def __init__(self,cal,run,calperiod,subcatchment):
        
        index = cal.C[:,10].argmin()
        
        plt.figure(figsize=(12,6))
        plt.plot(run.Q['Qobs'][calperiod[1]:calperiod[2]],label='Observed')
        plt.plot(run.Q['Qmod'][calperiod[1]:calperiod[2]],label='Modelled')
        plt.xlabel('Time')
        plt.ylabel('Discharge [$m^3/s$]')
        plt.title(f'{subcatchment}, Calibration NSE = {round(cal.C[index,8],3)}')
        plt.legend()
        plt.savefig(f'Cal_plot_{subcatchment}.png');
        
class Cum_cal_plot(object):
    
    def __init__(self,cal,run,calperiod,subcatchment):
        
        index = cal.C[:,10].argmin()
        
        cum_disch = pd.DataFrame()
        cum_disch['Observed'] = run.Q['Qobs'][calperiod[1]:calperiod[2]]
        cum_disch['Modelled'] = run.Q['Qmod'][calperiod[1]:calperiod[2]]
        
        cum_disch.cumsum().plot(figsize=(12,6))
        plt.title(f'{subcatchment}, Calibration NSE = {round(cal.C[index,9],3)}')
        plt.xlabel('Time')
        plt.ylabel('Cumulative Discharge [$m^3/s$]')
        plt.savefig(f'Cum_cal_plot_{subcatchment}.png');
        
class Dotty_plot(object):
    
    def __init__(self,cal,run,calperiod,subcatchment):
        
        Obj = cal.C[:,8]
        Obj_sum = cal.C[:,9]
        De = cal.C[:,10]
        
        plt.figure()
        plt.plot(Obj_sum,Obj,'.')
        plt.xlabel('NSE Cumulative Discharge')
        plt.ylabel('NSE Q')
        plt.title(f'{subcatchment} NSE')
        plt.savefig(f'{subcatchment} NSE')
        
        variables = ['Imax', 'Ce', 'Su,max', 'Beta', 'Pmax', 'Tlag', 'Kf', 'Ks']
        objectives = [Obj, Obj_sum, De]
        objectives_title = ['Q', 'Cum Q', 'De']
        
        for j in range(len(objectives)):
            plt.figure(figsize=(8, 8))
            plt.suptitle(f"{objectives_title[j]}", y=0.975, fontsize=14, va='center')

            for i, var in enumerate(variables, start=1):
                plt.subplot(4, 2, i)
                plt.plot(cal.C[:, i-1], objectives[j], '.')
                plt.xlabel(var)
                if objectives_title[j] == 'De':
                    if i in (1, 3, 5, 7):  # Add y-label only for odd subplots
                        plt.ylabel('DE(-)')
                        plt.xlim(cal.C[:, i-1].min(), cal.C[:, i-1].max())
                else:
                    if i in (1, 3, 5, 7):  # Add y-label only for odd subplots
                        plt.ylabel('NSE(-)')
                        plt.xlim(cal.C[:, i-1].min(), cal.C[:, i-1].max())

            plt.tight_layout()
            plt.savefig(f'{objectives_title[j]}_{subcatchment}.png')
            plt.show()
            
class Valperiod_plot(object):
    
    def __init__(self,Validation,valperiod,subcatchment):
        
        NSE = Validation.Obj
        
        plt.figure(figsize=(12,6))
        plt.plot(Validation.Q['Qobs'],label='Observed')
        plt.plot(Validation.Q['Qmod'],label='Modelled')
        plt.axvline(datetime.strptime(valperiod[1], '%Y-%m-%d %H:%M:%S'),color='red',label='Start validation')
        plt.xlabel('Time')
        plt.ylabel('Discharge [$m^3/s$]')
        plt.title(f'{subcatchment}, Validation NSE = {round(NSE,3)}')
        plt.legend()
        plt.savefig(f'Valperiod_plot_{subcatchment}.png');
        
class Val_plot(object):
    
    def __init__(self,Validation,valperiod,subcatchment):
        
        NSE = Validation.Obj
        
        plt.figure(figsize=(12,6))
        plt.plot(Validation.Q['Qobs'][valperiod[1]:valperiod[2]],label='Observed')
        plt.plot(Validation.Q['Qmod'][valperiod[1]:valperiod[2]],label='Modelled')
        plt.xlabel('Time')
        plt.ylabel('Discharge [$m^3/s$]')
        plt.title(f'{subcatchment}, Validation NSE = {round(NSE,3)}')
        plt.legend()
        plt.savefig(f'Val_plot_{subcatchment}.png');
        
class Cum_val_plot(object):
    
    def __init__(self,Validation,valperiod,subcatchment):
        
        NSE_Cum = Validation.Obj_sum
        
        Validation.Qcum.plot(figsize=(12,6))
        plt.title(f'{subcatchment}, Validation NSE = {round(NSE_Cum,3)}')
        plt.xlabel('Time')
        plt.ylabel('Cumulative Discharge [$m^3/s$]')
        plt.savefig(f'Cum_val_plot_{subcatchment}.png');