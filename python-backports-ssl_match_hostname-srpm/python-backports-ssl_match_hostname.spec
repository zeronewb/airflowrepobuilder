#
# spec file for package python-backports.ssl_match_hostname
#
# Copyright (c) 2015 Nico Kadel-Garcia.
#

%{?scl:%scl_package python-backports-ssl_match_hostname}
%{!?scl:%global pkg_name %{name}}

%global srcname backports.ssl_match_hostname

# CentOS "extras" renames this oddly
Name: %{?scl_prefix}python-backports-ssl_match_hostname

Version:        3.4.0.2
Release:        0.2%{?dist}
Url:            http://bitbucket.org/brandon/backports.ssl_match_hostname
Summary:        The ssl.match_hostname() function from Python 3.4
License:        Python Software Foundation
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}
Obsoletes: %{?scl_prefix}python-backports.ssl_match_hostname < %{verson}-%{release}
Obsoletes: %{?scl_prefix}python-backports.ssl_match_hostname < %{verson}-%{release}

%description
The Secure Sockets layer is only actually *secure*
if you check the hostname in the certificate returned
by the server to which you are connecting,
and verify that it matches to hostname
that you are trying to reach.

But the matching logic, defined in `RFC2818`_,
can be a bit tricky to implement on your own.
So the ``ssl`` package in the Standard Library of Python 3.2
and greater now includes a ``match_hostname()`` function
for performing this check instead of requiring every application
to implement the check separately.

This backport brings ``match_hostname()`` to users
of earlier versions of Python.
Simply make this distribution a dependency of your package,
and then use it like this::

    from backports.ssl_match_hostname import match_hostname, CertificateError
    ...
    sslsock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv3,
                              cert_reqs=ssl.CERT_REQUIRED, ca_certs=...)
    try:
        match_hostname(sslsock.getpeercert(), hostname)
    except CertificateError, ce:
        ...

Note that the ``ssl`` module is only included in the Standard Library
for Python 2.6 and later;
users of Python 2.5 or earlier versions
will also need to install the ``ssl`` distribution
from the Python Package Index to use code like that shown above.

Brandon Craig Rhodes is merely the packager of this distribution;
the actual code inside comes verbatim from Python 3.4.

History
-------
* This function was introduced in python-3.2
* It was updated for python-3.4a1 for a CVE 
  (backports-ssl_match_hostname-3.4.0.1)
* It was updated from RFC2818 to RFC 6125 compliance in order to fix another
  security flaw for python-3.3.3 and python-3.4a5
  (backports-ssl_match_hostname-3.4.0.2)


.. _RFC2818: http://tools.ietf.org/html/rfc2818.html

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
# Clear unnecessary "backports" module overlaps
rm -f %{buildroot}%{python_sitelib}/backports/__init__.py*


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
* Mon Dec  7 2015 - Nico Kadel-Garcia <nkadel@skyhookwireless.com>
- Build .spec file from py2pack
- Rename to python-backports-ssl_match_hostname based name, too match CentOS
