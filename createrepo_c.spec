#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : createrepo_c
Version  : 0.17.6
Release  : 67
URL      : https://github.com/rpm-software-management/createrepo_c/archive/0.17.6/createrepo_c-0.17.6.tar.gz
Source0  : https://github.com/rpm-software-management/createrepo_c/archive/0.17.6/createrepo_c-0.17.6.tar.gz
Summary  : Creates a common metadata repository
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: createrepo_c-bin = %{version}-%{release}
Requires: createrepo_c-data = %{version}-%{release}
Requires: createrepo_c-lib = %{version}-%{release}
Requires: createrepo_c-license = %{version}-%{release}
Requires: createrepo_c-man = %{version}-%{release}
Requires: createrepo_c-python = %{version}-%{release}
Requires: createrepo_c-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : bzip2-dev
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : file-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libmagic)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : popt-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : rpm-dev
BuildRequires : zlib-dev

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package bin
Summary: bin components for the createrepo_c package.
Group: Binaries
Requires: createrepo_c-data = %{version}-%{release}
Requires: createrepo_c-license = %{version}-%{release}

%description bin
bin components for the createrepo_c package.


%package data
Summary: data components for the createrepo_c package.
Group: Data

%description data
data components for the createrepo_c package.


%package dev
Summary: dev components for the createrepo_c package.
Group: Development
Requires: createrepo_c-lib = %{version}-%{release}
Requires: createrepo_c-bin = %{version}-%{release}
Requires: createrepo_c-data = %{version}-%{release}
Provides: createrepo_c-devel = %{version}-%{release}
Requires: createrepo_c = %{version}-%{release}

%description dev
dev components for the createrepo_c package.


%package lib
Summary: lib components for the createrepo_c package.
Group: Libraries
Requires: createrepo_c-data = %{version}-%{release}
Requires: createrepo_c-license = %{version}-%{release}

%description lib
lib components for the createrepo_c package.


%package license
Summary: license components for the createrepo_c package.
Group: Default

%description license
license components for the createrepo_c package.


%package man
Summary: man components for the createrepo_c package.
Group: Default

%description man
man components for the createrepo_c package.


%package python
Summary: python components for the createrepo_c package.
Group: Default
Requires: createrepo_c-python3 = %{version}-%{release}

%description python
python components for the createrepo_c package.


%package python3
Summary: python3 components for the createrepo_c package.
Group: Default
Requires: python3-core

%description python3
python3 components for the createrepo_c package.


%prep
%setup -q -n createrepo_c-0.17.6
cd %{_builddir}/createrepo_c-0.17.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632766746
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DCMAKE_CTEST_ARGUMENTS="--verbose --output-on-failure" \
-DLIB_INSTALL_DIR=/usr/lib64 \
-DWITH_ZCHUNK=OFF \
-DENABLE_DRPM=OFF \
-DWITH_LIBMODULEMD=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make -C clr-build test

%install
export SOURCE_DATE_EPOCH=1632766746
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/createrepo_c
cp %{_builddir}/createrepo_c-0.17.6/COPYING %{buildroot}/usr/share/package-licenses/createrepo_c/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/createrepo_c
/usr/bin/mergerepo_c
/usr/bin/modifyrepo_c
/usr/bin/sqliterepo_c

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/createrepo_c
/usr/share/bash-completion/completions/mergerepo_c
/usr/share/bash-completion/completions/modifyrepo_c
/usr/share/bash-completion/completions/sqliterepo_c

%files dev
%defattr(-,root,root,-)
/usr/include/createrepo_c/checksum.h
/usr/include/createrepo_c/compression_wrapper.h
/usr/include/createrepo_c/constants.h
/usr/include/createrepo_c/createrepo_c.h
/usr/include/createrepo_c/deltarpms.h
/usr/include/createrepo_c/error.h
/usr/include/createrepo_c/helpers.h
/usr/include/createrepo_c/koji.h
/usr/include/createrepo_c/load_metadata.h
/usr/include/createrepo_c/locate_metadata.h
/usr/include/createrepo_c/mergerepo_c.h
/usr/include/createrepo_c/misc.h
/usr/include/createrepo_c/modifyrepo_shared.h
/usr/include/createrepo_c/package.h
/usr/include/createrepo_c/parsehdr.h
/usr/include/createrepo_c/parsepkg.h
/usr/include/createrepo_c/repomd.h
/usr/include/createrepo_c/sqlite.h
/usr/include/createrepo_c/threads.h
/usr/include/createrepo_c/updateinfo.h
/usr/include/createrepo_c/version.h
/usr/include/createrepo_c/xml_dump.h
/usr/include/createrepo_c/xml_file.h
/usr/include/createrepo_c/xml_parser.h
/usr/lib64/libcreaterepo_c.so
/usr/lib64/pkgconfig/createrepo_c.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcreaterepo_c.so.0
/usr/lib64/libcreaterepo_c.so.0.17.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/createrepo_c/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/createrepo_c.8
/usr/share/man/man8/mergerepo_c.8
/usr/share/man/man8/modifyrepo_c.8
/usr/share/man/man8/sqliterepo_c.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
