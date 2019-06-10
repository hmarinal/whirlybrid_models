from openmdao.api import ExplicitComponent

import numpy as np 

class StatMarg(ExplicitComponent):
    def setup(self):
        self.add_input('Xnp_wing')
        self.add_input('Xcg_tot') 
        self.add_input('C_bar')        
        self.add_output('Stat_marg')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        Xnp_wing = inputs['Xnp_wing']
        Xcg_tot = inputs['Xcg_tot']
        C_bar = inputs['C_bar']
        outputs['Stat_marg'] =  ((Xnp_wing-Xcg_tot))/C_bar
        