from openmdao.api import ExplicitComponent

class QualityHoursComp(ExplicitComponent):

    def setup(self):
        self.add_input('Hm')
        self.add_output('Hq')
        self.declare_partials('*','*')

    def compute(self, inputs, outputs):
        Hm = inputs['Hm']
        coef = 0.133
        outputs['Hq'] = coef * Hm

    def compute_partials(self, inputs, partials):
        Hm = inputs['Hm']
        coef = 0.133
        partials['Hq','Hm'] = coef

#Qve-onda