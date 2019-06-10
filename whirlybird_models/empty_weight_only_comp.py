from openmdao.api import ExplicitComponent

class EmptyWeightOnlyComp(ExplicitComponent):
    def setup(self):
        self.add_input('We/W0')
        self.add_input('W0')
        self.add_output('We')
        self.declare_partials('We','W0', method = 'fd')
    def compute(self, inputs, outputs):
        We_W0 = inputs['We/W0']
        W0 = inputs['W0']
        outputs['We'] = We_W0 * W0


