from openmdao.api import ExplicitComponent

class WingLoadingComp(ExplicitComponent):
    def setup(self):
        self.add_input('W_S', val = 30.0)
        self.add_input('W0')
        self.add_output('S')
        self.declare_partials('S','W0')

    def compute(self, inputs, outputs):
        W_S = inputs['W_S']
        W0 = inputs['W0']
        outputs['S'] = W0 / (W_S)
    def compute_partials(self, inputs, partials):
        W_S = inputs['W_S']
        W0 = inputs['W0']
        partials['S','W0'] = 1.0/(W_S)

