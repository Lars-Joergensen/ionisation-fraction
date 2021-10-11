#!/usr/bin/env python
# coding: utf-8

# outputs baryon temperature for Planck parameters for comparison with own results, no reionisation

# import necessary modules as used in thermo.py example in CLASS
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from classy import Class
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
import math


# refined Planck 2018 parameters
my_settings = {'output' : 'tCl,pCl,nCl',
                    'reio_parametrization':'reio_none',
                    'h':0.674,
                    'omega_b':0.02237,
                    'omega_cdm':0.1200,
                    'A_s':2.098903167e-09,
                    'n_s':0.965,
                    'thermodynamics_verbose':1
                    }

# call CLASS
M = Class()
M.set(my_settings)
M.compute()
thermo = M.get_thermodynamics()

Tb = thermo['Tb [K]']
z = thermo['z']


# plot
plt.plot(z,Tb)
plt.xlim(1e-4,2e3)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\mathrm{redshift} \,\,\, z$')
plt.ylabel(r'$\mathrm{baryon \,\, temperature} \,\,\, T_{\mathrm{b}}$')
plt.gca().invert_xaxis()
plt.show()
