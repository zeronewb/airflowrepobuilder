%{?scl:%scl_package python-jinja2}
%{!?scl:%global pkg_name %{name}}

%global srcname Jinja2

# Enable building without docs to avoid a circular dependency between this
# and python-sphinx:
%global with_docs 1

Name:		%{?scl_prefix}python-jinja2
Version:	2.8
Release:	0.2%{?dist}
Summary:	General purpose template engine
Group:		Development/Languages
License:	BSD
URL:		http://jinja.pocoo.org/
Source0:	https://pypi.python.org/packages/source/J/%{srcname}/%{srcname}-%{version}.tar.gz
# This patch consists of two upstream patches merged and rebased for 2.2.1
#  (the first upstream patch introduced CVE-2014-0012 and the second fixed it)
#  https://github.com/mitsuhiko/jinja2/commit/acb672b6a179567632e032f547582f30fa2f4aa7
#  https://github.com/mitsuhiko/jinja2/pull/296/files
#Patch0:         %{pkg_name}-fix-CVE-2014-1402.patch
BuildRoot:	%{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	%{?scl_prefix}python-devel
BuildRequires:	%{?scl_prefix}python-setuptools
BuildRequires:	%{?scl_prefix}python-markupsafe
%if 0%{?with_docs}
BuildRequires:	%{?scl_prefix}python-sphinx
%endif # with_docs
Requires:	%{?scl_prefix}python-babel >= 0.8
Requires:	%{?scl_prefix}python-markupsafe
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
Jinja2 is a template engine written in pure Python.  It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.

%prep
%setup -q -n %{srcname}-%{version}

# cleanup
find . -name '*.pyo' -o -name '*.pyc' -delete

#%patch0 -p0

# fix EOL
sed -i 's|\r$||g' LICENSE

%if 0%{?with_python3}
cp -a . %{py3dir}
%endif # with_python3


%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

# for now, we build docs using Python 2.x and use that for both
# packages.
%if 0%{?with_docs}
%{?scl:scl enable %{scl} "}
make -C docs html
%{?scl:"}
%endif # with_docs

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build \
	    --root %{buildroot}
%{?scl:"}

# remove hidden file
rm -rf docs/_build/html/.buildinfo

%clean
rm -rf %{buildroot}

#%check
#%{?scl:scl enable %{scl} "}
#make test
#%{?scl:"}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES LICENSE
%if 0%{?with_docs}
%doc docs/_build/html
%endif # with_docs
%doc ext
%doc examples
%{python_sitelib}/*
#%exclude %{python_sitelib}/jinja2/_debugsupport.c

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.8-0.2
- Update to 2.8
- Use srcname consistently
- Add python(abi) dependency

* Fri May 30 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.6-10
- Fix CVE-2014-1402
Resolves: rhbz#1102891

* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.6-9
- Rebuild to generate bytecode properly after fixing rhbz#956289

* Wed Oct 10 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.6-8
- Enable building with documentation, now for real.

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.6-7
- Enable building with documentation.

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.6-6
- Rebuilt for SCL.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.6-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 2.6-4
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.6-1
- Update to 2.6.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.5-3
- Re-enable html doc generation.
- Remove conditional for F-12 and below.
- Do not silently fail the testsuite for with py3k.

* Mon Nov  1 2010 Michel Salim <salimma@fedoraproject.org> - 2.5.5-2
- Move python3 runtime requirements to python3 subpackage

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.5-1
- Update to 2.5.5.

* Wed Aug 25 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.2-4
- Revert to previous behavior: fail the build on failed test.
- Rebuild for Python 3.2.

* Wed Aug 25 2010 Dan Horák <dan[at]danny.cz> - 2.5.2-3
- %%ifnarch doesn't work on noarch package so don't fail the build on failed tests

* Wed Aug 25 2010 Dan Horák <dan[at]danny.cz> - 2.5.2-2
- disable the testsuite on s390(x)

* Thu Aug 19 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.2-1
- Update to upstream version 2.5.2.
- Package depends on python-markupsafe and is noarch now.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.5-4
- add explicit build-requirement on python-setuptools
- fix doc disablement for python3 subpackage

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.5-3
- support disabling documentation in the build to break a circular build-time
dependency with python-sphinx; disable docs for now

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 13 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5-1
- Update to upstream version 2.5.
- Create python3 subpackage.
- Minor specfile fixes.
- Add examples directory.
- Thanks to Gareth Armstrong for additional hints.

* Wed Apr 21 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.4.1-1
- Update to 2.4.1.

* Tue Apr 13 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.4-1
- Update to 2.4.

* Tue Feb 23 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.1-1
- Update to 2.3.1.
- Docs are built using Sphinx now.
- Run the testsuite.

* Sat Sep 19 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1, mainly a bugfix release.
- Remove patch no longer needed.
- Remove conditional for FC-8.
- Compilation of speedup module has to be explicitly requested now.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.1-1
- Update to 2.1.1 (bugfix release).

* Thu Dec 18 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.1-1
- Update to 2.1, which fixes a number of bugs.
  See http://jinja.pocoo.org/2/documentation/changelog#version-2-1.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0-3
- Rebuild for Python 2.6

* Tue Jul 22 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-2
- Use rpm buildroot macro instead of RPM_BUILD_ROOT.

* Sun Jul 20 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-1
- Upstream released 2.0.

* Sun Jun 29 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-0.1.rc1
- Modified specfile from the existing python-jinja package.
