import math


# Codes for different homology-derived distance restraints in MODELLER restraints
# files.
hddr_groups = ("9", # CA-CA.
               "10", # Main chain NO.
               "23", # Main chain-side chain.
               "26"  # Side chain-side chain.
               )

def get_modeller_dist(modeller_atm_i, modeller_atm_j):
    return math.sqrt((modeller_atm_i.x-modeller_atm_j.x)**2 +
                     (modeller_atm_i.y-modeller_atm_j.y)**2 +
                     (modeller_atm_i.z-modeller_atm_j.z)**2)

def get_modeller_atom(modeller_residue, atom_type):
    if atom_type in modeller_residue.atoms:
        return modeller_residue.atoms[atom_type]
    else:
        return None


def custom_argmax(l):
    return max(zip(range(0, len(l)), l), key=lambda t: t[1])[0]

def custom_argmin(l):
    return min(zip(range(0, len(l)), l), key=lambda t: t[1])[0]
