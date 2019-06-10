from openmdao.api import Problem, Group, IndepVarComp, NonlinearBlockGS, LinearBlockGS, ExecComp, ScipyOptimizeDriver
import numpy as np
from empty_weight_fraction_comp import EmptyWeightFractionComp
from gross_weight_comp import GrossWeightComp
from battery_range_comp import BatteryRangeComp
from power_loading_comp import PowerLoadingComp
from wing_loading_comp import WingLoadingComp
from wing_span_comp import WingSpanComp
from root_chord_comp import RootChordComp
from stat_marg_combine import StatMargGroup
from empty_weight_only_comp import EmptyWeightOnlyComp
from cer_combine_comp import CerGroup
# from drag_models import DragGroup
from drag_combine_comp import DragGroup
from new_gross_weight_comp import NewGrossWeightComp

from profit_group import ProfitGroup

prob = Problem()

group = Group()

comp = IndepVarComp()
' this is for version 1 of the whirlybird'
# comp.add_output('Wp', val=2.26) # weight is in kg
# comp.add_output('Wc', val=0.) # Crew weight, none
# comp.add_output('mb', val = 0.48) # mass of the battery
# comp.add_output('V_max', val= 28.7)
# comp.add_output('W_S', val = 16.0) # wing loading 16 kg/m**2 
# comp.add_output('lamda', val = 0.4) # this is the taper ratio
# comp.add_output('AR', val = 6.998) # this is the taper ratio
# comp.add_output('sweep', val = 35.0) # sweep from the LE
# comp.add_output('num_of_WB', val = 10)
'this is one is for version 2 of the whirlybird'
# comp.add_output('Wp', val=1.0) # weight is in kg 
# comp.add_output('Wc', val=0.) # Crew weight, none
# comp.add_output('mb', val = 0.48) # mass of the battery
# comp.add_output('V_max', val= 28.7)
# comp.add_output('W_S', val = 30.0) # wing loading 30 kg/m**2 selected by the FINDER UAV system 
# comp.add_output('lamda', val = 0.4) # this is the taper ratio
# comp.add_output('AR', val = 6.0) # this is the aspect ratio
# comp.add_output('sweep', val = 30.0) # sweep from the LE
# comp.add_output('num_of_WB', val = 10) # number of whirlybirds in a fleet for a day

'this one is for optimization and all of these are chosen as design variables (except for sweep)'
comp.add_output('Wp') # weight is in kg 
comp.add_output('Wc', val=0.) # Crew weight, none
comp.add_output('mb') # mass of the battery
comp.add_output('V_max')
comp.add_output('W_S', val = 10.0) # wing loading 10 kg/m**2
comp.add_output('lamda', val = 0.4) # this is the taper ratio
comp.add_output('AR', val = 10.) # this is the taper ratio
comp.add_output('sweep', val = 35.0) # sweep w.r.t. LE
comp.add_output('num_of_WB', val =10.0) # number of whirlybirds in a fleet for a day


group.add_subsystem('ivc', comp)

comp = EmptyWeightFractionComp()
group.add_subsystem('ewf', comp)

comp = GrossWeightComp()
group.add_subsystem('gwe', comp)

comp = NewGrossWeightComp()
group.add_subsystem('gw', comp)
group.connect('ivc.mb', 'gw.mb')
group.connect('gwe.W0_','gw.W0_')

comp = BatteryRangeComp() # 'electric battery range'
group.add_subsystem('r', comp)

comp = PowerLoadingComp()
group.add_subsystem('pw0', comp)

comp = WingLoadingComp()
group.add_subsystem('s', comp)

comp = WingSpanComp()
group.add_subsystem('ws', comp)

comp = RootChordComp()
group.add_subsystem('rc', comp)

# Empty Weight Comp for use in the cost model
comp = EmptyWeightOnlyComp()
group.add_subsystem('ew_only', comp)

group.connect('ewf.We/W0','ew_only.We/W0')
group.connect('gw.W0','ew_only.W0')


# Cost Model
comp = CerGroup()
group.add_subsystem('cer_g', comp)

group.connect('ew_only.We','cer_g.We')
# group.connect('ivc.V_max','cer_g.V_max')

# Profit Model

comp = ProfitGroup()
group.add_subsystem('pg', comp)
group.connect('ivc.V_max','pg.V_max')
group.connect('ivc.Wp','pg.Wp')
group.connect('ivc.num_of_WB','pg.num_of_WB')
group.connect('cer_g.U_P','pg.U_P')


group.connect('ivc.Wp', 'gwe.Wp')
group.connect('ivc.Wc', 'gwe.Wc')
group.connect('gwe.W0_', 'ewf.W0_')
group.connect('gw.W0', 's.W0')

group.connect('ewf.We/W0', 'gwe.We/W0')
group.connect('gw.W0', 'r.W0')
group.connect('ivc.mb', 'r.mb')

group.connect('ivc.V_max','pw0.V_max')
group.connect('ivc.W_S','s.W_S')

group.connect('s.S','ws.S')
group.connect('ivc.AR', 'ws.AR')


# group for  root chord
group.connect('ivc.lamda','rc.lamda')
group.connect('ws.b','rc.b')
group.connect('s.S','rc.S')

comp = StatMargGroup()
group.add_subsystem('static_margin', comp)

group.connect('ivc.sweep', 'static_margin.sweep')
# group.connect('ivc.Wp','static_margin.Wp')
group.connect('ws.b','static_margin.b')
group.connect('s.S','static_margin.S')
group.connect('ivc.Wp','static_margin.W_payload')
group.connect('ivc.lamda','static_margin.lamda')
group.connect('rc.cr','static_margin.cr')
# group.connect('static_margin.Xac','static_margin.Xac_wing')
# Drag model

comp = DragGroup()
group.add_subsystem('drag_g', comp)

group.connect('ivc.sweep','drag_g.sweep')
group.connect('s.S','drag_g.S')
group.connect('ws.b','drag_g.b') # connects wing span output b to drag group's b
group.connect('ivc.V_max','drag_g.V_max')
group.connect('static_margin.C_bar', 'drag_g.C_bar')
group.connect('drag_g.LD','r.LD')
group.connect('ivc.V_max','cer_g.V_max')

group.nonlinear_solver = NonlinearBlockGS(iprint=2, maxiter=200)

group.linear_solver = LinearBlockGS(iprint = 2, maxiter=100)


prob.model = group

# The optimizer below will attempt to optimize profit with design variables mb, Wp, V_max, and WB (number of whirlybirds) 

# cost_per_kg = $5.0 'USD'
# cost_per_use = $0.10 ' number of USD needed to maintain the whirlybird' # may capture use charge time cost, maintainance,
#  and operatinoal cost
# lifespan = 1200 'flight hours'
# obj = ( tm_day * cost_per_kg ) * lifespan - ( init_build_cost + cost_per_day ) * lifespan

# These are the design variables
prob.model.add_design_var('ivc.mb', lower=0.1, upper=10.0)              # Mass of the battery
prob.model.add_design_var('ivc.Wp', lower = 2.26, upper = 4.0)          # Payload mass
prob.model.add_design_var('ivc.num_of_WB', lower=1.0, upper = 2000.0)   # Number of whirlybirds
prob.model.add_design_var('ivc.V_max', lower=23.0, upper = 35.0)        # Airspeed, max case
prob.model.add_design_var('ivc.AR', lower = 5.0, upper = 10.0)          # aspec ratio
prob.model.add_design_var('ivc.lamda', lower = 0.35, upper = 0.8)       # taper ratio
prob.model.add_design_var('cer_g.Q', lower = 500.0, upper = 5000.00)    # Quantity to be produced
prob.model.add_design_var('ivc.W_S', lower =  10.0, upper = 30.0)       # Wing Loading, likely to choose smaller due to UAV size


# constraints
# the three experiments are conducted by seting constraints on the range of the Whirlybird
# Case 1 is set at 30 km 
# Case 2 is set at 20 km
# Case 3 is set at 10 km

prob.model.add_constraint('pg.Wp_mass_day', lower = 0.1, upper = 2000.0) # max allowable payload mass per day to deliver
prob.model.add_constraint('r.R', equals = 30000.0) # case 1 for optimization
# prob.model.add_constraint('r.R', equals = 20000.0) # case 2 for optimization
# prob.model.add_constraint('r.R', equals = 10000.0) # case 3 for optimization
prob.model.add_constraint('ws.b', lower = 0.5, upper = 10.0)
# prob.model.add_constraint('gw.W0', lower = 2.0, upper = 5.5)

# another set of constraints that would be interesting to see....

# prob.model.add_constraint('pg.profit', equals=0.0)....
#


# one thing to note form our simulations, it is favorable to use the Wp as a constriant rather than a design varible since the
# optimizer tends to choose the smallest payload (Wp) to satisfy the unit reduction cost. 
# Also it tends to stick to the samllest allowable airspeed and payload weight when optimizing for cost reduction
# 

# prob.model.add_constraint('drag_g.R', lower = None, upper = 500000.0), attempt to stay within laminar boundry layer?
# drag_g.R is the Drag Group's Reynold's component

# prob.model.add_subsystem('objective', 
#     ExecComp('obj = profit', scaler = -1.0), 
#         promotes=['*'])

# prob.model.add_objective('pg.profit', scaler=-1.0), FAILED to Optimize for profit, :/
prob.model.add_objective('cer_g.U_P', scaler = 1.0) # this worked pretty well and still managed to make profit.

prob.driver = ScipyOptimizeDriver()
prob.driver.options['optimizer'] = 'SLSQP'



prob.setup()
# prob.run_model()
prob.run_driver()
prob.model.list_outputs()

# TO RUN: 'python run.py'
# TO VISUALIZE: 'openmdao view_model run.py'
