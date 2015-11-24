%{?scl:%scl_package python-snakebite}
%{!?scl:%global pkg_name %{name}}

%global srcname snakebite

Summary: Pure Python HDFS client
Name: %{?scl_prefix}python-snakebite
Version: 2.7.2
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Wouter de Bie <wouter@spotify.com>
Url: http://github.com/spotify/snakebite
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
UNKNOWN

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
# Move bash completion file to standard bash location
mv %{?_scl_root}/usr/etc/bash_completion.d/snakebite-completion.bash \
    %{?_scl_root}/etc/bash_completion.d/snakebite-completion.bash

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
# Extra shell configuration file
%{?_scl_root}/etc/bash_completion.d/snakebite-completion.bash
# Misinstalled LICENSE file, rely on doc below
%exclude %{_prefix}/LICENSE
%doc LICENSE
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.7.2-0.1
- Build SRPM with setup.py
- Modify for python27  build
- Handle bash_completion.d file and spurious LICENSE file

