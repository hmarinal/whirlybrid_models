from openmdao.api import ExplicitComponent

class EngineHoursComp(ExplicitComponent):

    def setup(self):
        self.add_input('We')
        self.add_input('V')
        self.add_input('Q')
        self.add_output('He')
        self.declare_partials('*','*')
    
    def compute(self, inputs, outputs):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 5.18
        a = 0.777
        b = 0.894
        c = 0.163
        outputs['He'] = (coef) * (We**(a)) * (V**(b)) * (Q**(c))

    def compute_partials(self, inputs, partials):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 5.18
        a = 0.777
        b = 0.894
        c = 0.163
        partials['He','We'] = (coef*a) * (1.0/(We**(1.0-a))) * (V**(b)) * (Q**(c))
        partials['He','V'] = (coef*b) * (We**(a)) * (1.0/(V**(1.0-b))) * (Q**(c))
        partials['He','Q'] = (coef*c) * (We**(a)) * (V**(b)) * (1.0/(Q**(1.0-c)))

#Qve-onda