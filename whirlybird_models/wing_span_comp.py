from openmdao.api import ExplicitComponent

import numpy as np
import math


class WingSpanComp(ExplicitComponent):
    def setup(self):
        self.add_input('AR')
        self.add_input('S')
        self.add_output('b')
        self.declare_partials('b','AR')
        self.declare_partials('b','S')
    def compute(self, inputs, outputs):

        AR = inputs['AR']
        S = inputs['S']
        outputs['b'] = (AR * S)**0.5
    def compute_partials(self, inputs, partials):
        AR = inputs['AR']
        S = inputs['S']
        partials['b','AR'] = 0.5 * (AR * S) **(-0.5)
        partials['b','S'] = 0.5 * (AR * S) ** (-0.5)
        