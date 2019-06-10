from openmdao.api import ExplicitComponent


class GrossWeightComp(ExplicitComponent):

    def setup(self):
        self.add_input('Wp')
        self.add_input('Wc')
        # self.add_inputs('mb')
        self.add_input('We/W0', val=0.5)
        # self.add_input('mb')
        # self.add_input('mb/W0', val = 0.1)
        self.add_output('W0_', val=5.0)
        self.declare_partials('*', '*', method ='fd')

    def compute(self, inputs, outputs):
        Wp = inputs['Wp']
        Wc = inputs['Wc']
        # mb = inputs['mb']
        # mb_W0 = inputs['mb/W0']
        We_W0 = inputs['We/W0']
        # outputs['W0'] = (Wp + Wc) / (1 - We_W0 - mb_W0)

        outputs['W0_'] = (Wp + Wc) / (1 - We_W0 )
        # mb_W0 = inputs['mb'] / inputs['W0']

    # def compute_partials(self, inputs, partials):
    #     Wp = inputs['Wp']
    #     Wc = inputs['Wc']
    #     # mb_W0 = inputs['mb'] / inputs['W0']
    #     We_W0 = inputs['We/W0']
    #     partials['W0', 'Wp'] = 1. / (1 - We_W0 )
    #     partials['W0', 'Wc'] = 1. / (1 - We_W0 )
    #     partials['W0', 'We/W0'] = (Wp + Wc) / (1 - We_W0 ) ** 2
