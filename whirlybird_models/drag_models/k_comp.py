from openmdao.api import ExplicitComponent

import numpy as np

class K(ExplicitComponent):
    def setup(self):
        self.add_input('b')
        self.add_input('sweep')
        self.add_input('S')
        self.add_output('K')
        self.declare_partials('*', '*', method = 'fd')


    def compute(self, inputs, outputs):
        b = inputs['b']
        S = inputs['S']
        sweep = inputs['sweep']
        outputs['K'] = 1.0/(np.pi*((4.61*(1-(0.045*(((b**2.0)/S)**0.68)))*(np.cos( sweep * np.pi / 180.0 )**0.15)) - 3.1)*((b**2.0)/S))