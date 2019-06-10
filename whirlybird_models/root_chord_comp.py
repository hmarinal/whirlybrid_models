from openmdao.api import ExplicitComponent

class RootChordComp(ExplicitComponent):
    def setup(self):
        self.add_input('S')
        self.add_input('b')
        self.add_input('lamda')
        self.add_output('cr')
        self.declare_partials('cr', 'S', method = 'fd')
        self.declare_partials('cr', 'b', method = 'fd')
        self.declare_partials('cr', 'lamda', method = 'fd')

    def compute(self, inputs, outputs):
        S = inputs['S']
        b = inputs['b']
        lamda = inputs['lamda']
        outputs['cr'] = 2 * S / (b * (1+lamda))

