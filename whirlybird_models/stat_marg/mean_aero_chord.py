from openmdao.api import ExplicitComponent

import numpy as np 

class MeanAeroChord(ExplicitComponent):
    def setup(self):
        self.add_input('cr')
        self.add_input('lamda')
        self.add_output('C_bar')
        self.declare_partials('C_bar', 'cr', method = 'fd')
        self.declare_partials('C_bar', 'lamda', method = 'fd')

    def compute(self, inputs, outputs):
        cr = inputs['cr']
        lamda = inputs['lamda']
        outputs['C_bar'] = (2./3.)*cr*((1.+lamda+(lamda**2.))/(1.+lamda))    