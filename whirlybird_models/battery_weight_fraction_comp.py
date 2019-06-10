from openmdao.api import ExplicitComponent

class BatteryWeightFractionComp(ExplicitComponent):
    def setup(self):
        self.add_input('mb',val = 0.48)
        self.add_input('W0', val = 5.0)
        self.add_output('mb/W0')
        self.declare_partials('*','*')

    def compute(self, inputs, outputs):
        mb = inputs['mb']
        W0 = inputs['W0']
        outputs['mb/W0'] = mb/W0
    def compute_partials(self, inputs, partials):
        mb = inputs['mb']
        W0 = inputs['W0']
        partials['mb/W0','mb'] = 1.0/W0
        partials['mb/W0', 'W0'] = - 1.0/( W0 **2) 