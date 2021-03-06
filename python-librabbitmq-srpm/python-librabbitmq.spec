%{?scl:%scl_package python-librabbitmq}
%{!?scl:%global pkg_name %{name}}

%global srcname librabbitmq

Summary: AMQP Client using the rabbitmq-c library.
Name: %{?scl_prefix}python-librabbitmq
Version: 1.6.1
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
License: MPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Ask Solem <ask@celeryproject.org>
Url: http://github.com/celery/librabbitmq
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
#Requires: amqp >= 1.4.6
Requires: %{?scl_prefix}python-amqp >= 1.4.6
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
================================================================
 librabbitmq - Python AMQP Client using the rabbitmq-c library.
================================================================

:Version: 1.6.0
:Download: http://pypi.python.org/pypi/librabbitmq/
:Code: http://github.com/celery/librabbitmq/
:Keywords: rabbitmq, amqp, messaging, librabbitmq, rabbitmq-c, python,
           kombu, celery

.. contents::
    :local:

Python bindings to the RabbitMQ C-library `rabbitmq-c`_.
Supported by Kombu and Celery.

%prep
%setup -n %{srcname}-%{version}

%build
#env CFLAGS="$RPM_OPT_FLAGS" python setup.py build
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
%{python_sitearch}/*
%exclude %{python_sitearch}/funtests
#%{python_sitelib}/*
%doc AUTHORS Changelog LICENSE-GPL-2.0 LICENSE-MPL-RabbitMQ README.rst TODO
#%doc build/*

%changelog
* Mon Nov 24 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.6.10-01
- Provide full URL for source
- Activate python2.7 build and dependenies
- Exclude funtests, which comes from python-billiards

