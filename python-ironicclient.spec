%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora}
%global with_python3 1
%endif

%global sname ironicclient

Name:           python-ironicclient
Version:        1.11.2
Release:        1%{?dist}
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-ironicclient
Source0:        https://tarballs.openstack.org/python-ironicclient/python-ironicclient-%{version}%{?milestone}.tar.gz
BuildArch:      noarch


%description
A python and command line client library for Ironic.


%package -n python2-%{sname}
Summary:        Python client for Ironic

BuildRequires:  python2-devel
BuildRequires:  python-pbr >= 1.6
BuildRequires:  python-setuptools

Requires:       python-anyjson
Requires:       python-appdirs >= 1.3.0
Requires:       python-dogpile-cache >= 0.6.2
Requires:       python-httplib2
Requires:       python-jsonschema
Requires:       python-openstackclient >= 3.3.0
Requires:       python-keystoneauth1 >= 2.18.0
Requires:       python-lxml
Requires:       python-pbr >= 1.8
Requires:       python-prettytable
Requires:       python-six >= 1.9.0
Requires:       python-stevedore
Requires:       python-osc-lib >= 1.2.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-utils >= 3.18.0
Requires:       python-requests
Requires:       PyYAML

%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname}
A python and command line client library for Ironic


%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:        Python client for Ironic

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 1.8
BuildRequires:  python3-setuptools

Requires:       python3-anyjson
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-dogpile-cache >= 0.6.2
Requires:       python3-httplib2
Requires:       python3-jsonschema
Requires:       python3-openstackclient >= 3.3.0
Requires:       python3-keystoneauth1 >= 2.18.0
Requires:       python3-lxml
Requires:       python3-pbr >= 1.6
Requires:       python3-prettytable
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore
Requires:       python3-osc-lib >= 1.2.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-serialization >= 1.10.0
Requires:       python3-oslo-utils >= 3.18.0
Requires:       python3-requests
Requires:       python3-PyYAML

%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
A python and command line client library for Ironic
%endif

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/ironic %{buildroot}%{_bindir}/ironic-%{python3_version}
ln -s ./ironic-%{python3_version} %{buildroot}%{_bindir}/ironic-3
%endif

%py2_install
mv %{buildroot}%{_bindir}/ironic %{buildroot}%{_bindir}/ironic-%{python2_version}
ln -s ./ironic-%{python2_version} %{buildroot}%{_bindir}/ironic-2

ln -s ./ironic-2 %{buildroot}%{_bindir}/ironic


%files -n python2-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/ironic
%{_bindir}/ironic-2
%{_bindir}/ironic-%{python2_version}
%{python2_sitelib}/ironicclient*
%{python2_sitelib}/python_ironicclient*

%if 0%{?with_python3}
%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/ironic-3
%{_bindir}/ironic-%{python3_version}
%{python3_sitelib}/ironicclient*
%{python3_sitelib}/python_ironicclient*
%endif


%changelog
* Wed Sep 27 2017 rdo-trunk <javier.pena@redhat.com> 1.11.2-1
- Update to 1.11.2

* Thu Mar 16 2017 Alfredo Moralejo <amoralej@redhat.com> 1.11.1-1
- Update to 1.11.1

* Wed Feb 08 2017 Alfredo Moralejo <amoralej@redhat.com> 1.11.0-1
- Update to 1.11.0

