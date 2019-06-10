from openmdao.api import Problem, Group, IndepVarComp, NonlinearBlockGS

from engine_hours_comp import EngineHoursComp
from tooling_hours_comp import ToolingHoursComp
from mfg_hours_comp import MfgHoursComp
from quality_hours_comp import QualityHoursComp
from devel_support_comp import DevelSupportComp
from flight_test_cost_comp import FlightTestCostComp
from mfg_material_cost_comp import MfgMaterialCostComp
from rdte_fly_cost_comp import RdteFlyCostComp

prob = Problem()

group = Group()

# Adding all of the Explicit components to the main group
comp = IndepVarComp()
comp.add_output('We', val=4.)
comp.add_output('V', val=83.)
comp.add_output('Q', val=500.)
comp.add_output('FTA', val=2.)
comp.add_output('Re', val=86.0*1.530)
comp.add_output('Rt', val=88.0*1.530)
comp.add_output('Rq', val=81.0*1.530)
comp.add_output('Rm', val=73.0*1.530)
comp.add_output('Ceng', val=19.99)
comp.add_output('Neng', val=2.0)
comp.add_output('Cav', val=113.08)
group.add_subsystem('ivc', comp, promotes=['*','*'])


group.add_subsystem('ehc', EngineHoursComp(), promotes=['*','*'])
group.add_subsystem('thc', ToolingHoursComp(), promotes=['*','*'])
group.add_subsystem('mhc', MfgHoursComp(), promotes=['*','*'])
group.add_subsystem('qhc', QualityHoursComp(), promotes=['*','*'])
group.add_subsystem('dsc', DevelSupportComp(), promotes=['*','*'])
group.add_subsystem('ftc', FlightTestCostComp(), promotes=['*','*'])
group.add_subsystem('mmc', MfgMaterialCostComp(), promotes=['*','*'])
group.add_subsystem('rdfc', RdteFlyCostComp(), promotes=['*','*'])



prob.model = group
prob.setup()
prob.run_model()
print(prob['rdtef'])
# prob.check_partials(compact_print=True)

#Qve-onda