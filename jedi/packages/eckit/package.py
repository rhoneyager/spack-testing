# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
from spack import *

class Eckit(CMakePackage):
    """A C++ toolkit that supports development of tools and applications at ECMWF."""

    homepage = "https://software.ecmwf.int/wiki/display/eckit"
    git = "https://github.com/ecmwf/eckit.git"
    url = "https://github.com/ecmwf/eckit/archive/1.11.6.tar.gz"

    maintainers = ['rhoneyager', 'mmiesch']

    version('release-stable', branch='release-stable')
    version('develop', branch='develop')
    version('1.13.2', commit='2732c966cdeb46c5dc4d3644f373f27bdc839bf8')
    version('1.13.0', commit='8464759a7ea15b27768d0db460a275028b98d3fd')
    version('1.12.1', commit='71e727bab888721c3cb2a5a1e2d3ae6cf31956ac')
    version('1.12.0', commit='60f1fe5a83903066fd8d6a06373db29bf691c864')
    version('1.11.6', commit='f8b7c5776863bae003b9d85b592efe61175dbbd3')
    version('1.11.5', commit='13edada4c0a4e8f7ae0cb93ebcd25ddd9a359cdc')
    version('1.11.4', commit='74564a7afba384a73f9f366001953413c51cc522')
    version('1.11.3', commit='0373e0fd2192ea1a85c607bd0213dda7fc1cf7c5')
    version('1.11.2', commit='f55b7f781aa8f616415b7ef8988d2c52837e48e0')
    version('1.11.1', commit='bb4b33d8a3a4d8f0c928ea65dbebd5cacb397edd')
    version('1.10.2', commit='77e462800336ff2c2cb0dc5c4bbbb3f231bd4d86')

    #depends_on('cmake @3.10:', type=('build', 'run', 'link'))
    depends_on('ecbuild', type=('build'))

    depends_on('perl@5:')
    depends_on('mpi')
    depends_on('eigen')

    variant('lapack', default=False)
    depends_on('netlib-lapack', when='+lapack')

    variant('blas', default=False)
    depends_on('openblas', when='+blas')

    variant('mkl', default=False)
    depends_on('intel-mkl', when='+mkl')

    variant('git', default=False)
    depends_on('git', when='+git')

    variant('curses', default=True)
    depends_on('ncurses', when='+curses')

    variant('bzip2', default=False)
    depends_on('bzip2', when='+bzip2')
    variant('lz4', default=False)
    depends_on('lz4', when='+lz4')
    variant('openssl', default=False)
    depends_on('openssl', when='+openssl')
    variant('xxhash', default=False)
    depends_on('xxhash', when='+xxhash')
    variant('curl', default=False)
    depends_on('curl', when='+curl')
    variant('aio', default=False)
    depends_on('libaio', when='+aio')
    variant('rsync', default=False)
    depends_on('rsync', when='+rsync')
    variant('armadillo', default=False)
    depends_on('armadillo', when='+armadillo')
    variant('doxygen', default=False)
    depends_on('doxygen', when='+doxygen')
    variant('bison', default=False)
    depends_on('bison', when='+bison')
    variant('flex', default=False)
    depends_on('flex', when='+flex')
    variant('aec', default=False)
    depends_on('libaec', when='+aec')
    variant('snappy', default=False)
    depends_on('snappy', when='+snappy')

    # PkgConfig?
    # CMath?
    # Realtime?
    # Threads?

    def cmake_args(self):
        res = [
                self.define_from_variant('ENABLE_AEC', 'aec'),
                self.define_from_variant('ENABLE_AIO', 'aio'),
                self.define_from_variant('ENABLE_ARMADILLO', 'armadillo'),
                self.define('ENABLE_BUILD_TOOLS', True),
                self.define_from_variant('ENABLE_BZIP2', 'bzip2'),
                self.define('ENABLE_CUDA', False),
                self.define_from_variant('ENABLE_CURL', 'curl'),
                self.define_from_variant('ENABLE_DOCS', 'doxygen'),
                self.define('ENABLE_EIGEN', True),
                self.define_from_variant('ENABLE_LAPACK', 'lapack'),
                self.define_from_variant('ENABLE_LZ4', 'lz4'),
                self.define('ENABLE_MPI', True),
                self.define_from_variant('ENABLE_RSYNC', 'rsync'),
                self.define_from_variant('ENABLE_SNAPPY', 'snappy'),
                self.define_from_variant('ENABLE_SSL', 'openssl'),
                self.define_from_variant('ENABLE_XXHASH', 'xxhash')
                ] 
        res.append('-DCMAKE_MODULE_PATH=' + self.spec['ecbuild'].prefix + '/share/ecbuild/cmake')
        return res

