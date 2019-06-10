from openmdao.api import Group, IndepVarComp

from stat_marg.lift_curve_slope_inf import LiftCurveInf
from stat_marg.lift_curve_slope_comp import LiftCurveComp
from stat_marg.compon_xcg import ComponXcg
from stat_marg.wing_xcg import WingXcg
from stat_marg.total_xcg import TotalXcg
from stat_marg.wing_xac import WingXac
from stat_marg.neutral_point import NeutralPoint # it is the neutral point
from stat_marg.mean_aero_chord import MeanAeroChord
from stat_marg.coeff_moment_alpha import CoeffMomentAlpha
from stat_marg.stat_marg import StatMarg 

class StatMargGroup(Group):
    def setup(self):
        
        comp = IndepVarComp()
        'this is for the full sized vehicle and the optimized version'
        # comp.add_output('W_motor', val = 0.06)
        # comp.add_output('Xcg_motor', val = .4878)
        # comp.add_output('W_prop', val =0.006)
        # comp.add_output('Xcg_prop', val= .4878)
        # comp.add_output('W_abox', val = 0.74)
        # comp.add_output('Xcg_abox', val = 0.251)
        # comp.add_output('W_langear', val = 0.9)
        # comp.add_output('Xcg_langear', val = 0.351)
        # # comp.add_output('Xcg_langear', val = 0.485)
        # comp.add_output('W_spar', val = 0.06)
        # comp.add_output('Xcg_spar', val = 0.4120)
        # comp.add_output('W_body', val = .35)
        # comp.add_output('Xcg_body', val = 0.4151)
        # comp.add_output('Xcg_payload', val = 0.35)
        # # comp.add_output('Xcg_payload', val = 0.251)
        # comp.add_output('mass_wing', val = 0.447)
        # #for large whirly
        # comp.add_output('xcg_y', val=.395)
        # comp.add_output('xac_y', val=.4286)
        # comp.add_output('mass_allminuswing', val =3.71) 
        ################################################################
        # ' this next one is for a small vehicle, mass properties'
        # comp.add_output('W_motor', val = 0.06)
        # comp.add_output('Xcg_motor', val = .2092)
        # comp.add_output('W_prop', val =0.006)
        # comp.add_output('Xcg_prop', val= .2091)
        # comp.add_output('W_abox', val = 0.74)
        # comp.add_output('Xcg_abox', val = 0.2)
        # comp.add_output('W_langear', val = 0.9)
        # comp.add_output('Xcg_langear', val = 0.23)
        # comp.add_output('W_spar', val = 0.06)
        # comp.add_output('Xcg_spar', val = 0.25)
        # comp.add_output('W_body', val = .35)
        # comp.add_output('Xcg_body', val = 0.24)
        # comp.add_output('Xcg_payload', val = 0.24)
        # comp.add_output('xcg_y', val = 0.1913)
        # comp.add_output('mass_wing', val = 0.124)
        # comp.add_output('mass_allminuswing', val =2.336) 
        # comp.add_output('xac_y', val = .2143)


        ' this next one is for a optimized vehicle, mass properties'
        comp.add_output('W_motor', val = 0.086)
        comp.add_output('Xcg_motor', val = .4878)
        comp.add_output('W_prop', val =0.006)
        comp.add_output('Xcg_prop', val= .4878)
        comp.add_output('W_abox', val = 0.740)
        comp.add_output('Xcg_abox', val = 0.3)
        comp.add_output('W_langear', val = 0.9)
        comp.add_output('Xcg_langear', val = 0.2)
        comp.add_output('W_spar', val = 0.06)
        comp.add_output('Xcg_spar', val = 0.412)
        comp.add_output('W_body', val = .350)
        comp.add_output('Xcg_body', val = 0.2)
        comp.add_output('Xcg_payload', val = 0.25)
        comp.add_output('xcg_y', val = 0.1913)
        comp.add_output('mass_wing', val = 0.683)
        comp.add_output('mass_allminuswing', val =3.916) 
        comp.add_output('xac_y', val = .2143)

        
        self.add_subsystem('ivc', comp, promotes=['*'])

        self.add_subsystem('lcs_inf', LiftCurveInf() , promotes=['*'])
        self.add_subsystem('lcs', LiftCurveComp(), promotes=['*'])
        self.add_subsystem('X_cg_component', ComponXcg(), promotes=['*'])
        self.add_subsystem('Wing_xcg', WingXcg() , promotes=['*'])
        self.add_subsystem('total_xcg', TotalXcg(), promotes=['*'])
        self.add_subsystem('Wing_xac', WingXac(), promotes=['*'])
        self.add_subsystem('Neutral_point', NeutralPoint(), promotes=['*'])
        self.add_subsystem('Mean_aero_chord', MeanAeroChord(), promotes=['*'])
        self.add_subsystem('Moment_coefficient_alpha', CoeffMomentAlpha(), promotes=['*'])
        self.add_subsystem('Static_margin', StatMarg(), promotes=['*'])

        