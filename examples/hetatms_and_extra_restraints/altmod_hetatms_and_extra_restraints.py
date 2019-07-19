# Use altMOD to model a protein with HETATM residues and with additional user-defined
# restraints (and special patches).
# Adapted from: https://salilab.org/modeller/manual/node18.html
#               https://salilab.org/modeller/manual/node24.html
#               https://salilab.org/modeller/manual/node28.html

from modeller import *
from modeller.automodel import *
from altmod import Automodel_statistical_potential

log.verbose()
env = environ()

# To use HETATMs, simply set the hetatm flag on.
env.io.hetatm = True


class MyModel_statistical_potential(Automodel_statistical_potential):
    """
    To use the 'Automodel_statistical_potential' with custom restraints, we need to write a child class
    of 'Automodel_statistical_potential' and define additional restraints just like we do when using
    child classes of 'automodel' (see https://salilab.org/modeller/manual/node28.html).
    """

    def special_restraints(self, aln):
        """
        If we define additional restraints in the 'special_restraints' method, this will not interfere
        with the 'Automodel_statistical_potential' class behaviour. Therefore we may proceed exactly like
        we do with 'automodel' child classes.
        """

        rsr = self.restraints
        at = self.atoms

        # Residues 20 through 30 are forced to be in an alpha helix conformation.
        rsr.add(secondary_structure.alpha(self.residue_range('20:', '30:')))

        # Restrain a CA-CA distance to 10 angstroms (st. dev.=0.1),
        # with a harmonic potential and X-Y distance group.
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CA:35'], at['CA:40']),
                               mean=10.0, stdev=0.1))


    def special_patches(self, aln):
        """
        If we decide to override the 'special_patches' method (for example, in order to add a disulfide
        bridge in our model), we must remember to call the 'special_patches' method from the
        'Automodel_statistical_potential' class, where the statistical potential terms are included in
        the objective function.
        """

        # Call this in order to activate statistical potential terms.
        Automodel_statistical_potential.special_patches(self, aln)

        # A disulfide between residues 8 and 45.
        self.patch(residue_type='DISU', residues=(self.residues['8'],
                                                  self.residues['45']))


# Actually builds the models.
a = MyModel_statistical_potential(env,
                                  alnfile='tar_tem_alignment.ali',
                                  knowns='5fd1',
                                  sequence='1fdx')
a.starting_model = 1
a.ending_model = 5

a.make()
