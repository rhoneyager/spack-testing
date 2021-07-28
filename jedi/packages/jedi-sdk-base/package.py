# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *

class JediSdkBase(BundlePackage):
    """Base packages for jedi."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')


    # CMake needs to be built with apple-clang on macs.
    depends_on('boost~atomic~chrono~clanglibcpp~container~context~coroutine~date_time~debug~exception~fiber~filesystem~graph~icu~iostreams~locale~log~math~mpi+multithreaded~numpy~pic~program_options~python~random~regex~serialization+shared~signals~singlethreaded+system~taggedlayout~test+thread~timer~versionedlayout~wave cxxstd=14 visibility=hidden', type=('build', 'run'))
    depends_on('cgal+header_only', type='build')
    depends_on('cmake', type=('build', 'run'))
    depends_on('ecbuild', type=('build', 'run'))
    depends_on('eigen', type=('build', 'run'))
    depends_on('gsl-lite', type=('build', 'run'))

    depends_on('zlib+optimize+pic+shared', type=('build', 'run'))

    depends_on('udunits', type=('build', 'run')) # Local package definition. 2.2.24 is broken on macos. 2.2.28 works.
    depends_on('openblas', type=('build', 'run')) # Depends on which MPI works for the system. Needs some pref config.
    depends_on('szip', type=('build', 'run'))
    depends_on('hdf5@1.12.0:+hl+szip', type=('build', 'run')) # 1.12 needed for jedi. Make optional? C interface only. MPI.
    # depends_on('parallel-netcdf', type=('build', 'run'))
    depends_on('netcdf-c@:4.7.9', type=('build', 'run')) # C interface only. MPI. Do not use 4.8.0 yet.
    depends_on('netcdf-fortran', type=('build', 'run')) # buggy on macos 10.11. Need Fortran compiler. MPI.
    depends_on('nccmp', type=('build', 'run')) # Need only one version of this? MPI.

