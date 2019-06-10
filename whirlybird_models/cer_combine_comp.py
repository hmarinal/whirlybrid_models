from openmdao.api import Group, IndepVarComp

from cer_model.engine_hours_comp import EngineHoursComp
from cer_model.tooling_hours_comp import ToolingHoursComp
from cer_model.mfg_hours_comp import MfgHoursComp
from cer_model.quality_hours_comp import QualityHoursComp
from cer_model.devel_support_comp import DevelSupportComp
from cer_model.flight_test_cost_comp import FlightTestCostComp
from cer_model.mfg_material_cost_comp import MfgMaterialCostComp
from cer_model.rdte_fly_cost_comp import RdteFlyCostComp
from cer_model.price_per_unit_comp import PricePerUnitComp
from cer_model.vel_conversion_comp import VelConvComp
# from cer_model.cer_run import 

class CerGroup(Group):
    def setup(self):
        comp = IndepVarComp()
        # comp.add_output('We') # mass kg but will use output We from main code
        # comp.add_output('V') # km/hr
        # comp.add_output('V_max')
        comp.add_output('Q', val=2000.)
        comp.add_output('FTA', val=2.)
        # engineering rates from Raymer's text
        comp.add_output('Re', val=86.0*1.530)
        comp.add_output('Rt', val=88.0*1.530)
        comp.add_output('Rq', val=12.0*1.530)
        comp.add_output('Rm', val=8.0*1.530)
        comp.add_output('Ceng', val=19.99)
        comp.add_output('Neng', val=2.0)
        comp.add_output('Cav', val=95.37)

        # self.connect('V')

        self.add_subsystem('i_comp', comp, promotes=['*'])

        self.add_subsystem('vel_comp', VelConvComp(), promotes=['*'])

        self.add_subsystem('ehc',EngineHoursComp(), promotes=['*'])
        self.add_subsystem('thc',ToolingHoursComp(),promotes=['*'])
        self.add_subsystem('mfg_hc', MfgHoursComp(), promotes=['*'])
        self.add_subsystem('qhc', QualityHoursComp(), promotes=['*'])
        self.add_subsystem('dsc', DevelSupportComp(), promotes=['*'])
        self.add_subsystem('ftc', FlightTestCostComp(), promotes=['*'])
        self.add_subsystem('mfg_mcc', MfgMaterialCostComp(), promotes=['*'])
        self.add_subsystem('rfc', RdteFlyCostComp(), promotes=['*'])
        self.add_subsystem('ppuc', PricePerUnitComp(), promotes=['*'])
        