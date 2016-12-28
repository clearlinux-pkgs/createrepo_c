#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : createrepo_c
Version  : 0.10.0
Release  : 16
URL      : https://github.com/rpm-software-management/createrepo_c/archive/0.10.0.tar.gz
Source0  : https://github.com/rpm-software-management/createrepo_c/archive/0.10.0.tar.gz
Summary  : Test package
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: createrepo_c-bin
Requires: createrepo_c-python
Requires: createrepo_c-lib
Requires: createrepo_c-doc
Requires: createrepo_c-data
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : expat-dev
BuildRequires : file-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : popt-dev
BuildRequires : python-dev
BuildRequires : rpm-dev
BuildRequires : zlib-dev

%description
This package has provides, requires, obsoletes, conflicts options.

%package bin
Summary: bin components for the createrepo_c package.
Group: Binaries
Requires: createrepo_c-data

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
Requires: createrepo_c-lib
Requires: createrepo_c-bin
Requires: createrepo_c-data
Provides: createrepo_c-devel

%description dev
dev components for the createrepo_c package.


%package doc
Summary: doc components for the createrepo_c package.
Group: Documentation

%description doc
doc components for the createrepo_c package.


%package lib
Summary: lib components for the createrepo_c package.
Group: Libraries
Requires: createrepo_c-data

%description lib
lib components for the createrepo_c package.


%package python
Summary: python components for the createrepo_c package.
Group: Default

%description python
python components for the createrepo_c package.


%prep
%setup -q -n createrepo_c-0.10.0

%build
export LANG=C
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DLIB_INSTALL_DIR=/usr/lib64
make VERBOSE=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
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
/usr/include/createrepo_c/load_metadata.h
/usr/include/createrepo_c/locate_metadata.h
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
