Summary:	A Python 3D plotting and mesh analysis library
Name:		python-pyvista
Version:	0.44.1
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/pyvista/pyvista
#Source0:	https://github.com/pyvista/pyvista/archive/refs/tags/v%{version}/pyvista-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/p/pyvista/pyvista-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

# (mandian) python-vtk does not provide python%{py_ver}dist(vtk)
%global __requires_exclude  ^python%{pyver}dist\\(vtk\\)$
Requires:	python-vtk

BuildArch:	noarch

%description
PyVista is:
  - Pythonic VTK: a high-level API to the Visualization Toolkit (VTK)
  - mesh data structures and filtering methods for spatial datasets
  - 3D plotting made simple and built for large/complex data geometries

PyVista is a helper module for the Visualization Toolkit (VTK) that wraps the
VTK library through NumPy and direct array access through a variety of methods
and classes. This package provides a Pythonic, well-documented interface
exposing VTK's powerful visualization backend to facilitate rapid prototyping,
analysis, and visual integration of spatially referenced datasets.

This module can be used for scientific plotting for presentations and research
papers as well as a supporting module for other mesh 3D rendering dependent
Python modules.


This module takes a surface mesh and returns a uniformly meshed surface using
voronoi clustering. This approach is loosely based on research by S. Valette,
and J. M. Chassery in ACVD.

%files
%license LICENSE
%doc README.rst
%{py_sitedir}/pyvista/
%{py_sitedir}/pyvista*-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n pyvista-%{version}

#FIXME: omlx python-vtk doesn't provide python3dist(vtk)
sed -i -e "/  'vtk',/d" setup.py

%build
%py_build

%install
%py_install

