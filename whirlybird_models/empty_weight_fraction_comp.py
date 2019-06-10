from openmdao.api import ExplicitComponent

A = .86
C = -0.06

class EmptyWeightFractionComp(ExplicitComponent):

    def setup(self):
        self.add_input('W0_', val=5.00)
        self.add_output('We/W0', val=0.5)
        self.declare_partials('We/W0', 'W0_')

    def compute(self, inputs, outputs):
        outputs['We/W0'] = A * inputs['W0_'] ** C


    def compute_partials(self, inputs, partials):
        partials['We/W0', 'W0_'] = C * A * inputs['W0_'] ** (C - 1)
