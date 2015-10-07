%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		python-ironicclient
Version:	0.8.1
Release:	1%{?dist}
Summary:	Python client for Ironic

License:	ASL 2.0
URL:		https://pypi.python.org/pypi/python-ironicclient
Source0:	http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz


BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-setuptools

Requires:	python-pbr
Requires:	python-prettytable
Requires:	python-keystoneclient
Requires:	python-six
Requires:	python-stevedore
Requires:	python-keystoneclient
Requires:	python-lxml
Requires:	python-pbr
Requires:	python-prettytable
Requires:	python-six
Requires:	python-stevedore
Requires:	python-oslo-i18n
Requires:	python-oslo-utils
Requires:	python-anyjson
Requires:	python-appdirs
Requires:	python-dogpile-cache
Requires:	python-httplib2


%description
A python and command line client library for Ironic.

%prep
%setup -q -n %{name}-%{version}

# Let RPM handle the requirements
rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE README.rst
%{_bindir}/*
%{python2_sitelib}/ironicclient*
%{python2_sitelib}/python_ironicclient*


%changelog
* Wed Oct 07 2015 Alan Pevec <alan.pevec@redhat.com> 0.8.1-1
- Update to upstream 0.8.1

* Wed Jun 24 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.3.1-3
- Cleanup spec
- Drop unneeded patches

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild


* Thu Oct 16 2014 Angus Thomas <athomas@redhat.com> - 0.3.1-1
- Rebased to python-ironicclient-0.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-5
- Removed instance of macro in Changelog
- Consistent use of tabs in SPEC file

* Thu Feb 27 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-4
- Switched to patches made with git
- Write REDHATIRONICCLIENTVERSION correctly
- Reordered files section

* Thu Feb 27 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-3
- Added macro fix to support building on EL6

* Wed Feb 26 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-2
- Added patches to remove pbr dependency
- Updated the source URL
- Removed deletion of python_ironicclient.egg-info

* Tue Feb 25 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-1
- Initial package.
