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
    version('1.16.3', commit='64318b81bf3ba2afd78a592e6535d71e0b2dfd7f', preferred=True)
    version('1.16.2', commit='1857de5b1eab9fb24fd7c6d56f8954506315247a')
    version('1.16.1', commit='282cd626fc4e95d8a3dace8e051e84f30accc483')
    version('1.15.11', commit='230786462aeb8e55f4c2f9745ed6f499d532ce0b')
    version('1.13.2', commit='2732c966cdeb46c5dc4d3644f373f27bdc839bf8')
    version('1.12.1', commit='71e727bab888721c3cb2a5a1e2d3ae6cf31956ac')
    version('1.11.6', commit='f8b7c5776863bae003b9d85b592efe61175dbbd3')
    version('1.10.2', commit='77e462800336ff2c2cb0dc5c4bbbb3f231bd4d86')

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
        return res

