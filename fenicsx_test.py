import numpy as np
import ufl
from mpi4py import MPI
from dolfinx import mesh, fem

# Create mesh and function space
domain = mesh.create_unit_square(MPI.COMM_WORLD, 8, 8)
V = fem.FunctionSpace(domain, ("Lagrange", 1))

# Define and evaluate a simple expression
u = fem.Function(V)
u.interpolate(lambda x: np.sin(np.pi * x[0]) * np.sin(np.pi * x[1]))

if domain.comm.rank == 0:
    print("✅ Test passed: function space and interpolation succeeded.")
