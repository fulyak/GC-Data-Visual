# GC-Data-Visual

Overview
==========

This package takes the updated Baumgardt et al. 2021 Globular Cluster Catalog data (https://people.smp.uq.edu.au/HolgerBaumgardt/globular/) containing mean radial velocities, proper motion, and orbital parameters, of each globular cluster, and provides a quick visualization of any one or two parameters from that dataset.

How To Use
==========

First, install this package using:

``pip install GCDataVis``

Once you are in the directory of this package, enter the GCDataVis subdirectory:

``cd GCDataVis/``

Run Python on the visualize_data.py file.

``python visualize_data.py``

You will be prompted to enter parameters that you want to plot. Type in the one or two parameters you would like to plot, and make sure the spelling and capitalization is valid according to the following table. If you are only interested in seeing the distribution of one parameter, enter "N/A" for the second parameter when prompted. 

Here is the table of valid parameters:

| Name   |Meaning           |
| ------ |------------------|
| RA     |Right ascension   |
| DEC    |Declination       |
| l      |Galactic longitude|

   
