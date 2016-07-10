%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname ironicclient

%if 0%{?fedora}
%global with_python3 1
%endif

Name:       python-ironicclient
Version:    XXX
Release:    XXX
Summary:    Python client for Ironic
License:    ASL 2.0
URL:        https://bugs.launchpad.net/python-ironicclient
Source0:    http://tarballs.openstack.org/python-ironicclient/python-ironicclient-0.3.1.tar.gz

BuildArch:  noarch

%description
A python and command line client library for Ironic.

%package -n python2-%{sname}
Summary:    Python client for Ironic
%{?python_provide:%python_provide python2-{sname}}

BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-setuptools

Requires:    python-dogpile-cache
Requires:    python-keystoneauth1
Requires:    python-pbr
Requires:    python-prettytable
Requires:    python-six
Requires:    python-stevedore
Requires:    python-oslo-i18n
Requires:    python-oslo-utils
Requires:    python-cliff
Requires:    python-appdirs
Requires:    python-requests
Requires:    python-openstackclient

%description -n python2-%{sname}
A python and command line client library for Ironic.

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:    Python client for Ironic
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-setuptools

Requires:    python3-dogpile-cache
Requires:    python3-keystoneauth1
Requires:    python3-pbr
Requires:    python3-prettytable
Requires:    python3-six
Requires:    python3-stevedore
Requires:    python3-oslo-i18n
Requires:    python3-oslo-utils
Requires:    python3-cliff
Requires:    python3-appdirs
Requires:    python3-requests
Requires:    python3-openstackclient

%description -n python3-%{sname}
A python and command line client library for Ironic.
%endif

%package doc
Summary:    Documentation for OpenStack Ironic API Client

BuildRequires:    python-sphinx
BuildRequires:    python-oslo-sphinx

%description      doc
A python and command line client library for Ironic.

This package contains auto-generated documentation.

%prep
%setup -q -n %{name}-%{upstream_version}

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
# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/%{sname}/tests
%endif

%py2_install
mv %{buildroot}%{_bindir}/ironic %{buildroot}%{_bindir}/ironic-%{python2_version}
ln -s ./ironic-%{python2_version} %{buildroot}%{_bindir}/ironic-2

ln -s ./ironic-2 %{buildroot}%{_bindir}/ironic

# Delete tests
rm -fr %{buildroot}%{python2_sitelib}/%{sname}/tests


export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html


%files -n python2-%{sname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{sname}
%{python2_sitelib}/*.egg-info
%{_bindir}/ironic
%{_bindir}/ironic-2
%{_bindir}/ironic-%{python2_version}

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/*.egg-info
%{_bindir}/ironic-3
%{_bindir}/ironic-%{python3_version}
%endif

%files doc
%doc html
%license LICENSE

%changelog
