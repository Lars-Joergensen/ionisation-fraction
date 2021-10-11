## Code used in "Formation and Evolution of the Cosmic Microwave Background: Recombination"

This repository contains the Mathematica notebooks used for computing the different cases of the ionisation fraction in my bachelor thesis along with the input files that were used for CLASS. Note that for running CLASS, the whole code has to be downloaded, which can be done here: http://class-code.net.

In particular,

- **freezeout_kt.m**     was used in calculating the residual ionisation according to the approximations in Kolb and Turner (1994) in Section 3.3 of my thesis,
- **efraction.m**        was used for the computation of the ionisation fraction using the photon temperature and without reionisation, shown in Section 4.2 of my thesis, includes code used for comparison of expansion rate and interaction rate as seen in Chapter 3,
- **efrac_and_Tb.m**     contains the code for the solution of the ODEs for the ionisation fraction and the baryon temperature together, shown in Section 4.4 of my thesis,
- **efraction_reio.m**   contains the same code as "efraction.nb" but this time reionisation is taken into account, shown in Chapter 5 of my thesis,

- **class_efrac.py**      is the CLASS input file for the ionisation fraction according to the refined Planck 2018 results as given by the PDG, serving as comparison to "efraction.m",
- **class_omegab.py**     is the CLASS input file used to show the exemplary Omega_b h^2 dependence of the residual ionisation in Section 4.3 of my thesis,
- **class_tb.py**         is the CLASS input file that outputs the baryon temperature used as a comparison to the temperature from "efrac_and_Tb.m",
- **class_reio.py**       is the CLASS input file for the ionisation fraction including reionisation, serving as a comparison to "efraction_reio.m".

While the input is the same, the output has been modified in some cases in order to produce plots instead of exporting data, since the plots in my thesis were made with MATLAB.
