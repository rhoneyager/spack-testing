# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack import *
import sys

class Jedi(BundlePackage):
    """Base jedi stack."""

    homepage = "https://github.com/JCSDA/jedi-stack"
    git      = "https://github.com/JCSDA/jedi-stack.git"

    maintainers = ['rhoneyager', 'mmiesch']

    version('main', branch='main')

    force_ac_on_macs = ''
    blas = 'openblas'
    if sys.platform == 'darwin':
        force_compiler = '%apple-clang'
        blas = 'openblas'

    depends_on('cmake' + force_ac_on_macs, type='build')
    depends_on('autoconf' + force_ac_on_macs, type='build')
    # TODO: Redirect boost on Intel paired with clang.
    depends_on('boost~atomic~chrono~clanglibcpp~container~context~coroutine~date_time~debug~exception~fiber~filesystem~graph~icu~iostreams~locale~log~math~mpi+multithreaded~numpy~pic~program_options~python~random~regex~serialization+shared~signals~singlethreaded+system~taggedlayout~test+thread~timer~versionedlayout~wave cxxstd=14 visibility=hidden ' + force_ac_on_macs) # Header only / req compiler on Apple for install to succeed.
    depends_on('cgal+header_only' + force_ac_on_macs, type='build')
    depends_on('ecbuild' + force_ac_on_macs, type='build')
    depends_on('eigen' + force_ac_on_macs, type='build')
    depends_on('gsl-lite' + force_ac_on_macs, type='build')
    depends_on('m4' + force_ac_on_macs, type='build')
    depends_on('perl' + force_ac_on_macs, type='build')

    depends_on('git' + force_ac_on_macs, type='run')
    depends_on('git-lfs' + force_ac_on_macs, type='run')
    depends_on('python@3.7.0:' + force_ac_on_macs, type=('build', 'link', 'run'))
    depends_on('szip')
    depends_on('zlib+optimize+pic+shared')
    depends_on('udunits', type=('build', 'link', 'run'))
    depends_on('gsl-lite' + force_ac_on_macs, type='build')

    # gsl-lite from above
    # mpi
    depends_on('hdf+szip+shared')
    depends_on('hdf5@1.12.0+hl+szip') # 1.12 needed for jedi. Make optional? C interface only. MPI.
    #depends_on('hdf-eos2') # Optional. szlib issue.
    #depends_on('hdf-eos5') # Optional. szlib issue.
    depends_on('parallel-netcdf')
    depends_on('netcdf-c@4.7.4+parallel-netcdf+hdf4') # DAP?
    depends_on('netcdf-fortran') # buggy on macos 10.11. Need Fortran compiler. MPI.
    depends_on('nccmp', type='run')
    # pio
    depends_on('eckit')
    depends_on('fckit')
    depends_on('atlas')
    depends_on('py-numpy')
    depends_on('py-pybind11')
    # bufr

    # lapack / openblas / mkl
    depends_on('blas')
    depends_on('lapack')


