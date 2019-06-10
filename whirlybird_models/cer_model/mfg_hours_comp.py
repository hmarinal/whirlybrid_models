from openmdao.api import ExplicitComponent

class MfgHoursComp(ExplicitComponent):

    def setup(self):
        self.add_input('We')
        self.add_input('V')
        self.add_input('Q')
        self.add_output('Hm')
        self.declare_partials('*','*')
    
    def compute(self, inputs, outputs):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 10.5
        a = 0.820
        b = 0.484
        c = 0.641
        outputs['Hm'] = (coef) * (We**(a)) * (V**(b)) * (Q**(c))

    def compute_partials(self, inputs, partials):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 10.5
        a = 0.820
        b = 0.484
        c = 0.641
        partials['Hm','We'] = (coef*a) * (1.0/(We**(1.0-a))) * (V**(b)) * (Q**(c))
        partials['Hm','V'] = (coef*b) * (We**(a)) * (1.0/(V**(1.0-b))) * (Q**(c))
        partials['Hm','Q'] = (coef*c) * (We**(a)) * (V**(b)) * (1.0/(Q**(1.0-c)))

#Qve-onda