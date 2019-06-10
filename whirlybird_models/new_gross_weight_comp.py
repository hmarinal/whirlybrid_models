from openmdao.api import ExplicitComponent

class NewGrossWeightComp(ExplicitComponent):
    def setup(self):
        self.add_input('W0_')
        self.add_input('mb')
        self.add_output('W0')
        self.declare_partials('*','*', method = 'fd')
    def compute(self, inputs, outputs):
        W0_ = inputs['W0_']
        mb = inputs['mb']
        outputs['W0'] = W0_ + mb