from openmdao.api import ExplicitComponent

class FlightTestCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('We')
        self.add_input('V')
        self.add_input('FTA')
        self.add_output('Cft')
        self.declare_partials('*','*')
    
    def compute(self, inputs, outputs):
        We = inputs['We']
        V = inputs['V']
        FTA = inputs['FTA']
        coef = 1408
        a = 0.325
        b = 0.822
        c = 1.210
        d = 1.530
        outputs['Cft'] = (d*coef) * (We**(a)) * (V**(b)) * (FTA**(c))

    def compute_partials(self, inputs, partials):
        We = inputs['We']
        V = inputs['V']
        FTA = inputs['FTA']
        coef = 1408
        a = 0.325
        b = 0.822
        c = 1.210
        d = 1.530
        partials['Cft','We'] = (d*coef*a) * (1.0/(We**(1.0-a))) * (V**(b)) * (FTA**(c))
        partials['Cft','V'] = (d*coef*b) * (We**(a)) * (1.0/(V**(1.0-b))) * (FTA**(c))
        partials['Cft','FTA'] = (d*coef*c) * (We**(a)) * (V**(b)) * (1.0/(FTA**(1.0-c)))

#Qve-onda