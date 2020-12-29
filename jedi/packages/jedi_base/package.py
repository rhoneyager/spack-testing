# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *


class JediBase(Package):
    """Base packages for jedi."""

    homepage = "https://github.com/rhoneyager/spack-fake-package"
    git      = "https://github.com/rhoneyager/spack-fake-package.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')

    depends_on('zlib+optimize+pic+shared')
    depends_on('cmake')
    depends_on('udunits')
    depends_on('openblas')
    depends_on('boost~atomic~chrono~clanglibcpp~container~context~coroutine~date_time~debug~exception~fiber~filesystem~graph~icu~iostreams~locale~log~math~mpi+multithreaded~numpy~pic~program_options~python~random~regex~serialization+shared~signals~singlethreaded+system~taggedlayout~test+thread~timer~versionedlayout~wave cxxstd=14 visibility=hidden')
    depends_on('eigen')
    depends_on('cgal+header-only')
    depends_on('szip')
    depends_on('hdf5+hl+szip')
    # depends_on('parallel-netcdf')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    # depends_on('nccmp')


    def install(self, spec, prefix):
        make()
        make('install')
