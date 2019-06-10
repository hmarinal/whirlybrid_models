from openmdao.api import ExplicitComponent

class RdteFlyCostComp(ExplicitComponent):
    
    def setup(self):
        self.add_input('He')
        self.add_input('Re')
        self.add_input('Ht')
        self.add_input('Rt')
        self.add_input('Hm')
        self.add_input('Rm')
        self.add_input('Hq')
        self.add_input('Rq')
        self.add_input('Cdev')
        self.add_input('Cft')
        self.add_input('Cmat')
        self.add_input('Ceng')
        self.add_input('Neng')
        self.add_input('Cav')
        self.add_output('rdtef')
        self.declare_partials('*','*')

    def compute(self, inputs, outputs):
        He = inputs['He']
        Re = inputs['Re']
        Ht = inputs['Ht']
        Rt = inputs['Rt']
        Hm = inputs['Hm']
        Rm = inputs['Rm']
        Hq = inputs['Hq']
        Rq = inputs['Rq']
        Cdev = inputs['Cdev']
        Cft = inputs['Cft']
        Cmat = inputs['Cmat']
        Ceng = inputs['Ceng']
        Neng = inputs['Neng']
        Cav = inputs['Cav']
        outputs['rdtef'] = He * Re + Ht * Rt + Hm * Rm + Hq * Rq + Cdev + Cft + Cmat + Ceng * Neng + Cav

    def compute_partials(self, inputs, partials):
        He = inputs['He']
        Re = inputs['Re']
        Ht = inputs['Ht']
        Rt = inputs['Rt']
        Hm = inputs['Hm']
        Rm = inputs['Rm']
        Hq = inputs['Hq']
        Rq = inputs['Rq']
        Cdev = inputs['Cdev']
        Cft = inputs['Cft']
        Cmat = inputs['Cmat']
        Ceng = inputs['Ceng']
        Neng = inputs['Neng']
        Cav = inputs['Cav']
        partials['rdtef', 'He'] = Re
        partials['rdtef', 'Re'] = He
        partials['rdtef', 'Ht'] = Rt
        partials['rdtef', 'Rt'] = Ht
        partials['rdtef', 'Hm'] = Rm
        partials['rdtef', 'Rm'] = Hm
        partials['rdtef', 'Hq'] = Rq
        partials['rdtef', 'Rq'] = Hq
        partials['rdtef', 'Cdev'] = 1.0
        partials['rdtef', 'Cft'] = 1.0
        partials['rdtef', 'Cmat'] = 1.0
        partials['rdtef', 'Ceng'] = Neng
        partials['rdtef', 'Neng'] = Ceng
        partials['rdtef', 'Cav'] = 1.0
        
#Qve-onda