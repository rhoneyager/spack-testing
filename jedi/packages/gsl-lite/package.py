# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class GslLite(CMakePackage):
    """gsl-lite – A single-file header-only version of ISO C++ Guidelines Support Library (GSL) for C++98, C++11, and later"""
    homepage = "https://github.com/gsl-lite/gsl-lite"
    git = "https://github.com/gsl-lite/gsl-lite.git"
    url = "https://github.com/gsl-lite/gsl-lite/archive/0.37.0.zip"

    version('0.37.0', commit='4b796627ad0fa42640f5fdb96f23c4a0d9ee084f')
    version('0.34.0', commit='93607223a48621dae3cedd6b3335431b38067fae')


