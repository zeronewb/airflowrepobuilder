%{?scl:%scl_package python-backports_abc}
%{!?scl:%global pkg_name %{name}}

%global srcname backports_abc

%define name backports_abc

Summary: A backport of recent additions to the 'collections.abc' module.
Name: %{?scl_prefix}python-backports_abc
Version: 0.4
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
License: Python
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Stefan Behnel et al. <cython-devel@python.org>
Url: https://github.com/cython/backports_abc
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
=============
ABC-Backports
=============

Usage:

.. code-block:: python

    try:
        # ABCs live in "collections.abc" in Python >= 3.3
        from collections.abc import Coroutine, Generator
    except ImportError:
        # fall back to import from "backports_abc"
        from backports_abc import Coroutine, Generator

You can also install the ABCs into the stdlib by calling the ``patch()``
function:

.. code-block:: python

    import backports_abc
    backports_abc.patch()

    try:
        # ABCs live in "collections.abc" in Python >= 3.3
        from collections.abc import Coroutine, Generator
    except ImportError:
        # fall back to import from "collections" in Python <= 3.2
        from backports_abc import Coroutine, Generator

Currently, ``patch()`` provides the following names if missing:

* ``collections.abc.Generator``
* ``collections.abc.Awaitable``
* ``collections.abc.Coroutine``
* ``inspect.isawaitable(obj)``

All of them are also available directly from the ``backports_abc``
module namespace.

In Python 2.x and Python 3.2, it patches the ``collections`` module
instead of the ``collections.abc`` module.  Any names that are already
available when importing this module will not be overwritten.

The names that were previously patched by ``patch()`` can be queried
through the mapping in ``backports_abc.PATCHED``.

Changelog
=========

0.4 (2015-09-14)
----------------

* direct wheel building support

* make all names available at the module level instead of requiring patching


0.3 (2015-07-03)
----------------

* removed patching of ``inspect.iscoroutine()`` as it is not ABC based


0.2 (2015-07-03)
----------------

* require explicit ``backports_abc.patch()`` call to do the patching
  (avoids side-effects on import and allows future configuration)

* provide access to patched names through global ``PATCHED`` dict

* add ABC based implementations of inspect.iscoroutine() and
  inspect.isawaitable()


0.1 (2015-06-24)
----------------

* initial public release

* provided ABCs: Generator, Coroutine, Awaitable


%prep
%setup -n %{srcname}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc CHANGES.rst README.rst
#%doc build/*

%changelog
* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.4-0.1
- Activate python2.7 build and dependenies
- Add python(abi) dependency
