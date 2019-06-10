from openmdao.api import ExplicitComponent


class Reynolds(ExplicitComponent): 

    def setup(self):
        self.add_input('rho', val = 1.225)
        self.add_input('V_max', val = 23)
        self.add_input('mu', 2.008 * 10 **(-5.0) )
        self.add_input('C_bar') # mean aerodynamic chord
        self.add_output('R')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs): 
        rho = inputs['rho']
        V_max = inputs['V_max']
        mu = inputs['mu']
        C_bar = inputs['C_bar']

        outputs['R'] = (rho * V_max * C_bar )/mu