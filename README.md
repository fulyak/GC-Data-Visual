# GC-Data-Visual

Overview
==========

This package takes the updated Baumgardt et al. 2021 Globular Cluster Catalog data (https://people.smp.uq.edu.au/HolgerBaumgardt/globular/) containing mean radial velocities, proper motion, and orbital parameters, of each globular cluster, and provides a quick visualization of any one or two parameters from that dataset.

[![DOI](https://zenodo.org/badge/506388170.svg)](https://zenodo.org/badge/latestdoi/506388170)

How To Use
==========

First, install this package using:

``pip install GCDataVis``

Once have successfully installed the package, import the package in iPython:

``import GCDataVis``

Import the visualize_data.py file from the package.

``from GCDataVis import visualize_data``

You will be prompted to enter parameters that you want to plot. Type in the one or two parameters you would like to plot, and make sure the spelling and capitalization is valid according to the following table. If you are only interested in seeing the distribution of one parameter, enter "N/A" for the second parameter when prompted. 

Here is the table of valid parameters:

| Name     |Meaning                                                       |
| -------- |--------------------------------------------------------------|
| RA       |Right ascension                                               |
| DEC      |Declination                                                   |
| l        |Galactic longitude                                            |
| b        |Galactic latitude                                             |
| Rsun     |Distance from Sun                                             |
| R_GC     |Distance from the Galactic centre                             |
| < RV >   |Radial velocity                                               |
| mualpha  |Proper motion in right ascension                              |
| mu_delta |Proper motion in declination                                  |
| rhopmrade|Correlation coefficient between mualpha and mu_delta          |
| X        |Distance from the Galactic centre in direction of Sun         |
| Y        |Distance from the Galactic centre in direction of Solar motion|
| Z        |Distance above/below galactic plane                           |
| U        |Velocity in X direction                                       |
| V        |Velocity in Y direction                                       |
| W        |Velocity in Z direction                                       |
| RPERI    |Average perigalactic distance                                 |
| RAPO     |Average apogalactic distance                                  |

   
