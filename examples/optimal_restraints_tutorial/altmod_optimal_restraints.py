# In this tutorial we will illustrate how to build an homology model in MODELLER
# using optimal parameters for homology-derived distance restraints (HDDRs).
# Here, we define optimal parameters as the optimal set of sigma values and
# multiple-template weights for each HDDR. The use of optimal HDDR parameters
# greatly increases the quality of 3D models [1].
# However, note that optimal HDDR parameters can only be used when we already know
# the experimentally-determined structure of target protein! Therefore they have
# very little practical utility, but their existance suggests that if we were able
# to estimate them with a certain degree of accuracy, we might improve the 3D
# modeling performance of MODELLER (or similar approaches).

# References:
#     [1] Janson et al. Revisiting the "satisfaction of spatial restraints" approach of MODELLER for protein homology modeling". 2019


from __future__ import print_function
import os
import random
import csv

from modeller import environ, log
from modeller.automodel import automodel
from altmod.automodel_optimal_restraints import Automodel_optimal_restraints


# Initialize the MODELLER environment.
script_dirpath = os.path.dirname(os.path.dirname(__file__))
examples_dirpath = os.path.join(os.path.join(script_dirpath, "basic_example"))
log.none()
env = environ()
env.io.atom_files_directory = [".", examples_dirpath]


# As a first thing, we initialize an automodel object like we usually do in
# MODELLER, except that we will use the 'Automodel_optimal_restraints' class
# imported from the 'altmod' package. Here, we will be modeling a target protein
# (UniProtKB: O96445) with three templates. It's the same protein used in the
# original MODELLER tutorial (https://salilab.org/modeller/tutorial/basic.html).
a = Automodel_optimal_restraints(env,
                                 alnfile=os.path.join(examples_dirpath, 'tar_tem_mt_alignment.ali'),
                                 knowns=('1bdmA', "2mdhA", "1b8pA"),
                                 sequence='TvLDH')

# Luckily, since an experimentally-determined structure of this protein is available
# (PDB code: 4UUM) we can readily extract the theoretically optimal parameters for
# the HDDRs which MODELLER will use to model this target.
# Let's use the 'set_target_structure' to define the path of the target structure.
# Note that since the PDB file of the target has more than one chain, we have
# to specify through the 'target_chain' argument which chain corresponds to our
# target protein.
a.set_target_structure(target_filepath=os.path.join(examples_dirpath, '4uum.pdb'), target_chain="A",)

# We can finally build the models in the traditional way. The 'Automodel_optimal_restraints'
# class will take care of editing the HDDRs lines in the .rsr file of MODELLER with
# the optimal parameters calculated by analysing the structural divergence in each
# restrained distance in each target-template pair.
a.starting_model = 1
a.ending_model = 1
a.make()

# If you take the model built in this way and measure its RMSD with the target
# structure, you will notice a very low value (we get 0.350 A using PyMOL's cealign).
# If your run this script again by using the default 'automodel' class from
# MODELLER and measure the RMSD of the model built with default HDDR parameters,
# you will notice a much higher value (we get 1.458 A).
# Being able to accurately infer near-optimal HDDR parameters would make an
# important difference when applying the MODELLER strategy for homology modeling!
