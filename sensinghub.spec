%global prj_name    sensinghub
%global debug_package %{nil}

Name:           qcom-sensing-hub
Version:        2.2.3
Release:        %autorelease
Summary:        Qualcomm Sensing-hub APIs Library

License:        BSD-3-Clause

URL:		    https://github.com/qualcomm/sensinghub
Source0:		%{url}/archive/v%{version}/%{prj_name}-%{version}.tar.gz

ExclusiveArch:  %{arm64}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  nanopb
BuildRequires:  nanopb-devel
BuildRequires:  python3-protobuf 

%description
Qualcomm Sensing-hub APIs Library.

%package devel
Summary:        Qualcomm Sensing-hub APIs Library dev package
Requires:       %{name}%{?_isa} = %{version}-%{release}

# Debian Replaces/Breaks: libsensinghub-dev
Obsoletes:      libsensinghub-dev < %{version}-%{release}
Conflicts:      libsensinghub-dev

%description devel
Qualcomm Sensing-hub headers & libraries

# Debian Replaces/Breaks: libsensinghub1 (applies to the base package)
Obsoletes:      libsensinghub1 < %{version}-%{release}
Conflicts:      libsensinghub1

%prep
%autosetup -n %{prj_name}-%{version}

%build
autoreconf -fi
%configure \
	CFLAGS="%{optflags} -I%{_includedir}/nanopb" \
	CXXFLAGS="%{optflags} -I%{_includedir}/nanopb" \
	CPPFLAGS="-I%{_includedir}/nanopb"

%make_build LDFLAGS="-lprotobuf-nanopb"

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files
%{_libdir}/lib*.so.*
%{_bindir}/*
%{_sysconfdir}/sensors/proto

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Wed Nov 19 2025 Bhanu Vivek Matsa <bmasta@qti.qualcomm.com> - 1.0.2-1
- Add operator override in suid

* Mon Aug 11 2025 Bhanu Vivek Matsa <bmasta@qti.qualcomm.com> - 1.0.1-1
- debian : Fixed the debs compilation error
- Added not installed file for package
- Versioned the shared libs generated

* Tue Jun 17 2025 Bhanu Vivek Matsa <quic_bmasta@quicinc.com> - 1.0.0-1
- Initial release.
