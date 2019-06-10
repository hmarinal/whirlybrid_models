from openmdao.api import ExplicitComponent

import numpy as np 

class WingXac(ExplicitComponent):
    def setup(self):
        self.add_input('sweep')
        self.add_input('xac_y')        
        self.add_output('Xac')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        sweep = inputs['sweep']
        xac_y = inputs['xac_y']
        outputs['Xac'] = ( xac_y*np.tan(sweep * np.pi / 180 ) ) + 0.12065      