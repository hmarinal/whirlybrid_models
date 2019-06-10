from openmdao.api import ExplicitComponent

class PricePerUnitComp(ExplicitComponent):
    def setup(self):
        self.add_input('rdtef')
        self.add_input('Q')
        self.add_output('U_P')
        self.declare_partials('*','*', method = 'fd')

    def compute(self, inputs, outputs):
        rdte = inputs['rdtef']
        Q = inputs['Q']
        outputs['U_P'] = rdte / Q 