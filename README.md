# altMOD
altMOD is a MODELLER (https://salilab.org/modeller/) [1] plugin for improved 3D homology model building. Right now, it allows to incorporate in the program's objective function terms for interatomic distances statistical potentials, such as DOPE [2] and DFIRE [3]. The effect of adding statistical potentials in the objective function of MODELLER is described in _Revisiting the "satisfaction of spatial restraints" approach of MODELLER for protein
homology modeling"_ (Janson et al., 2019). In a benchmark with 225 single-template homology models, we found that the inclusion of DOPE in the objective function of MODELLER brings an average improvement of 1.3% and 2.0% in GDT-HA [4] and lDDT [5] and a large improvement of -29.8% in MolProbity scores [6].

# Installation
Just put the _altmod_ directory (the one with the _\_\_init\_\_.py_ file inside it) of this package in one of your _sys.path_ directories.

# Example
The _Automodel\_statistical\_potential_ class in the _altmod_ module is a child class of the original _automodel_ class of MODELLER. Just import _Automodel\_statistical\_potential_ in your scripts and use it instead of the default _automodel_ class (see the _examples/altmod\_basic.py_ script in this package). By default, altMOD includes in the objective function DOPE statistical potential terms, with a weight of 0.5 and a contact shell value of 8.0 Å. We found that these values give best 3D modeling results when coupled with standard sigma values produced by the MODELLER histogram-based approach [1]. These parameters may be changed by the user (see the _Advanced usage_ section).

# Advanced usage
There are several parameters which may be changed in altMOD (see the _examples/altmod\_advanced.py_ script in this package).

* Statistical potential type: altMOD allows to use the following statistical potentials:
    - DOPE (default): we found DOPE to give best results in 3D modeling benchmarks.
    - DFIRE: a statistical potentials with very similar characteristics to DOPE. It also has a similar (but slightly inferior) performance in 3D modeling.
    - DOPE-HR: an "high-resolution" version of DOPE (https://salilab.org/modeller/manual/node259.html). We found that it obtains a much worse performance in 3D modeling with respect to the default DOPE (data not published). It still may be used for experimental purposes.
    - Fiser-Melo potential: a statistical potential originally developed for loop modeling [7]. It has an inferior performance with respect to DOPE and DFIRE (data not published), but it may be used for experimental purposes.
* Weight of the statistical potential terms in the objective function: by default this weight is 0.5. We found this value to give best results in 3D modeling benchmarks. Users may change it through the _altmod\_w\_sp_  attribute at their will.

* Contact shell value for non-bonded interactions (including statistical potentials terms): by default this value is set to 8.0 Å. The higher its value is, the higher are the computational times (with a value of 8.0 Å, computational times increase by ~6.5 over the default MODELLER). We found that increasing this value over 8.0 Å does not change significantly 3D modeling quality. Decreasing it under 8.0 Å, gradually decreases computational times, but also 3D modeling quality decreases on average (data not published). Users may change this parameter through the _sp\_contact\_shell_ attribute according to their needs.

# References
1. Sali A, Blundell TL. Comparative protein modelling by satisfaction of spatial restraints. J Mol Biol. 1993;234: 779–815. doi:10.1006/jmbi.1993.1626
2. Shen M-Y, Sali A. Statistical potential for assessment and prediction of protein structures. Protein Sci. 2006;15: 2507–2524. doi:10.1110/ps.062416606
3. Zhou H, Zhou Y. Distance-scaled, finite ideal-gas reference state improves structure-derived potentials of mean force for structure selection and stability prediction. Protein Sci. 2002;11: 2714–2726. doi:10.1110/ps.0217002
4. Kryshtafovych A, Monastyrskyy B, Fidelis K, Moult J, Schwede T, Tramontano A. Evaluation of the template-based modeling in CASP12. Proteins. 2018;86 Suppl 1: 321–334. doi:10.1002/prot.25425
5. Mariani V, Biasini M, Barbato A, Schwede T. lDDT: a local superposition-free score for comparing protein structures and models using distance difference tests. Bioinformatics. 2013;29: 2722–2728. doi:10.1093/bioinformatics/btt473
6. Chen VB, Arendall WB, Headd JJ, Keedy DA, Immormino RM, Kapral GJ, et al. MolProbity: all-atom structure validation for macromolecular crystallography. Acta Crystallogr D Biol Crystallogr. 2010;66: 12–21. doi:10.1107/S0907444909042073
7. Fiser A, Do RK, Sali A. Modeling of loops in protein structures. Protein Sci. 2000;9: 1753–1773. doi:10.1110/ps.9.9.1753
