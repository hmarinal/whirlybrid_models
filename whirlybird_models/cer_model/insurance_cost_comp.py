from openmdao.api import ExplicitComponent

class InsuranceCostComp(ExplicitComponent):
    
    def setup(self):
        self.add_input('OM')
        self.add_output('Cins')
        self.declare_partials('*','*')

    def compute(self, inputs, outputs):
        OM = inputs['OM']
        outputs['Cins'] = 0.02*OM

    def compute_partials(self, inputs, partials):
        partials['Cins', 'OM'] = 0.02
