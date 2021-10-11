#!/usr/bin/env python
# coding: utf-8

# outputs ionisation fraction for Planck parameters for comparison with own Data, including reionisation

# import necessary modules as used in thermo.py example in CLASS
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from classy import Class
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
import math


# reionisation parameters
my_settings = {'output' : 'tCl,pCl,nCl',
                    'reio_parametrization':'reio_camb',
                   'h':0.674,
                   'omega_b':0.02237,
                   'omega_cdm':0.1200,
                   'A_s':2.098903167e-09,
                   'n_s':0.965,
                   'tau_reio':0.054,
                   'thermodynamics_verbose':1
                   }
# call CLASS
M = Class()
M.set(my_settings)
M.compute()
thermo = M.get_thermodynamics()
derived = M.get_current_derived_parameters(['z_reio','z_rec'])
print('recombination at: ', derived['z_rec'])
print('reionisation at: ', derived['z_reio'])


xe = thermo['x_e']
z = thermo['z']

plt.plot(z,xe)
plt.xlim(1e-4,2e3)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$z$')
plt.ylabel(r'$X_{\mathrm{e}}$')
plt.gca().invert_xaxis()
plt.show()



