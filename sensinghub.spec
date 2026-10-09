%global prj_name    sensinghub
%global debug_package %{nil}

Name:           qcom-sensing-hub
Version:        2.2.3
Release:        2%{?dist}
Summary:        Qualcomm Sensing-hub APIs Library
License:        BSD-3-Clause
URL:		    https://github.com/qualcomm/sensinghub
Source0:	    %{url}/archive/v%{version}/%{prj_name}-%{version}.tar.gz
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
BuildRequires:  nanopb-generator
BuildRequires:  python3-protobuf 

%description
Qualcomm Sensing Hub (QSH) is an always-on, low-power interface designed to
collect, process, and combine sensor and contextual data. It offers stable APIs
that enable applications and services to interact with the hub efficiently,
reducing the need for frequent application processor wake ups.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup -n %{prj_name}-%{version}

%build
autoreconf -fi
%configure \
    CFLAGS="%{optflags} -I%{_includedir}/nanopb" \
    CXXFLAGS="%{optflags} -I%{_includedir}/nanopb" \
    CPPFLAGS="%{optflags} -I%{_includedir}/nanopb"

%install
%make_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib*.so.*
%{_bindir}/*
%{_sysconfdir}/sensors/proto

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Sun Sep 27 2026 Mritunjoy Das <mmritunj@qti.qualcomm.com> - 2.2.3-2
- Initial RPM Build for sensing hub, imported from fedora package
