# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-jinja2
Epoch: 100
Version: 2.12.3
Release: 1%{?dist}
BuildArch: noarch
Summary: General purpose template engine for python3
License: BSD-3-Clause
URL: https://github.com/pallets/jinja/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-Jinja2
Summary: General purpose template engine for python3
Requires: python3
Requires: python3-MarkupSafe >= 0.23
Provides: python3-Jinja2 = %{epoch}:%{version}-%{release}
Provides: python3dist(Jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-Jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(Jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-Jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(Jinja2) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Jinja2
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%files -n python%{python3_version_nodots}-Jinja2
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-Jinja2
Summary: General purpose template engine for python3
Requires: python3
Requires: python3-MarkupSafe >= 0.23
Provides: python3-Jinja2 = %{epoch}:%{version}-%{release}
Provides: python3dist(Jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-Jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(Jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-Jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(Jinja2) = %{epoch}:%{version}-%{release}

%description -n python3-Jinja2
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%files -n python3-Jinja2
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-jinja2
Summary: General purpose template engine for python3
Requires: python3
Requires: python3-markupsafe >= 0.23
Provides: python3-jinja2 = %{epoch}:%{version}-%{release}
Provides: python3dist(jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jinja2) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-jinja2
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%files -n python%{python3_version_nodots}-jinja2
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?rhel} == 7)
%package -n python3-jinja2
Summary: General purpose template engine for python3
Requires: python3
Requires: python3-markupsafe >= 0.23
Provides: python3-jinja2 = %{epoch}:%{version}-%{release}
Provides: python3dist(jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jinja2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jinja2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jinja2) = %{epoch}:%{version}-%{release}

%description -n python3-jinja2
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%files -n python3-jinja2
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog
