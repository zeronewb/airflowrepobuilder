%{?scl:%scl_package python-ldap3}
%{!?scl:%global pkg_name %{name}}

%define srcname ldap3

Summary: A strictly RFC 4510 conforming LDAP V3 pure Python client. Same codebase for Python 2, Python3, PyPy and PyPy 3
Name: %{?scl_prefix}python-ldap3
Version: 0.9.9.3
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: LGPL v3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Giovanni Cannata <cannatag@gmail.com>
Url: https://github.com/cannatag/ldap3
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
LDAP3
=====

.. image:: https://img.shields.io/pypi/v/ldap3.svg
    :target: https://pypi.python.org/pypi/ldap3/
    :alt: Latest Version

.. image:: https://img.shields.io/travis/cannatag/ldap3/master.svg
    :target: https://travis-ci.org/cannatag/ldap3
    :alt: TRAVIS-CI build status for master branch

.. image:: https://img.shields.io/pypi/l/ldap3.svg
    :target: https://pypi.python.org/pypi/ldap3/
    :alt: License

ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python **client**. The same codebase works with Python, Python 3, PyPy and PyPy3.

This project was formerly named **python3-ldap**. The name has been changed to avoid confusion with the python-ldap library.

Home Page
---------

Project home page is https://github.com/cannatag/ldap3


Documentation
-------------

Documentation is available at http://ldap3.readthedocs.org


License
-------

The ldap3 project is open source software released under the **LGPL v3 license**.


PEP8 Compliance
---------------

ldap3 is PEP8 compliant, except for line length.


Download
--------

Package download is available at https://pypi.python.org/pypi/ldap3.


Install
-------

Install with **pip install ldap3**


Git repository
--------------

You can download the latest source at https://github.com/cannatag/ldap3


Continuous integration
----------------------

Continuous integration for testing is at https://travis-ci.org/cannatag/ldap3

Support
-------

You can submit support tickets on https://github.com/cannatag/ldap3/issues/new


Thanks to
---------

* **Ilya Etingof**, the author of the *pyasn1* package for his excellent work and support.
* **Mark Lutz** for his *Learning Python* and *Programming Python* excellent books series and **John Goerzen** and **Brandon Rhodes** for their book *Foundations of Python Network Programming*. These books are wonderful tools for learning Python and this project owes a lot to them.
* **JetBrains** for donating to this project the Open Source license of *PyCharm 3 Professional*.
* **GitHub** for providing the *free source repository space and the tools* I use to develop this project.
* The **Python Software Foundation** for providing support for the test lab infrastructure.


Contact me
----------

For information and suggestions you can contact me at cannatag@gmail.com or you can also a support ticket on https://github.com/cannatag/ldap3/issues/new


Changelog
---------

You can read the current changelog at http://ldap3.readthedocs.org/changelog.html


%prep
%setup -q -n %{srcname}-%{version}

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
%doc COPYING.LESSER.txt COPYING.txt LICENSE.txt README.rst
#%doc build/*

%changelog
* Tue Dec  1 2015  Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.9.9.3
- Build SRPM from setup.py
- Activate python2.7 build and dependenies
