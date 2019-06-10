from openmdao.api import ExplicitComponent

import numpy as np 

class ComponXcg(ExplicitComponent):
    def setup(self):
        self.add_input('W_motor')
        self.add_input('Xcg_motor')
        self.add_input('W_prop')
        self.add_input('Xcg_prop')
        self.add_input('W_abox')
        self.add_input('Xcg_abox')
        self.add_input('W_langear')
        self.add_input('Xcg_langear')
        self.add_input('W_spar')
        self.add_input('Xcg_spar')
        self.add_input('W_body')
        self.add_input('Xcg_body')        
        self.add_input('W_payload')
        self.add_input('Xcg_payload')
        self.add_output('Xcg_allminuswing')
        self.declare_partials('*','*',method = 'fd')

        ##self.declare_partials('xcg','xcg_w')
        ## self.declare_partials('Xcg_allminuswing', 'sweep', method ='fd') 

    def compute(self, inputs, outputs):
        W_motor = inputs['W_motor']
        Xcg_motor = inputs['Xcg_motor']
        W_prop = inputs['W_prop']
        Xcg_prop = inputs['Xcg_prop']
        W_abox = inputs['W_abox']
        Xcg_abox = inputs['Xcg_abox']
        W_langear = inputs['W_langear']
        Xcg_langear = inputs['Xcg_langear']
        W_spar = inputs['W_spar']
        Xcg_spar = inputs['Xcg_spar']
        W_body = inputs['W_body']
        Xcg_body= inputs['Xcg_body']
        W_payload= inputs['W_payload']
        Xcg_payload= inputs['Xcg_payload']
       
        outputs['Xcg_allminuswing'] = ((W_motor*Xcg_motor)+(W_prop*Xcg_prop)+(W_abox*Xcg_abox)+\
        (W_langear*Xcg_langear)+(W_spar*Xcg_spar)+(W_body*Xcg_body)+(W_payload*Xcg_payload))\
        /(W_motor+W_prop+W_abox+W_langear+W_spar+W_body+W_payload)