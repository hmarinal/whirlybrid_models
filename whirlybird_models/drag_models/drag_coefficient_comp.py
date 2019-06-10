from openmdao.api import ExplicitComponent

class Cd(ExplicitComponent):
    def setup(self):
        self.add_input('Dq', val = 0.0)
        # self.add_input('Dq', val = 0.0278709)
        self.add_input('Cd0_23', val = 0.007380519577681) #for version 1
        # self.add_input('Cd0_23', val = 0.0189) # for version 2
        self.add_input('cd0')
        self.add_input('S')
        self.add_output('Cd')
        self.declare_partials('*', '*', method = 'fd')


    def compute(self, inputs, outputs):
        Dq = inputs['Dq']
        Cd0_23 = inputs['Cd0_23']
        S = inputs['S']
        cd0 = inputs['cd0']
        
        outputs['Cd'] = (cd0 + Cd0_23 + Dq)/(4.0*S)