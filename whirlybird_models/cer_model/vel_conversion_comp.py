from openmdao.api import ExplicitComponent

class VelConvComp(ExplicitComponent):
    def setup(self):
        self.add_input('V_max')
        self.add_output('V')
        self.declare_partials('*','*', method='fd')

    def compute(self, inputs, outputs):
        V_max = inputs['V_max']
        outputs['V'] = V_max * (3600/1000) # km per hour