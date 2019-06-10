from openmdao.api import ExplicitComponent

L_D = 13.*1.5 # General aviation L/D ratio with a 50 percent incrase in L/D
eta = 0.9
E_mb = 577200.0*0.02 # 'energy density of the battery in joules per mass'
# R = eta*(E/mb)*(L/D)*(mb/W0) 'electric aircaft range equation'
# (mb/W0) does depend on the W0 iteration,  we will include the iterated W0 in our Range model. 

class BatteryRangeComp(ExplicitComponent):
    def setup(self):
        # self.add_input('E/mb', val = 30193.54) # 'double check'
        # self.add_input('L/D', val = 1.5*L_D)
        # self.add_input('eta',)
        self.add_input('mb', val = 0.480) # 0.115 is the mass of the battery
        self.add_input('W0', val = 5.0)
        self.add_input('LD')
        # self.add_input('mb/W0')
        self.add_output('R')
        # self.declare_partials('R','E/mb')
        self.declare_partials('*','*', method = 'fd')
        # self.declare_partials('R','W0')

    def compute(self, inputs, outputs):
        mb_W0 = inputs['mb'] / inputs['W0']
        mb = inputs['mb']
        W0 = inputs['W0']
        L_D = inputs['LD']
        outputs['R'] = eta*L_D* E_mb*mb_W0

    # def compute_partials(self, inputs, partials):
    #     mb = inputs['mb']
    #     W0 = inputs['W0']
    #     L_D = inputs['L_D']
    #     partials['R', 'W0'] = - eta*L_D*E_mb*mb / (W0)**2

