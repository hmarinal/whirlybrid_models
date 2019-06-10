from openmdao.api import ExplicitComponent

import numpy as np 

class WingXcg(ExplicitComponent):
    def setup(self):
        self.add_input('sweep')
        self.add_input('xcg_y')        
        self.add_output('Xcg_wing')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        sweep = inputs['sweep']
        xcg_y = inputs['xcg_y']
        outputs['Xcg_wing'] = ( xcg_y*np.tan(sweep * np.pi / 180.0 ) ) + 0.1206   