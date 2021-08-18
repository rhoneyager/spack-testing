# A Spackified Stack for JEDI

This directory contains everything you need to build the JEDI stack using [Spack](https://spack.readthedocs.io/en/latest/).

Spack does work, but it is quite a headache to set up properly. Your mileage may vary.

## Setting up Spack

Choose your own adventure. You can either install Spack locally or can experiment with a virtual machine image.

For installation details, see the [Spack](https://spack.readthedocs.io/en/latest/) website.

An Amazon AMI is available for testing. To launch it, customize these settings and run:

```bash
export MYNAME=your_name_here
export AWSKEY=your_aws_key_name_here      # See https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:
aws ec2 run-instances --region us-east-1 --image-id ami-0f0eeaeb6d367e95b --instance-type c4.4xlarge --cpu-options "CoreCount=8,ThreadsPerCore=1" --count 1 --security-group-ids sg-0f715b41f30e6d3aa --instance-initiated-shutdown-behavior terminate --key-name "${AWSKEY}" --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=spack-testing-${MYNAME}}]" --block-device-mapping DeviceName=/dev/sda1,Ebs={VolumeSize=100}
```

After the instance boots, you can get the IP address by going to the [EC2 console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances:sort=instanceState) and finding your instance. You can SSH to the instance using:

```bash
ssh ubuntu@your_instance_ip_address
```

It may take 1-2 minutes before SSH is ready.

### Looking around

Spack is accessible using the ```spack``` command. There are many sub-commands that are detailed in the Spack documentation.
A few examples are given later in this README.

Spack is installed in ```/opt/spack```.

The AMI has several available compilers to choose from. Intel and NVidia can also be installed, but the AMI takes *forever* to build.

```bash
spack compiler list

==> Available compilers
-- clang ubuntu20.04-x86_64 -------------------------------------
clang@12.0.0  clang@11.0.0  clang@10.0.0  clang@9.0.1

-- gcc ubuntu20.04-x86_64 ---------------------------------------
gcc@11.1.0  gcc@10.3.0  gcc@9.3.0  gcc@8.4.0
```

Spack can build many packages. These are grouped into repositories.

```bash
spack repo list
==> 4 package repositories.
jedi_stack_components    /opt/spack/jedi-stack/spack/repos/jedi_stack_components
jedi_components          /opt/spack/jedi-stack/spack/repos/jedi_components
jedi_environments        /opt/spack/jedi-stack/spack/repos/jedi_environments
builtin                  /opt/spack/var/spack/repos/builtin
```

Each repository has several packages, and each package has its own ```package.py``` file that describes the package's source, versions, dependencies, options, and build instructions.

The builtin repository contains the recipes for thousands of packages. These recipes are contributed by users like
you and are vetted by the Spack maintainers on GitHub.

There are three JCSDA Spack Repositories:

1. ```jedi_stack_components```: Components like atlas, ecbuild, eckit, and gsl-lite. These are not provided by the default Spack environment.
2. ```jedi_components```: Components like jedi-cmake, oops, ioda, and ufo. We develop these.
3. ```jedi_environments```: Meta-packages that depend on sets of JEDI stack components to produce a consistent development environment.

## Getting information about a package

Use the ```spack info``` command.

```bash
spack info ioda
CMakePackage:   ioda

Description:
    Interface for Observation Data Access.

Homepage: https://github.com/JCSDA-internal/ioda

Maintainers: @rhoneyager @mmiesch

Externally Detectable: 
    False

Tags: 
    None

Preferred version:  
    develop    [git] git@github.com:JCSDA-internal/ioda.git on branch develop

Safe versions:  
    develop    [git] git@github.com:JCSDA-internal/ioda.git on branch develop
    master     [git] git@github.com:JCSDA-internal/ioda.git on branch master
    2.0.0      https://github.com/JCSDA/ioda/archive/refs/tags/2.0.0.tar.gz
    1.0.0      https://github.com/JCSDA/ioda/archive/refs/tags/1.0.0.tar.gz

Variants:
    Name [Default]                 Allowed values          Description
    ===========================    ====================    ==================================

    bufr [off]                     on, off                 
    build_type [RelWithDebInfo]    Debug, Release,         CMake build type
                                   RelWithDebInfo,         
                                   MinSizeRel              
    ipo [off]                      on, off                 CMake interprocedural optimization
    odc [off]                      on, off                 

Installation Phases:
    cmake    build    install

Build Dependencies:
    atlas  bufr  cmake  ecbuild  eckit  fckit  gsl-lite  hdf5  jedi-cmake  jedi-sdk-base  netcdf-c  odc  oops

Link Dependencies:
    atlas  bufr  eckit  fckit  gsl-lite  hdf5  jedi-sdk-base  netcdf-c  odc  oops

Run Dependencies:
    None

Virtual Packages: 
    None
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

To see what Spack's dependency chain for a particular package, you can use the ```spack spec``` command.

```bash
spack spec engines-env

Input spec
--------------------------------
engines-env

Concretized
--------------------------------
engines-env@main%gcc@11.1.0+python arch=linux-ubuntu20.04-haswell
    ^jedi-cmake@1.1.0%gcc@11.1.0~ipo build_type=RelWithDebInfo arch=linux-ubuntu20.04-haswell
        ^cmake@3.21.1%gcc@11.1.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-ubuntu20.04-haswell
            ^ncurses@6.2.20200212%gcc@11.1.0+symlinks+termlib abi=6 arch=linux-ubuntu20.04-haswell
            ^openssl@1.1.1k%gcc@11.1.0~docs+systemcerts arch=linux-ubuntu20.04-haswell
                ^perl@5.30.0%gcc@11.1.0~cpanm+shared+threads arch=linux-ubuntu20.04-haswell
                ^zlib@1.2.11%gcc@11.1.0+optimize+pic+shared arch=linux-ubuntu20.04-haswell
    ^jedi-sdk-base@main%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
        ^boost@1.76.0%gcc@11.1.0~atomic~chrono~clanglibcpp~container~context~coroutine~date_time~debug~exception~fiber~filesystem~graph~icu~iostreams~locale~log~math~mpi+multithreaded~numpy~pic~program_options~python~random~regex~serialization+shared~signals~singlethreaded+system~taggedlayout~test+thread~timer~versionedlayout~wave cxxstd=14 visibility=hidden arch=linux-ubuntu20.04-haswell
        ^cgal@5.0.3%gcc@11.1.0~core~demos+eigen+header_only~imageio~ipo+shared build_type=Release arch=linux-ubuntu20.04-haswell
            ^eigen@3.3.9%gcc@11.1.0~ipo build_type=RelWithDebInfo patches=55daee880b7669807efc0dcbeda2ae3b659e6dd4df3932f3573c8778bf5f8a42 arch=linux-ubuntu20.04-haswell
            ^gmp@6.2.1%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                ^autoconf@2.69%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                ^automake@1.16.1%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                ^libtool@2.4.6%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                ^m4@1.4.18%gcc@11.1.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-ubuntu20.04-haswell
            ^mpfr@4.1.0%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                ^autoconf-archive@2019.01.06%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                ^texinfo@6.5%gcc@11.1.0 patches=12f6edb0c6b270b8c8dba2ce17998c580db01182d871ee32b7b6e4129bd1d23a,1732115f651cff98989cb0215d8f64da5e0f7911ebf0c13b064920f088f2ffe1 arch=linux-ubuntu20.04-haswell
        ^ecbuild@3.6.2%gcc@11.1.0~ipo build_type=RelWithDebInfo arch=linux-ubuntu20.04-haswell
        ^gsl-lite@0.38.1%gcc@11.1.0~ipo build_type=RelWithDebInfo arch=linux-ubuntu20.04-haswell
        ^hdf5@1.12.1%gcc@11.1.0~cxx~fortran+hl~ipo~java+mpi+shared+szip~threadsafe+tools api=default build_type=RelWithDebInfo arch=linux-ubuntu20.04-haswell
            ^libaec@1.0.5%gcc@11.1.0~ipo build_type=RelWithDebInfo arch=linux-ubuntu20.04-haswell
            ^openmpi@4.1.1%gcc@11.1.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker~pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=none schedulers=none arch=linux-ubuntu20.04-haswell
                ^hwloc@2.5.0%gcc@11.1.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~opencl+pci~rocm+shared arch=linux-ubuntu20.04-haswell
                    ^libpciaccess@0.16%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                        ^pkg-config@0.29.1%gcc@11.1.0+internal_glib patches=49ffcd644e190dc5efcb2fab491177811ea746c1a526f75d77118c2706574358 arch=linux-ubuntu20.04-haswell
                        ^util-macros@1.19.3%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                    ^libxml2@2.9.10%gcc@11.1.0~python arch=linux-ubuntu20.04-haswell
                        ^libiconv@1.16%gcc@11.1.0 libs=shared,static arch=linux-ubuntu20.04-haswell
                        ^xz@5.2.4%gcc@11.1.0~pic libs=shared,static arch=linux-ubuntu20.04-haswell
                ^libevent@2.1.12%gcc@11.1.0+openssl arch=linux-ubuntu20.04-haswell
                ^numactl@2.0.14%gcc@11.1.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-ubuntu20.04-haswell
                ^openssh@8.2p1%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
        ^nccmp@1.8.9.0%gcc@11.1.0~ipo build_type=RelWithDebInfo arch=linux-ubuntu20.04-haswell
            ^netcdf-c@4.7.4%gcc@11.1.0~dap~fsync~hdf4~jna+mpi~parallel-netcdf+pic+shared arch=linux-ubuntu20.04-haswell
        ^netcdf-fortran@4.5.3%gcc@11.1.0~doc+pic+shared arch=linux-ubuntu20.04-haswell
        ^openblas@0.3.17%gcc@11.1.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-ubuntu20.04-haswell
        ^udunits@2.2.28%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
            ^expat@2.4.1%gcc@11.1.0+libbsd arch=linux-ubuntu20.04-haswell
                ^libbsd@0.11.3%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                    ^libmd@1.0.3%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
    ^py-numpy@1.21.1%gcc@11.1.0+blas+lapack patches=873745d7b547857fcfec9cae90b09c133b42a4f0c23b6c2d84cf37e2dd816604 arch=linux-ubuntu20.04-haswell
        ^py-cython@0.29.24%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
            ^py-setuptools@57.4.0%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                ^python@3.8.11%gcc@11.1.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-ubuntu20.04-haswell
                    ^bzip2@1.0.8%gcc@11.1.0~debug~pic+shared arch=linux-ubuntu20.04-haswell
                    ^gdbm@1.19%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                        ^readline@8.1%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                    ^gettext@0.21%gcc@11.1.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-ubuntu20.04-haswell
                        ^tar@1.30%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
                    ^libffi@3.3%gcc@11.1.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-ubuntu20.04-haswell
                    ^sqlite@3.35.5%gcc@11.1.0+column_metadata+fts~functions~rtree arch=linux-ubuntu20.04-haswell
                    ^util-linux-uuid@2.36.2%gcc@11.1.0 arch=linux-ubuntu20.04-haswell
    ^py-pybind11@2.5.0%gcc@11.1.0~ipo build_type=RelWithDebInfo arch=linux-ubuntu20.04-haswell

```


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

