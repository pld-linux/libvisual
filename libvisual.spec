Summary:	Abstraction library that comes between applications and audio visualisation plugins
Summary(pl.UTF-8):	Abstrakcyjna biblioteka pomiędzy aplikacjami a wtyczkami wizualizacji audio
Name:		libvisual
Version:	0.4.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/libvisual/%{name}-%{version}.tar.bz2
# Source0-md5:	7ad5a74317337d91e87c905fd5d8013e
Patch0:		%{name}-link.patch
Patch1:		%{name}-NULL.patch
URL:		http://libvisual.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14
Obsoletes:	libvisual-tools < 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstraction library that comes between applications and audio
visualisation plugins.

%description -l pl.UTF-8
Abstrakcyjna biblioteka pomiędzy aplikacjami a wtyczkami wizualizacji
audio.

%package devel
Summary:	Header files for libvisual library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvisual
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvisual library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvisual.

%package static
Summary:	Static libvisual library
Summary(pl.UTF-8):	Statyczna biblioteka libvisual
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvisual library.

%description static -l pl.UTF-8
Statyczna biblioteka libvisual.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/libvisual-0.4

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvisual-0.4.la

# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{es_ES,es}

%find_lang %{name}-0.4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-0.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libvisual-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvisual-0.4.so.0
%dir %{_libdir}/libvisual-0.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-0.4.so
%{_includedir}/libvisual-0.4
%{_pkgconfigdir}/libvisual-0.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvisual-0.4.a
