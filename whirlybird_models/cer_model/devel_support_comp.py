from openmdao.api import ExplicitComponent

class DevelSupportComp(ExplicitComponent):

    def setup(self):
        self.add_input('We')
        self.add_input('V')
        self.add_output('Cdev')
        self.declare_partials('*','*')
    
    def compute(self, inputs, outputs):
        We = inputs['We']
        V = inputs['V']
        coef = 48.7
        a = 0.630
        b = 1.300
        d = 1.530
        outputs['Cdev'] = (d*coef) * (We**(a)) * (V**(b)) 

    def compute_partials(self, inputs, partials):
        We = inputs['We']
        V = inputs['V']
        coef = 48.7
        a = 0.630
        b = 1.300
        d = 1.530
        partials['Cdev','We'] = (d*coef*a) * (1.0/(We**(1.0-a))) * (V**(b))
        partials['Cdev','V'] = (d*coef*b) * (We**(a)) * (V**(b-1.0))        
#Qve-onda