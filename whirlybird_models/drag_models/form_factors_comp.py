from openmdao.api import ExplicitComponent

import numpy as np
class FormFactors(ExplicitComponent):
    
    def setup(self):
        self.add_input('tc1')
        self.add_input('xc1')
        self.add_input('M', val = .0676)
        self.add_input('sweep')
        self.add_output('FF')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        tc1 = inputs['tc1']
        xc1 = inputs['xc1']
        M = inputs['M']
        sweep = inputs['sweep']

        outputs['FF'] = ((0.6*tc1/xc1) + (100.0*(tc1**4.0)) + 1.0)*(1.34*(M**(.18)))*(np.cos(sweep * np.pi / 180.0 ) ** (.28))


