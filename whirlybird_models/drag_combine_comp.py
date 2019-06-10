from openmdao.api import IndepVarComp, Group

from drag_models.c_f_comp import Cf
from drag_models.drag_coefficient_comp import Cd
from drag_models.drag_coefficient_zero_comp import Cd0
from drag_models.drag_m_comp import DragModelComp
from drag_models.form_factors_comp import FormFactors
from drag_models.k_comp import K
from drag_models.lift_drag_comp import LD
from drag_models.reynolds_comp import Reynolds

class DragGroup(Group):
    def setup(self):
        comp = IndepVarComp()

        comp.add_output('M', val = 0.0676 )
        # comp.add_output('Dq', val = 0.0278709)
        comp.add_output('Dq', val = 0.0)
        comp.add_output('Cd0_23', val = 0.007380519577681)
        comp.add_output('Q1', val = 1.4)
        comp.add_output('Cl', val = 0.7)
        comp.add_output('tc1', val = .12)
        comp.add_output('xc1', val= 0.3)
        # comp.add_output('')
        # comp.add_output('Cd_total')
        comp.add_output('rho', val = 1.225)
        comp.add_output('V', val = 23.0)
        comp.add_output('mu', val = 2.008 * 10**(-5) )

        self.add_subsystem('i_comp', comp, promotes=['*'])

        self.add_subsystem('re', Reynolds(), promotes=['*'])
        self.add_subsystem('cf_comp',Cf(), promotes=['*'])
        # self.add_subsystem('drag_co', Cd(), promotes=['*'])
        self.add_subsystem('k_comp', K(), promotes=['*'])
        self.add_subsystem('ff',FormFactors(),promotes=['*'])

        self.add_subsystem('cd0', Cd0(), promotes=['*'])
        self.add_subsystem('drag_co', Cd(), promotes=['*'])
        self.add_subsystem('drag_m', DragModelComp(), promotes=['*'])
        # self.add_subsystem('ff',FormFactors(),promotes=['*'])
        # self.add_subsystem('k_comp', K(), promotes=['*'])
        self.add_subsystem('lift_drag', LD(), promotes=['*'])
        


