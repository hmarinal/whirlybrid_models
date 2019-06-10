from openmdao.api import ExplicitComponent


class LD(ExplicitComponent):

    def setup(self): 
        self.add_input('Cd_total')
        self.add_input('Cl', val = 0.7)
        self.add_output('LD')
        self.declare_partials('*', '*', method = 'fd')
        
    def compute(self, inputs, outputs):
       Cd_total = inputs['Cd_total']
       Cl = inputs['Cl']
       outputs['LD'] = Cl/Cd_total


