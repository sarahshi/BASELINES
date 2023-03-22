========================
Importing Data
========================

We walk through an implementation of PyBaselines here. We recommend following this tutorial as-is for those not familiar with navigating between directories in Python. Create this following file structure locally: 

PyBaselines/
├── MC3_RUNFILE.py
└── Inputs/
    ├── ChemThick.csv
    ├── ReflectanceSpectra/
    └── TransmissionSpectra/
        └── YourDirectoryName
            ├── a.CSV
            ├── b.CSV
            └── c.CSV

Users can batch process their FTIR data by creating directories containing all spectra files, called SampleSpectra here, in comma separated values (.CSV). Users should format their glass composition and thickness data as a spreadsheet of comma separated values (.CSV) file with each analysis having its own row and columns of sample name, oxide components in weight percentages, and thicknesses and uncertainties in thickness in micrometers. The spectrum file name **must** match the sample name input in the chemistry and thickness file. The order of columns doesn’t matter, as the Python Pandas package will identify the column heading regardless of its location. 

The following columns are required for this ChemThick file:

*  Sample
*  SiO2
*  TiO2
*  Al2O3
*  Fe2O3
*  FeOt
*  MnO
*  MgO 
*  CaO 
*  Na2O
*  K2O 
*  P2O5 
*  Thickness
*  Sigma_Thickness

For example, here a screenshot of a CSV spreadsheet containing the glass composition and thickness data. You can use the ChemThickTemplate.csv from the GitHub repository to create your own. 

.. image:: img/chemthick.png


For the liquid composition, PyBaselines allows users to specify how they partition Fe between ferrous and ferric iron, because glass density changes due to the proportion of Fe$^{3+}$. To avoid ambiguity, the ChemThick file handles this by providing two columns for FeO and Fe$_{2}O_{3}$. If the speciation is unknown, input all Fe as FeO and leave the Fe$_{2}O_{3} cells empty. This will not constitute the largest uncertainty, as the molar absorptivities and thicknesses impact concentrations more significantly. 


*******
========================
MC$^3$ for Transmission FTIR Spectra
========================

We use the os package in Python to facilitate navigation to various directories and files. To load the transmission FTIR spectra, you must provide the path to the directory. Specify the wavenumbers of interest to fit all species peaks between 5500 and 1000 cm$^{-1}$. 

.. code-block:: python

    PATH = os.getcwd() + '/Inputs/TransmissionSpectra/YourDirectoryName/'
    FILES = sorted(glob.glob(PATH + "*"))
    DFS_FILES, DFS_DICT = bl.Load_SampleCSV(FILES, wn_high = 5500, wn_low = 1000)

bl.Load_SampleCSV returns DFS_FILES, a list of all the spectra names (without .CSV), and DFS_DICT, a dictionary of the wavenumber and absorbance of each sample. 

To load the CSV containing glass chemistry and thickness information, provide the path to the file. 

.. code-block:: python

    CHEMTHICK_PATH = os.getcwd() + '/Inputs/ChemThick.csv'
    MICOMP, THICKNESS = bl.Load_ChemistryThickness(CHEMTHICK_PATH)

Inspect each returned data type to ensure that the data imports are successful. 


========================
Thicknesses from Reflectance FTIR Spectra 
========================

Loading reflectance FTIR spectra occurs through a near-identical process. Define your path to the file, but modify the wavenumbers of interest for either glass or olivine. 

.. code-block:: python

    REF_PATH = os.getcwd() + '/Inputs/ReflectanceSpectra/YourDirectoryName/'
    REF_FILES, REF_DICT = bl.Load_SampleCSV(REF_FILES, wn_high = wn_high, wn_low = wn_low)
    REF_FILES = sorted(glob.glob(REF_PATH + "*"))

For olivine, specify the following wavenumber range based on :cite:t:`NicholsandWysoczanski2007` and calculate the relevant reflectance index $n$ from :cite:t:`DHZ1992`. 

.. code-block:: python
    wn_high = 2700 
    wn_low = 2100
    REF_FILES, REF_DICT = bl.Load_SampleCSV(REF_FILES, wn_high = wn_high, wn_low = wn_low)
    n_ol = bl.ReflectanceIndex(XFo) # Input your XFo between 0-1. 

For glass, specify the following wavenumber range based on :cite:t:`NicholsandWysoczanski2007` and enter the relevant reflectance index $n$. We use the reflectance index for basaltic glasses from :cite:t:`NicholsandWysoczanski2007` here. 

.. code-block:: python
    wn_high = 2850 
    wn_low = 1700
    REF_FILES, REF_DICT = bl.Load_SampleCSV(REF_FILES, wn_high = wn_high, wn_low = wn_low)
    n_gl = 1.546 


========================
Data Import Complete 
========================

That is all for loading files! You are ready to get rolling with PyBaselines. See the example notebook MC3_RUNFILE.ipynb, under the big examples heading, to see how to run PyBaselines and export files. 
