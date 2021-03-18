# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *
import sys

class JediSdkBase(BundlePackage):
    """Base packages for jedi."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')


    # CMake needs to be built with apple-clang on macs.
    if sys.platform == 'darwin':
        depends_on('autoconf%apple-clang', type='build')
        # TODO: Redirect boost on Intel paired with clang.
        depends_on('boost~atomic~chrono~clanglibcpp~container~context~coroutine~date_time~debug~exception~fiber~filesystem~graph~icu~iostreams~locale~log~math~mpi+multithreaded~numpy~pic~program_options~python~random~regex~serialization+shared~signals~singlethreaded+system~taggedlayout~test+thread~timer~versionedlayout~wave cxxstd=14 visibility=hidden %apple-clang')
        depends_on('cgal+header-only%apple-clang', type='build')
        depends_on('cmake%apple-clang', type='build')
        depends_on('ecbuild%apple-clang', type='build')
        depends_on('eigen%apple-clang', type='build')
        depends_on('gsl-lite%apple-clang', type='build')
        depends_on('m4%apple-clang', type='build')
        depends_on('perl%apple-clang', type='build')

    else:
        depends_on('boost~atomic~chrono~clanglibcpp~container~context~coroutine~date_time~debug~exception~fiber~filesystem~graph~icu~iostreams~locale~log~math~mpi+multithreaded~numpy~pic~program_options~python~random~regex~serialization+shared~signals~singlethreaded+system~taggedlayout~test+thread~timer~versionedlayout~wave cxxstd=14 visibility=hidden')
        depends_on('cgal+header-only', type='build')
        depends_on('cmake', type='build')
        depends_on('ecbuild', type='build')
        depends_on('eigen', type='build')
        depends_on('gsl-lite', type='build')


    depends_on('zlib+optimize+pic+shared')

    depends_on('udunits') # Local package definition. 2.2.24 is broken on macos. 2.2.28 works.
    depends_on('openblas')
    depends_on('szip')
    depends_on('hdf5@1.12.0+hl+szip') # 1.12 needed for jedi. Make optional? C interface only. MPI.
    # depends_on('parallel-netcdf')
    depends_on('netcdf-c') # C interface only. MPI.
    depends_on('netcdf-fortran') # buggy on macos 10.11. Need Fortran compiler. MPI.
    depends_on('nccmp') # Need only one version of this? MPI.

