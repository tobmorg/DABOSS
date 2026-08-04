# DABOSS

DABOSS stands for **Debiasing Algorithm for Bodies in the Outer Solar System**. This algorithm is designed to debias populations of Trans-Neptunian Objects (TNOs) and Centaurs/Scattered Disk Objects. It uses orbital data from the Minor Planet Center (MPC), together with a compiled list of survey fields.

The debiasing routine uses the semi-major axis, eccentricity, inclination, argument of pericenter, longitude of the ascending node, and absolute magnitude for each object. It also uses survey-field information, including right ascension, declination, angular width and height of each frame, and limiting apparent magnitude. The field center coordinates are given in a heliocentric equatorial coordinate system. The method is inspired by the approach developed by [Vitense, Krivov & Löhne 2010](https://ui.adsabs.harvard.edu/abs/2010A%26A...520A..32V/abstract) and described in more detail in Morgner & Krivov 2026.

## External Data Used

The Algorithm uses the following external datasets:
- The data for the orbital elements and absolute magnitudes of [TNOs](http://www.minorplanetcenter.org/iau/lists/TNOs.html) and [Centaurs/Scattered Disk Objects](http://www.minorplanetcenter.org/iau/lists/Centaurs.html) were taken from the MPC. 
- The parameters characterizing each survey were retrieved from the survey publications. They are listed in `data/surveys.csv`, and the `ref` column contains the Bibcode for the respective survey publication. You can paste this Bibcode directly to [ADS](https://ui.adsabs.harvard.edu/) to view the publication.
- The approximate dynamical classification uses fixed values for the eccentricity and pericenter distance for the scattering and detached populations, which were taken from [Gladman & Volk (2021)](https://ui.adsabs.harvard.edu/abs/2021ARA%26A..59..203G/abstract). Resonant objects were classified using the results of numerical integrations provided by the [Deep Ecliptic Survey team](https://www2.boulder.swri.edu/~buie/kbo/desclass.html).

## Requirements

DABOSS uses both Python and C++. The scripts that prepare the input data are written in Python and require NumPy and Pandas. The main debiasing routine is written in C++. To run it without changing the code, you need `g++`, OpenMP, and `make`. The code has been tested on Linux and MacOS.

OpenMP is used to run parts of the debiasing code in parallel, which can make the calculation much faster. If your system does not support OpenMP, you can still run the code after making a few changes. These changes are listed in the **Long Version** section below.


## How to use DABOSS

DABOSS is set up such that you can download TNO and Centaur data from the MPC, run the debiasing routine, classify the objects, and estimate their sizes and masses. The collection of surveys can be found at `data/surveys.csv`. Theoretically, you can also use your own set of surveys as input. However, if you do not want to change the code, you input file should have the same format as the file used here. The code reads the first four columns. You could also use your own set of TNOs as input for the debiasing. In this case, make sure the file is in the same format as the `data/tnos_mpc.csv` file. 
The short version below shows the standard workflow. The long version explains each step in more detail and describes what to change if the code does not run.

## Short Version

From the main directory, run:

```bash
make prepare
make debias
make classify
make masses
```

This runs the full workflow: convert the MPC data to csv tables, run the debiasing algorithm, classify the objects, and calculate diameters and masses. The returned files are:
- ```output/tnos_debiased.csv```: Table with orbital elements, absolute magnitudes and detection probabilty of all TNOs.  
- ```output/probability_matrix.bin```: Table with detection probabilities of every TNO (column) in each survey (row). A python script to read the matrix can be found under ```python/read_prob_matrix.py```.
- ```output/tnos_debiased_classified.csv```: Same as ```tnos_debiased.csv```but with approximate dynamical classification.
- ```output/tnos_debiased_classified_masses.csv```: Same as ```tnos_debiased_classified.csv```but with additional diameters and masses for every TNO.

## Long Version

### 1. Download the MPC data

Download the [TNO](http://www.minorplanetcenter.org/iau/lists/TNOs.html) and [Centaur/Scattered Disk Objects](http://www.minorplanetcenter.org/iau/lists/Centaurs.html) data from the Minor Planet Center. This should give you two text files:

```text
TNOs.txt
Centaurs.txt
```


### 2. Add the input files

Place both files in the `input` directory. Do not rename the files, and do not change their formatting. The script that reads these files depends on the exact column positions in each line. Even small changes to the spacing or line format can cause the data to be read incorrectly.

### 3. Prepare the data

From the main directory, run:

```bash
make prepare
```

This creates the file `data/tnos_mpc.csv`. It combines the TNO and Centaur data and contains the object information needed for the debiasing step.

### 4. Set the debiasing parameters

Open `cpp/src/run_debiasing.cpp`. In this file, you can change the parameters used by the debiasing routine.

### 5. Run the debiasing routine

From the main directory, run:

```bash
make debias
```

This compiles and runs the C++ debiasing code. The C++ build settings are defined in the Makefile inside the `cpp/` directory. If the code does not compile or run correctly, this Makefile is a good place to check first.

Common things you may need to change are listed below.

#### Compiler

The compiler is set by the `COMPILER` entry in the Makefile. On some systems, the default `g++` compiler does not work with OpenMP. In that case, you may need to use a different compiler. For example, on macOS, you may need to install a newer version of `g++` with Homebrew and use something like:

```make
COMPILER = g++-15
```

instead of:

```make
COMPILER = g++
```

#### OpenMP

OpenMP is used for parallelization. If OpenMP is not available on your system, you can remove it and run the code in a single thread. This will make the debiasing routine slower, but it should still work.

To do this, remove the OpenMP flag from the `FLAGS` entry in the Makefile:

```make
-fopenmp
```

You also need to remove or comment out the OpenMP parts of the C++ code. In `cpp/src/debiasing.cpp`, remove or comment out:

```cpp
#include "omp.h"
```

and:

```cpp
#pragma omp parallel for
```

### 6. Classify the objects

After the debiasing step is finished, run:

```bash
make classify
```

This assigns each TNO to one of the following dynamical classes: classical, resonant, scattering, or detached. This classification is approximate. The classified objects are saved in `output/tnos_debiased_classified.csv`.

### 7. Calculate sizes and masses

Run:

```bash
make masses
```

This calculates estimated diameters and masses for the TNOs. The final object table is saved in `output/tnos_debiased_classified_masses.csv`. 
