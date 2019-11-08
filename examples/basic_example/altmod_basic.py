import os
from modeller import *
from modeller.automodel import *

from altmod import Automodel_statistical_potential


example_dirpath = os.path.dirname(__file__)
env = environ()
env.io.atom_files_directory.append(example_dirpath)

# This will build 5 models of the TvLDH protein, including in the MODELLER
# objective function DOPE terms with a weight of 0.5 (the default behaviour of
# the 'Automodel_statistical_potential' class).
a = Automodel_statistical_potential(env,
                                    alnfile=os.path.join(example_dirpath, 'tar_tem_alignment.ali'),
                                    knowns='1bdm', sequence='TvLDH')

# Uncomment the line below to employ a more thorough molecular dynamics refinement phase.
# When coupled with the use of DOPE, this slightly increases 3D modeling quality at
# the expense of an increase in computational times.
# a.md_level = refine.slow

a.starting_model = 1
a.ending_model = 5
a.make()
