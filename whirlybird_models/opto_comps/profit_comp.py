from openmdao.api import ExplicitComponent

class ProfitComp(ExplicitComponent):
    def setup(self):
        self.add_input('cost_per_kg', val = 20.0) # cost per kg in USD
        self.add_input('cost_per_day', val = 1.0) # cost of flight per day USD
        self.add_input('Lifespan', val = 365.0) # lifespan in days 
        self.add_input('U_P') # unit cost of whirlybird
        self.add_input('Wp_mass_day') # total mass per day
        self.add_output('profit')
        self.declare_partials('*','*', method='fd')

    def compute(self, inputs, outputs):
        cost_per_kg = inputs['cost_per_kg']
        cost_per_day = inputs['cost_per_day']
        Lifespan = inputs['Lifespan']
        U_P = inputs['U_P']
        Wp_mass_day = inputs['Wp_mass_day']
        outputs['profit'] = Lifespan* ( Wp_mass_day * cost_per_kg - U_P * cost_per_day )



