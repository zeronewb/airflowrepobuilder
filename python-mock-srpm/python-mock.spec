%{?scl:%scl_package python-mock}
%{!?scl:%global pkg_name %{name}}

%global mod_name mock

Name: %{?scl_prefix}python-mock
Version:        0.8.0
Release:        0.1%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

Group:          Development/Libraries
License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        http://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%prep
%setup -q -n %{mod_name}-%{version}
cp -p %{SOURCE1} .

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
%doc LICENSE.txt README.txt
%doc docs/
%{python_sitelib}/*.egg-info
%{python_sitelib}/%{mod_name}.py*

%changelog
* Tue Nov 24 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0,8.0-0.1
- Update to python27 build

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.8.0-2
- Python3 support

* Thu Mar 22 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8.0-1
- Updated to new version

* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.2-1
- Initial RPM release