from modeller import *
from modeller.automodel import *

from altmod import Automodel_statistical_potential

env = environ()

# This will build 5 models of the TvLDH protein, including in the MODELLER
# objective function DFIRE terms with a weight of 0.75 and by using a
# contact shell value of 7.5 Angstroms.
a = Automodel_statistical_potential(env, alnfile='tar_tem_alignment.ali',
                                    knowns='1bdm', sequence='TvLDH')
a.starting_model = 1
a.ending_model = 5
a.statistical_potential = "dfire"
a.altmod_w_sp = 0.75
a.sp_contact_shell = 7.5
a.make()
