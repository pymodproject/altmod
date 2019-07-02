from modeller import *
from modeller.automodel import *

from altmod import Automodel_statistical_potential


env = environ()

# This will build 5 models of the TvLDH protein, including in the MODELLER
# objective function DOPE terms with a weight of 0.5 (the default behaviour of
# the 'Automodel_statistical_potential' class).
a = Automodel_statistical_potential(env, alnfile='tar_tem_alignment.ali',
                                    knowns='1bdm', sequence='TvLDH')
a.starting_model = 1
a.ending_model = 5
a.make()
