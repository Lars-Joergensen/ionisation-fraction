#!/usr/bin/env python
# coding: utf-8

# outputs ionisation fraction for varying omega_b, no reionisation

# import necessary modules as used in thermo.py example in CLASS
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from classy import Class
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
import math


# for-loop to depict exemplary Omega_b h^2 dependence of ionisation fraction
# unnatural unless omega_b = 0.02237
thermolist = []
for i in range(7,12):
    # settings for every omega_b
    omegavar = i*0.02237*0.1
    common_settings = {'output' : 'tCl,pCl,nCl',
                    'reio_parametrization':'reio_none',
                   'h':0.674,
                   'omega_b':omegavar,          # omega_b = Omega_b h^2
                   'omega_cdm':0.1200,
                   'A_s':2.098903167e-09,
                   'n_s':0.965,
                   'thermodynamics_verbose':1
                   }
    # call CLASS
    M = Class()
    M.set(common_settings)
    M.compute()
    thermo = M.get_thermodynamics()
    thermolist.append(thermo)
    xe = thermo['x_e']
    xinf = xe[0]
    print('residual ionisation fraction times Omega_b h^2: ', xinf*omegavar/0.674)
    

xe = [thermolist[i]['x_e'] for i in range(len(thermolist))]
z = thermolist[0]['z']

# plot settings
plt.xlim(1e-2,2e+3)
plt.xlabel('$z$')
plt.ylabel('$X_{\mathrm{e}}$')
plt.xscale('log')
plt.yscale('log')

# produce plot for every omega_b
for i in range(len(thermolist)):
    plt.plot(z,xe[i], label=r'$\Omega_{\mathrm{b}} h^2 = 0.02237 \times $'+str(round((i+7)*0.1,1)))
    plt.gca().invert_xaxis()
    plt.legend(loc='best')
plt.show()


