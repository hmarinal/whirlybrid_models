from openmdao.api import ExplicitComponent

class Cd0(ExplicitComponent):
    def setup(self):
        self.add_input('Cf')
        self.add_input('FF')
        self.add_input('Q1', val = 1.4)
        self.add_input('S')
        self.add_output('cd0')
        self.declare_partials('*', '*', method = 'cs')

    def compute(self, inputs, outputs): 
        Cf  = inputs['Cf']
        FF = inputs['FF']
        Q1 = inputs['Q1']
        S = inputs['S']
        outputs['cd0'] = (Cf*FF*Q1*S*4.)