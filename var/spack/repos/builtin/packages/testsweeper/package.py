# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Testsweeper(CMakePackage):
    """Tool used by BLAS++, LAPACK++, and SLATE for performing sweeps
    across input parameters."""

    homepage = "https://bitbucket.org/icl/testsweeper"
    url      = "https://bitbucket.org/icl/testsweeper"

    # notify when the package is updated.
    maintainers = ['jmfinney-icl']

    # Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('develop', hg=url)

    def cmake_args(self):
        spec = self.spec
        cmake_args = [
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix,
            '-DCMAKE_INSTALL_NAME_DIR:PATH=%s/lib' % self.prefix
        ]

        return cmake_args
