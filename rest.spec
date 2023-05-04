#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : rest
Version  : 0.9.1
Release  : 28
URL      : https://download.gnome.org/sources/rest/0.9/rest-0.9.1.tar.xz
Source0  : https://download.gnome.org/sources/rest/0.9/rest-0.9.1.tar.xz
Summary  : RESTful web api query library
Group    : Development/Tools
License  : LGPL-2.1
Requires: rest-bin = %{version}-%{release}
Requires: rest-data = %{version}-%{release}
Requires: rest-lib = %{version}-%{release}
Requires: rest-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : ca-certs
BuildRequires : gobject-introspection-dev
BuildRequires : json-glib-dev
BuildRequires : pkgconfig(gtksourceview-5)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libsoup-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# librest
This library has been designed to make it easier to access web services that
claim to be "RESTful". A reasonable definition of what this means can be found
on [Wikipedia][1]. However a reasonable description is that a RESTful service
should have urls that represent remote objects which methods can then be
called on.

%package bin
Summary: bin components for the rest package.
Group: Binaries
Requires: rest-data = %{version}-%{release}
Requires: rest-license = %{version}-%{release}

%description bin
bin components for the rest package.


%package data
Summary: data components for the rest package.
Group: Data

%description data
data components for the rest package.


%package dev
Summary: dev components for the rest package.
Group: Development
Requires: rest-lib = %{version}-%{release}
Requires: rest-bin = %{version}-%{release}
Requires: rest-data = %{version}-%{release}
Provides: rest-devel = %{version}-%{release}
Requires: rest = %{version}-%{release}

%description dev
dev components for the rest package.


%package lib
Summary: lib components for the rest package.
Group: Libraries
Requires: rest-data = %{version}-%{release}
Requires: rest-license = %{version}-%{release}

%description lib
lib components for the rest package.


%package license
Summary: license components for the rest package.
Group: Default

%description license
license components for the rest package.


%prep
%setup -q -n rest-0.9.1
cd %{_builddir}/rest-0.9.1
pushd ..
cp -a rest-0.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683227738
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dca_certificates_path=/var/cache/ca-certs/compat/ca-roots.pem \
-Dgtk_doc=false  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dca_certificates_path=/var/cache/ca-certs/compat/ca-roots.pem \
-Dgtk_doc=false  builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/rest
cp %{_builddir}/rest-%{version}/COPYING %{buildroot}/usr/share/package-licenses/rest/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/librest-demo
/usr/bin/librest-demo

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Rest-1.0.typelib
/usr/lib64/girepository-1.0/RestExtras-1.0.typelib
/usr/share/applications/org.gnome.RestDemo.desktop
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/librest-1.0.so
/V3/usr/lib64/librest-extras-1.0.so
/usr/include/rest-1.0/rest-extras/flickr-proxy-call.h
/usr/include/rest-1.0/rest-extras/flickr-proxy.h
/usr/include/rest-1.0/rest-extras/lastfm-proxy-call.h
/usr/include/rest-1.0/rest-extras/lastfm-proxy.h
/usr/include/rest-1.0/rest-extras/youtube-proxy.h
/usr/include/rest-1.0/rest/rest-enum-types.h
/usr/include/rest-1.0/rest/rest-oauth2-proxy-call.h
/usr/include/rest-1.0/rest/rest-oauth2-proxy.h
/usr/include/rest-1.0/rest/rest-param.h
/usr/include/rest-1.0/rest/rest-params.h
/usr/include/rest-1.0/rest/rest-pkce-code-challenge.h
/usr/include/rest-1.0/rest/rest-proxy-auth.h
/usr/include/rest-1.0/rest/rest-proxy-call.h
/usr/include/rest-1.0/rest/rest-proxy.h
/usr/include/rest-1.0/rest/rest-utils.h
/usr/include/rest-1.0/rest/rest-xml-node.h
/usr/include/rest-1.0/rest/rest-xml-parser.h
/usr/include/rest-1.0/rest/rest.h
/usr/lib64/librest-1.0.so
/usr/lib64/librest-extras-1.0.so
/usr/lib64/pkgconfig/rest-1.0.pc
/usr/lib64/pkgconfig/rest-extras-1.0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/librest-1.0.so.0
/V3/usr/lib64/librest-1.0.so.0.0.0
/V3/usr/lib64/librest-extras-1.0.so.0
/V3/usr/lib64/librest-extras-1.0.so.0.0.0
/usr/lib64/librest-1.0.so.0
/usr/lib64/librest-1.0.so.0.0.0
/usr/lib64/librest-extras-1.0.so.0
/usr/lib64/librest-extras-1.0.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rest/9a1929f4700d2407c70b507b3b2aaf6226a9543c
