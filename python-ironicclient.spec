%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-ironicclient
Version:        1.2.0
Release:        2%{?dist}
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-ironicclient
Source0:        http://tarballs.openstack.org/python-ironicclient/python-ironicclient-%{version}%{?milestone}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr >= 1.6
BuildRequires:  python-setuptools

Requires:       python-anyjson
Requires:       python-appdirs >= 1.3.0
Requires:       python-cliff
Requires:       python-dogpile-cache >= 0.5.7
Requires:       python-httplib2
Requires:       python-openstackclient >= 2.1.0
Requires:       python-keystoneauth1 >= 2.1.0
Requires:       python-lxml
Requires:       python-pbr >= 1.6
Requires:       python-prettytable
Requires:       python-six >= 1.9.0
Requires:       python-stevedore
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-utils >= 3.5.0


%description
A python and command line client library for Ironic.

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

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
* Fri Apr 15 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.2.0-2
- Fix dependencies

* Wed Mar 23 2016 RDO <rdo-list@redhat.com> 1.2.0-0.1
-  Rebuild for Mitaka
