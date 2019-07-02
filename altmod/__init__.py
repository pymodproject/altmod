import os
import sys

from modeller import physical, group_restraints, gbsa
from modeller.automodel import automodel


__version__ = 0.1

module_path = sys.modules[__name__].__file__
altmod_dirpath = os.path.dirname(module_path)


class Automodel_statistical_potential(automodel):
    """
    Automodel using statistical potentials.
    """

    def __init__(self, *args, **params):

        automodel.__init__(self, *args, **params)

        # Type of statistical potential to include in the objective function of MODELLER.
        self.statistical_potential = "dope"

        # Weights for the objective function terms.
        self._altmod_w_default = 1.0
        self.altmod_w_sp = 0.5 # Statistical potential terms weight.
        # Homology-derived distance restraints terms.
        self._altmod_w_ca_distance = 1.0
        self._altmod_w_n_o_distance = 1.0
        self._altmod_w_sd_mn_distance = 1.0
        self._altmod_w_sd_sd_distance = 1.0

        # Contact shell values for non-bonded interaction.
        self.sp_contact_shell = 8.00

        # DOPE params path.
        self._dope_params_filepath = '$(LIB)/dist-mf.lib'

        # DFIRE params path.
        self._dfire_params_filepath = os.path.join(altmod_dirpath, "data", "dfire", "dfire_mod.lib")


    def special_patches(self, aln):

        # Sets the weights of the objective function.
        self.env.schedule_scale = physical.values(default=self._altmod_w_default,
                                                  nonbond_spline=self.altmod_w_sp,
                                                  # Distance restraints terms.
                                                  ca_distance=self._altmod_w_ca_distance,
                                                  n_o_distance=self._altmod_w_n_o_distance,
                                                  sd_mn_distance=self._altmod_w_sd_mn_distance,
                                                  sd_sd_distance=self._altmod_w_sd_sd_distance,
                                                  )

        # Allow calculation of statistical (dynamic_modeller) potential.
        edat = self.env.edat
        edat.contact_shell = self.sp_contact_shell
        edat.dynamic_modeller = True


        #--------------------
        # Group restraints. -
        #--------------------

        # Read Fiser/Melo loop modeling potential
        if self.statistical_potential == "fm":
            gprsr = group_restraints(self.env, classes='$(LIB)/atmcls-melo.lib', parameters='$(LIB)/melo1-dist.lib')

        # Read DOPE loop modeling potential (the same one used in assess_dope).
        elif self.statistical_potential == "dope":
            gprsr = group_restraints(self.env, classes='$(LIB)/atmcls-mf.lib', parameters=self._dope_params_filepath)

        # Read DOPE-HR loop modeling potential
        elif self.statistical_potential == "dopehr":
            gprsr = group_restraints(self.env, classes='$(LIB)/atmcls-mf.lib', parameters='$(LIB)/dist-mfhr.lib')

        # DFIRE.
        elif self.statistical_potential == "dfire":
            gprsr = group_restraints(self.env, classes='$(LIB)/atmcls-mf.lib', parameters=self._dfire_params_filepath)

        elif self.statistical_potential == None:
            gprsr = None

        else:
            raise KeyError("Unknown potential: %s." % self.statistical_potential)

        self.group_restraints = gprsr
