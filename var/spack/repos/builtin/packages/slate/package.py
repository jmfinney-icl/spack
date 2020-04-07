# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Slate(Package):
    """The Software for Linear Algebra Targeting Exascale (SLATE) project is
    to provide fundamental dense linear algebra capabilities to the US
    Department of Energy and to the high-performance computing (HPC) community
    at large. To this end, SLATE will provide basic dense matrix operations
    (e.g., matrix multiplication, rank-k update, triangular solve), linear
    systems solvers, least square solvers, singular value and eigenvalue
    solvers."""

    homepage = "https://icl.utk.edu/slate/"
    hg      = "https://bitbucket.org/icl/slate"
    maintainers = ['G-Ragghianti']

    version('develop', hg=hg)

    variant('test', default=False, description='Build testing routines')

    depends_on('cuda@9:')
    depends_on('mpi')
    depends_on('blaspp')
    depends_on('lapackpp')
    depends_on('testsweeper', when'+test')

    conflicts('%gcc@:5')

    def cmake_args(self):
        spec = self.spec
        cmake_args = [
            '-DSLATE_BUILD_TESTS={}'.format ('ON' if '+test' in spec else 'OFF'),
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix,
            '-DCMAKE_INSTALL_NAME_DIR:PATH=%s/lib' % self.prefix
        ]

        return cmake_args
