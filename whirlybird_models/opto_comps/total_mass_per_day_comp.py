from openmdao.api import ExplicitComponent

class TotalMassPerDayComp(ExplicitComponent):
    def setup(self):
        self.add_input('del_day')
        self.add_input('Wp')
        self.add_input('num_of_WB')
        self.add_output('Wp_mass_day')
        self.declare_partials('*','*', method = 'fd')

    def compute(self, inputs, outputs):
        del_day = inputs['del_day']
        num_of_WB = inputs['num_of_WB']
        Wp = inputs['Wp']
        outputs['Wp_mass_day'] = del_day * num_of_WB * Wp # payload's mass per day 

        