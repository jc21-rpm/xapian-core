%global debug_package %{nil}

Summary:       The Xapian Probabilistic Information Retrieval Library
Name:          xapian-core
Version:       1.4.13
Release:       1
License:       GPL
Vendor:        xapian.org
Group:         Applications/Databases
URL:           https://xapian.org
Requires:      %{name}-libs = %{version}
BuildRequires: gcc-c++ zlib-devel libuuid-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Xapian is an Open Source Probabilistic Information Retrieval Library. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications.

%package libs
Summary: Xapian search engine libraries.
Group: System Environment/Libraries

%description libs
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
libraries for applications using Xapian functionality.

%package devel
Group: Development/Libraries
Summary: Files needed for building packages which use Xapian.
Requires: %{name}-libs = %{version}

%description devel
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for building packages which use Xapian.

%prep
wget http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
xz -d %{name}-%{version}.tar.xz
tar xf %{name}-%{version}.tar

%build
cd %{name}-%{version}
%configure
make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}
cd %{name}-%{version}
make DESTDIR=%{buildroot} install
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_datadir}/doc/%{name}-devel-%{version}
cp HACKING %{buildroot}%{_datadir}/doc/%{name}-devel-%{version}
mkdir -p %{buildroot}%{_datadir}/doc/%{name}-%{version}
cp AUTHORS ChangeLog ChangeLog.examples COPYING NEWS PLATFORMS README %{buildroot}%{_datadir}/doc/%{name}-%{version}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/xapian-tcpsrv
%{_bindir}/xapian-progsrv
%{_bindir}/quest
%{_bindir}/copydatabase
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/simpleexpand
%{_bindir}/xapian-check
%{_bindir}/xapian-compact
%{_bindir}/xapian-delve
%{_bindir}/xapian-replicate
%{_bindir}/xapian-replicate-server
%{_bindir}/xapian-metadata
%{_bindir}/xapian-pos
%{_datadir}/xapian-core/stopwords/*.list
%doc %{_datadir}/doc/%{name}-%{version}
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian-tcpsrv.1*
%{_mandir}/man1/xapian-progsrv.1*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/copydatabase.1*
%{_mandir}/man1/xapian-check.1*
%{_mandir}/man1/xapian-compact.1*
%{_mandir}/man1/xapian-delve.1*
%{_mandir}/man1/xapian-replicate.1*
%{_mandir}/man1/xapian-replicate-server.1*
%{_mandir}/man1/xapian-metadata.1*
%{_mandir}/man1/xapian-pos.1*

%files libs
%defattr(-, root, root)
%{_libdir}/libxapian*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/xapian-config
%{_includedir}/xapian
%{_includedir}/xapian.h
%{_libdir}/libxapian*.so
#%{_libdir}/libxapian*.a
%{_libdir}/libxapian*.la
%{_libdir}/cmake/xapian
%{_libdir}/pkgconfig/xapian*.pc
%{_datadir}/aclocal/xapian*.m4
%doc %{_datadir}/doc/%{name}-devel-%{version}
# man pages may be gzipped, hence the trailing wildcard.
%{_mandir}/man1/xapian-config.1*

%changelog
* Thu Oct 17 2019 Jamie Curnow <jc@jc21.com> - 1.4.13-1
- v1.4.13

* Mon Mar 11 2019 Jamie Curnow <jc@jc21.com> - 1.4.11-1
- v1.4.11

* Thu Dec 6 2018 Jamie Curnow <jc@jc21.com> - 1.4.9-1
- v1.4.9

* Tue Aug 28 2018 Jamie Curnow <jc@jc21.com> - 1.4.7-1
- v1.4.7

* Thu Jul 19 2018 Jamie Curnow <jc@jc21.com> - 1.4.6-1
- updated spec to 1.4.6

