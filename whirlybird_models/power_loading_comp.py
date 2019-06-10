from openmdao.api import ExplicitComponent


# power loading component for the propeller driven airplane
# the ratio of the 0.3 (in metric units of Watt/gram ) for the typical twin engine, general aviation from Raymer's textbook
# this equation was found from empirical data from historical UAV trends
A = 0.048
C = 0.32
q = (745.7/453.592) # conversion factor from mph to m/s
class PowerLoadingComp(ExplicitComponent):

    def setup(self):
        self.add_input('V_max', val = 28.7) # 'the units ar in mph, the original unit choice for this was 23.0 m/s
        self.add_output('P_W0', val = 0.3)
        self.declare_partials('P_W0', 'V_max'), 'Initial gross weight is not used in this'
        # Wing Loading: W/S = 25 = 30 kg/m^2 . Power loading is determined by the two UAV's that have been looked at. The 'Finder' and Lockheed's FARKASS(?)

    def compute(self, inputs, outputs):
        V_max = inputs['V_max']
        outputs['P_W0'] = A * V_max ** C # ' be warned that  the units for this is in imperial units hp/lb '
    
    def compute_partials(self, inputs, partials):
        V_max = inputs['V_max']
        partials['P_W0', 'V_max'] = C * A * V_max **(C-1)

