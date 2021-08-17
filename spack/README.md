# A Spackified Stack for JEDI

This directory contains everything you need to build the JEDI stack using [Spack](https://spack.readthedocs.io/en/latest/).

Spack does work, but it is quite a headache to set up properly. Your mileage may vary.

## Setting up Spack

Choose your own adventure. You can either install Spack locally or can experiment with a virtual machine image.

1. Install Spack locally on [Linux](./docs/setup-local-linux.md) or [macOS](./docs/setup-local-macos.md).
2. [Use an already-established image](./docs/setup-fromAMI.md)
3. [Build your own image using Packer](./docs/setup-packer.md)

## Adding the JCSDA Spack repositories

Repositories are located in the ```repos``` folder. There are three:

1. ```jedi_stack_components```: Components like atlas, ecbuild, eckit, and gsl-lite. These are not provided by the default Spack environment.
2. ```jedi_components```: Components like jedi-cmake, oops, ioda, and ufo. We develop these.
3. ```jedi_environments```: Meta-packages that depend on sets of JEDI stack components to produce a consistent development environment.

Each repository has several packages, and each package has its own ```package.py``` file that describes the package's source, versions, dependencies, options, and build instructions.

To add a repository to Spack, run:

```bash
spack repo add path_to_the_repository
```

To add all three repositories:

```bash
spack repo add /path/to/jedi_stack_components
spack repo add /path/to/jedi_components
spack repo add /path/to/jedi_environments
```

## Detecting your compilers

```bash
spack compiler find
```

## Building some packages

Spack has an unfortunate naming convention. To build a package, use ```spack install```.

Examples:
```bash
spack install zlib                # Default version and compiler
spack install zlib%clang@12.0.1   # zlib built with clang 12.0.1
spack install engines-env+python%gcc@10.0.0 ^python@3.8.11   # "engines-env" package, with Python turned on, and using Python 3.8.11.
```

To load packages into your current shell, use ```spack load package_name``` or create and enter a Spack environment.

## Creating and using a Spack environment

See the Spack docs.

```bash
spack env create my-spack-environment
spack env activate my-spack-environment
spack install engines-env
spack concretize
```

## Using Spack with ecbuild and CMake

Example where we just build ioda-engines (for speed):

```bash
spack env activate my-spack-environment
git checkout https://github.com/JCSDA-internal/ioda.git
cd ioda/src/engines
mkdir build
cd build
cmake ..
make -j12
ctest
```

Example with a bundle:

```bash
spack env activate my-spack-environment
git checkout https://github.com/JCSDA-internal/ioda-bundle.git
cd ioda-bundle
mkdir build
ecbuild ..
make -j12
ctest
```

## What's working:

- [x] AMIs
- [x] The required JEDI stack components (CMake, udunits, jpeg, zlib, png, szip, lapack (via BLAS), Boost (headers), Eigen3, Bufr, CGAL, git, git-lfs, ecbuild, eckit, fckit, atlas, hdf5, pnetcdf, netcdf-c, netcdf-fortran, nccmp, gsl-lite
- [ ] Optional stack components:
    - [x] odc
    - [x] pybind11
    - [x] boost (all libs)
    - [x] numpy
    - [x] sqlite
    - [x] json
    - [x] json-schema-validator
    - [x] fftw
    - Unconsidered / untested: jasper, armadillo, xerces, nceplibs, tkdiff, pyjedi, geos, proj, ecflow, gptl, nco, pio, esmf, baselibs, pdtoolkit, tau2, fms
- Bundles:
    - [ ] ioda-bundle
    - [ ] ufo-bundle
- Machines
    - [x] macOS - **NOTE**: Instructions needed. Needs the *clingo* concretizer. Is usually helps to pre-load some hard-to-build packages using HomeBrew first (gcc, llvm, mpfr, sqlite, openssl@1.1, python@3.9, git, git-lfs).
    - [x] Ubuntu 20.04 - **NOTE**: The AMI is built with quite a few packages and compilers pre-installed to speed up Spack build times.
    - [x] Windows Subsystem for Linux v2, based on Ubuntu 20.04.
- Compilers
    - [x] gcc 11.1.0, 10.3.0, 9.4.0, 8.5.0, 7.5.0.
    - [x] Apple Clang 12.0.5
    - [x] LLVM Clang 12.0.1
    - [x] Intel 2021.3
    - [ ] oneAPI 2021.3 (icx)
    - [ ] nVidia HPC SDK (formerly PGI)

