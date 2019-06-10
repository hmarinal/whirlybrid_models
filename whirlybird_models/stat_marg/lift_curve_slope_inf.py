from openmdao.api import ExplicitComponent
import numpy as np
#' lift curve slope component of static margin model
# ' 5.605 Kg' for the initial gross weight
class LiftCurveInf(ExplicitComponent):
    def setup(self):
        self.add_input('sweep')
        # self.add_input('t/c', val = .12)
        self.add_output('Cl_alpha_inf')  
        self.declare_partials('Cl_alpha_inf', 'sweep', method = 'fd')

    def compute(self, inputs, outputs):
        sweep = inputs['sweep']
        outputs['Cl_alpha_inf'] = 1.8 * np.pi * ( 1+ 0.8 * .12) * np.cos( (sweep * np.pi/180.0) ) -1.0 #'double check'
