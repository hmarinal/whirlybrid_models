from openmdao.api import ExplicitComponent


class DragModelComp(ExplicitComponent):

    def setup(self): 
        self.add_input('K')
        self.add_input('Cd')
        self.add_input('Cl', val = 0.7)
        self.add_output('Cd_total')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
       K = inputs['K']
       Cd = inputs['Cd']
       Cl = inputs['Cl']
       outputs['Cd_total'] = Cd +(K*(Cl**2.0))


