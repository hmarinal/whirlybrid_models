from openmdao.api import ExplicitComponent
import numpy as np
#' lift curve slope component of static margin model
# ' 5.605 Kg' for the initial gross weight
class LiftCurveComp(ExplicitComponent):
    def setup(self):
        #self.add_input('sweep')
        # self.add_input('t/c', val = .12)
        self.add_input('b',)
        self.add_input('S',)
        self.add_input('Cl_alpha_inf')
        self.add_output('Cl_alpha')
        # self.declare_partials('Cl_alpha', 'sweep', method ='fd')
        self.declare_partials('Cl_alpha', 'b', method = 'fd')
        self.declare_partials('Cl_alpha', 'S', method = 'fd')
        self.declare_partials('Cl_alpha', 'Cl_alpha_inf', method = 'fd')

    
    def compute(self, inputs, outputs):
        #sweep = inputs['sweep']
        b = inputs['b']
        S = inputs['S']
        Cl_alpha_inf = inputs['Cl_alpha_inf']
        # Cl_alpha_inf = outputs['Cl_alpha_inf']
        outputs['Cl_alpha'] = Cl_alpha_inf * ( 1 + (Cl_alpha_inf / (np.pi * (b**2 / S) ) ) )
        #  'Double check this !!! '

