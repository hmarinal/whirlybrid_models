from openmdao.api import ExplicitComponent

class ToolingHoursComp(ExplicitComponent):

    def setup(self):
        self.add_input('We')
        self.add_input('V')
        self.add_input('Q')
        self.add_output('Ht')
        self.declare_partials('*','*')
    
    def compute(self, inputs, outputs):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 7.22
        a = 0.777
        b = 0.696
        c = 0.263
        outputs['Ht'] = (coef) * (We**(a)) * (V**(b)) * (Q**(c))

    def compute_partials(self, inputs, partials):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 7.22
        a = 0.777
        b = 0.696
        c = 0.263
        partials['Ht','We'] = (coef*a) * (1.0/(We**(1.0-a))) * (V**(b)) * (Q**(c))
        partials['Ht','V'] = (coef*b) * (We**(a)) * (1.0/(V**(1.0-b))) * (Q**(c))
        partials['Ht','Q'] = (coef*c) * (We**(a)) * (V**(b)) * (1.0/(Q**(1.0-c)))

#Qve-onda