from openmdao.api import ExplicitComponent
import numpy as np
import math

# The  Total Flight Time Component will be used for the optimization problem
# This component calculates the total time per whirlybird per delivery

class DeliveriesPerDayComp(ExplicitComponent):
    def setup(self):
        self.add_input('V_max')
        self.add_input('d', val = 10000) # assume distance of 10 km from Amazon's Service constraints
        self.add_input('t_charge', val = 2.0) # need justification for the charge time of this battery, 2 hrs from the study Noe did
        self.add_input('t_op', val = 24.0) # 24 hour operation
        # self.add_input('Wp')
        self.add_output('del_day') # 
        self.declare_partials('*','*', method ='fd')
    def compute(self, inputs, outputs):
        V_max = inputs['V_max']
        d = inputs['d']
        t_charge = inputs['t_charge']
        t_op = inputs['t_op']
        # Wp = inputs['Wp']
        outputs['del_day'] = ( (( (2.0 * d / V_max) * (1.0/3600) + t_charge ) ** (-1.0) ) * t_op ) # deliveries per day per whirlybird