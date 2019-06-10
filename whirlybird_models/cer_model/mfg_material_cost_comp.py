from openmdao.api import ExplicitComponent

class MfgMaterialCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('We')
        self.add_input('V')
        self.add_input('Q')
        self.add_output('Cmat')
        self.declare_partials('*','*')
    
    def compute(self, inputs, outputs):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 22.6
        a = 0.921
        b = 0.621
        c = 0.799
        d = 1.530
        outputs['Cmat'] = (d*coef) * (We**(a)) * (V**(b)) * (Q**(c))

    def compute_partials(self, inputs, partials):
        We = inputs['We']
        V = inputs['V']
        Q = inputs['Q']
        coef = 22.6
        a = 0.921
        b = 0.621
        c = 0.799
        d = 1.530
        partials['Cmat','We'] = (d*coef*a) * (1.0/(We**(1.0-a))) * (V**(b)) * (Q**(c))
        partials['Cmat','V'] = (d*coef*b) * (We**(a)) * (1.0/(V**(1.0-b))) * (Q**(c))
        partials['Cmat','Q'] = (d*coef*c) * (We**(a)) * (V**(b)) * (1.0/(Q**(1.0-c)))

#Qve-onda