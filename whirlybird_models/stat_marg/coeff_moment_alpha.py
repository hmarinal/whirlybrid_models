from openmdao.api import ExplicitComponent

import numpy as np 

class CoeffMomentAlpha(ExplicitComponent):
    def setup(self):
        self.add_input('Xcg_tot')
        self.add_input('Xac')
        self.add_input('C_bar')
        self.add_output('Cm_alpha')
        self.declare_partials('Cm_alpha', 'Xcg_tot', method = 'fd')
        self.declare_partials('Cm_alpha', 'Xac', method = 'fd')
        self.declare_partials('Cm_alpha', 'C_bar', method = 'fd')

    def compute(self, inputs, outputs):
        Xcg_tot = inputs['Xcg_tot']
        Xac = inputs['Xac']
        C_bar = inputs['C_bar']
        outputs['Cm_alpha'] = (Xcg_tot -Xac)/C_bar       