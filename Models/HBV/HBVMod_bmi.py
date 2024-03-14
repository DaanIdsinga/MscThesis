## Import the required packages
import numpy as np
from bmipy import Bmi

class BmiHBV(Bmi):
    
    _name = "Semi-distributed HBV"
    _input_var_names = ("Parameters","Precipitation","Evaporation","Canopy Store","Unsaturated Store",
                        "Fast Lateral Store","Saturated Store","Area")
    _output_var_names = ("Canopy Store","Unsaturated Store","Fast Lateral Recharge","Saturated Store",
                         "Modelled Discharge","Precipitation","Evaporation")
    
    def __init__(self):
        #Create a BmiHBV model that is ready for initialization
        self._values = {}
        self._var_units = {}
        
        self._start_time = 0
        self._end_time = np.finfo("d").max
        self._time_units = "h"
        
    def initialize(self, par, forcing, lateral_id=0):
        #Initialize the HBV model
        if lateral_id == 0:
            self.Par = par.Par
        
            self.Si = par.Si
            self.Su = par.Su
            self.Sf = par.Sf
            self.Ss = par.Ss
        
            self.area = par.area
            
            self.Prec = forcing.Prec.values
            self.Evap = forcing.Evap.values
            
        else:
            
            self.lateral_id = lateral_id
        
            self.Par = np.array([par._laterals.Imax[lateral_id],
                                 par._laterals.Ce[lateral_id],
                                 par._laterals.Sumax[lateral_id],
                                 par._laterals.beta[lateral_id],
                                 par._laterals.Pmax[lateral_id],
                                 par._laterals.Tlag[lateral_id],
                                 par._laterals.Kf[lateral_id],
                                 par._laterals.Ks[lateral_id]])
        
            self.Si = par._laterals.Si[lateral_id]
            self.Su = par._laterals.Su[lateral_id]
            self.Sf = par._laterals.Sf[lateral_id]
            self.Ss = par._laterals.Ss[lateral_id]
        
            self.area = par._laterals.area[lateral_id]
            
            self.Prec = forcing.Prec[lateral_id].values
            self.Evap = forcing.Evap.values
                
        self.Qm = 0
        self.Qm_store = np.zeros(int(np.ceil(self.Par[5])))
        
        self.time = self._start_time
        self.time_step = 1
        
        self._values = {"Canopy Store": "Si",
                        "Unsaturated Store": "Su",
                        "Fast Lateral Recharge": "Sf",
                        "Saturated Store": "Ss",
                        "Modelled Discharge": "Qm",
                        "Precipitation": "Prec",
                        "Evaporation": "Evap",
                        "Area": "area",
                        "Parameters": "Par"
                        }
        
        self._var_units = {"Canopy Store": "mm",
                          "Unsaturated Store": "mm",
                          "Fast Lateral Discharge": "mm",
                          "Saturated Store": "mm",
                          "Modelled Discharge": "m3/s",
                          "Precipitation": "mm",
                          "Evaporation": "mm",
                          "Area": "km2"}
        
    def HBVMod(self,Param, Prec, Evap, Si, Su, Sf, Ss, area):
        from Weigfun import Weigfun
        
        #HBVpareto Calculates values of 3 objective functions for HBV model
        Imax=Param[0]
        Ce=Param[1]
        Sumax=Param[2]
        beta=Param[3]
        Pmax=Param[4]
        Tlag=Param[5]
        Kf=Param[6]
        Ks=Param[7]    
        
        Pdt = Prec
        Epdt = Evap
        
        #Interception Reservoir
        if Pdt > 0:
            Si = Si + Pdt
            Pedt = max(0, Si - Imax)
            Si = Si - Pedt
            Eidt = 0
        else:
            #Evaporation only when there is no rainfall
            Pedt = 0
            Eidt = min(Epdt, Si)
            Si = Si - Eidt
                    
        #Unsaturated Reservoir
        if Pedt>0:
            rho = (Su/Sumax)**beta            
            Su = Su + (1-rho)*Pedt
            Qufdt = rho*Pedt
        else:
            Qufdt=0
                    
        #Transpiration
        Epdt = max(0, Epdt - Eidt)
        Eadt = Epdt*(Su/(Sumax*Ce))
        Eadt = min(Eadt, Su)
        Su = Su - Eadt
        
        #Percolation
        Qusdt = (Su/Sumax)*Pmax
        Su = Su - min(Qusdt, Su)
                    
        #Fast Reservoir
        Sf = Sf + Qufdt
        Qfdt = Kf*Sf
        Sf = Sf - min(Qfdt, Sf)
                    
        #Slow Reservoir
        Ss = Ss + Qusdt
        Qsdt = Ks*Ss
        Ss = Ss - min(Qsdt, Ss)
        
        #Total Flow        
        Qtotdt = Qsdt + Qfdt
        
        #Offset Q
        Weigths=Weigfun(Tlag)
        Qm = np.convolve(Qtotdt,Weigths)
        Qm = Qm*area/3.6
        
        return Qm, Si, Su, Sf, Ss
        
    def update(self):
        Qm, self.Si, self.Su, self.Sf, self.Ss = self.HBVMod(
            self.Par,
            self.Prec[self.get_current_time()],
            self.Evap[self.get_current_time()],
            self.Si,
            self.Su,
            self.Sf,
            self.Ss,
            self.area
        )

        Store = self.Qm_store + Qm
        self.Qm = Store[0]
        self.Qm_store = np.zeros(len(Store))
        self.Qm_store[0:len(Store)-1] = Store[1:]
        
        self.time += self.time_step
        
    def update_frac(self, time_frac):
        #Update model by a fraction of a time step
        time_step = self.get_time_step()
        self.time_step = time_frac * time_step
        self.update()
        self.time_step = time_step
    
    def update_until(self, then):
        #Update model until a particular time
        n_steps = (then - self.get_current_time()) / self.get_time_step()
        
        for __ in range(int(n_steps)):
            self.update()
        self.update_frac(n_steps - int(n_steps))
        
    def finalize(self):
        #Finalize model
        self._model = None
        
    def get_var_type(self, var_name):
        #Data type of variable
        return str(self.get_value_ptr(var_name).dtype)
    
    def get_var_units(self, var_name):
        #Get units of variable
        return self._var_units[var_name]
    
    def get_var_nbytes(self, var_name):
        #Get units of variable in bytes
        return self.get_value_ptr(var_name).nbytes
    
    def get_var_itemsize(self, name):
        return np.dtype(self.get_var_type(name)).itemsize
    
    def get_var_location(self, var_name):
        raise NotImplementedError("get_var_location")
    
    def get_var_grid(self, var_name):
        raise NotImplementedError("get_var_grid")
        
    def get_grid_rank(self, grid_id):
        raise NotImplementedError("get_grid_rank")
        
    def get_grid_size(self, grid_id):
        raise NotImplementedError("get_grid_size")
    
    def get_value_ptr(self, var_name):
        #Reference to values
        return getattr(self,self._values[var_name])
    
    def get_value(self, var_name):
        #Copy of values
        return self.get_value_ptr(var_name)
    
    def get_value_at_indices(self, var_name, indices):
        raise NotImplementedError("get_value_at_indices")
    
    def set_value(self, var_name, src):
        setattr(self,self._values[var_name],src)
        
    def set_value_at_indices(self, name, inds, src):
        raise NotImplementedError("set_value_at_indices")
    
    def get_component_name(self):
        #Name of the component
        return self._name

    def get_input_item_count(self):
        #Get names of input variables
        return len(self._input_var_names)

    def get_output_item_count(self):
        #Get names of output variables
        return len(self._output_var_names)

    def get_input_var_names(self):
        #Get names of input variables
        return self._input_var_names

    def get_output_var_names(self):
        #Get names of output variables
        return self._output_var_names
    
    def get_grid_shape(self, grid_id, shape):
        raise NotImplementedError("get_grid_shape")
        
    def get_grid_spacing(self, grid_ids, spacing):
        raise NotImplementedError("get_grid_spacing")
        
    def get_grid_origin(self, grid_id, origin):
        raise NotImplementedError("get_grid_origin")
        
    def get_grid_type(self, grid_id):
        raise NotImplementedError("get_grid_type")
    
    def get_start_time(self):
        #Start time of model
        return self._start_time

    def get_end_time(self):
        #End time of model
        return self._end_time

    def get_current_time(self):
        #Current time of model
        return self.time

    def get_time_step(self):
        #Time step of model
        return self._model.time_step

    def get_time_units(self):
        #Time units of model
        return self._time_units
    
    def get_grid_edge_count(self, grid):
        raise NotImplementedError("get_grid_edge_count")

    def get_grid_edge_nodes(self, grid, edge_nodes):
        raise NotImplementedError("get_grid_edge_nodes")

    def get_grid_face_count(self, grid):
        raise NotImplementedError("get_grid_face_count")

    def get_grid_face_nodes(self, grid, face_nodes):
        raise NotImplementedError("get_grid_face_nodes")
        
    def get_grid_node_count(self, grid):
        raise NotImplementedError("get_grid_size")
    
    def get_grid_nodes_per_face(self, grid, nodes_per_face):
        raise NotImplementedError("get_grid_nodes_per_face")

    def get_grid_face_edges(self, grid, face_edges):
        raise NotImplementedError("get_grid_face_edges")

    def get_grid_x(self, grid, x):
        raise NotImplementedError("get_grid_x")

    def get_grid_y(self, grid, y):
        raise NotImplementedError("get_grid_y")

    def get_grid_z(self, grid, z):
        raise NotImplementedError("get_grid_z")
