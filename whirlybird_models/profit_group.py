from openmdao.api import Group, IndepVarComp

from opto_comps.deliveries_per_day_comp import DeliveriesPerDayComp
from opto_comps.total_mass_per_day_comp import TotalMassPerDayComp
from opto_comps.profit_comp import ProfitComp

class ProfitGroup(Group):
    def setup(self):
        comp = IndepVarComp()

        comp.add_output('cost_per_kg', val = 5.0) # cost per kg in USD
        comp.add_output('cost_per_day', val = .10) # cost of flight per day USD
        comp.add_output('Lifespan', val = 360.0) # lifespan of Whirlybird
        comp.add_output('d',val = 10000) # delivery distance set by FAA possibly
        comp.add_output('t_op', val =24.0) # 24 hour operation
        comp.add_output('t_charge', val = 2.0) # two hour charge time
        # comp.add_output('')
        
        self.add_subsystem('ivc_comps', comp, promotes=['*'])

        self.add_subsystem('delivery_per_day_comp', DeliveriesPerDayComp(), promotes=['*'])
        self.add_subsystem('total_mass_per_day_comp', TotalMassPerDayComp(), promotes=['*'])
        self.add_subsystem('profit_comp', ProfitComp(), promotes=['*'])

