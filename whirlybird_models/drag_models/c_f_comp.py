from openmdao.api import ExplicitComponent

import math
class Cf(ExplicitComponent): 

    def setup(self):
        self.add_input('R')
        self.add_input('M', val =0.0676)
        self.add_output('Cf')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        R = inputs['R']
        M = inputs['M']



        # outputs['Cf'] = ((math.log10(R)**(2.58)) * ((1. +  (0.144 * ( M **(2.0) ) ) ) **(0.65)))
        outputs['Cf'] = 1.328/(R ** (0.5))


        # ((math.log10(R)**(2.58)) * ((1. +  (0.144 * ( M **(2.0) ) ) ) **(0.65)))     