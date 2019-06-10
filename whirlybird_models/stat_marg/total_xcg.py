from openmdao.api import ExplicitComponent

import numpy as np 

class TotalXcg(ExplicitComponent):
    def setup(self):
        self.add_input('Xcg_wing')
        self.add_input('Xcg_allminuswing')     
        self.add_input('mass_wing')
        self.add_input('mass_allminuswing')   
        self.add_output('Xcg_tot')
        
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        Xcg_wing = inputs['Xcg_wing']
        Xcg_allminuswing = inputs['Xcg_allminuswing']
        mass_wing = inputs['mass_wing']
        mass_allminuswing = inputs['mass_allminuswing']
        outputs['Xcg_tot'] =   (Xcg_wing*mass_wing + Xcg_allminuswing*mass_allminuswing)/(mass_allminuswing+mass_wing)