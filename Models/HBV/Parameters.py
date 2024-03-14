class Parameters(object):
    
    def __init__(self, Par, Sin, area):
        
        self._Par = Par
        self._Si = Sin[0]
        self._Su = Sin[1]
        self._Sf = Sin[2]
        self._Ss = Sin[3]
        self._area = area
    
    @property
    def Par(self):
        #Set parameters
        return self._Par
    
    @property
    def Si(self):
        #Set parameters
        return self._Si
    
    @property
    def Su(self):
        #Set parameters
        return self._Su
    
    @property
    def Sf(self):
        #Set parameters
        return self._Sf
    
    @property
    def Ss(self):
        #Set parameters
        return self._Ss
    
    @property
    def area(self):
        #Set parameters
        return self._area