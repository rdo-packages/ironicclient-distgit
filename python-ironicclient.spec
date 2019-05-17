# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname ironicclient

%global common_desc A python and command line client library for Ironic

Name:           python-ironicclient
Version:        XXX
Release:        XXX
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-%{sname}
Source0:        https://tarballs.openstack.org/python-%{sname}/python-%{sname}-%{version}%{?milestone}.tar.gz
BuildArch:      noarch


%description
%{common_desc}


%package -n python%{pyver}-%{sname}
Summary:        Python client for Ironic
%{?python_provide:%python_provide python%{pyver}-%{sname}}
%if %{pyver} == 3
Obsoletes: python2-%{sname} < %{version}-%{release}
%endif

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr >= 2.0.0
BuildRequires:  python%{pyver}-setuptools

Requires:       genisoimage
Requires:       python%{pyver}-appdirs >= 1.3.0
Requires:       python%{pyver}-keystoneauth1 >= 3.4.0
Requires:       python%{pyver}-pbr >= 2.0.0
Requires:       python%{pyver}-prettytable
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-osc-lib >= 1.10.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-requests
# Handle python2 exception
%if %{pyver} == 2
Requires:       python-dogpile-cache >= 0.6.2
Requires:       python-jsonschema
Requires:       PyYAML
%else
Requires:       python%{pyver}-dogpile-cache >= 0.6.2
Requires:       python%{pyver}-jsonschema
Requires:       python%{pyver}-PyYAML
%endif

%description -n python%{pyver}-%{sname}
%{common_desc}

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{pyver_build}

%install
%{pyver_install}
# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s ironic %{buildroot}%{_bindir}/ironic-%{pyver}

%files -n python%{pyver}-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/ironic
%{_bindir}/ironic-%{pyver}
%{pyver_sitelib}/%{sname}*
%{pyver_sitelib}/python_%{sname}*

%changelog
