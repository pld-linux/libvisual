Summary:	Abstraction library that comes between applications and audio visualisation plugins
Summary(pl.UTF-8):	Abstrakcyjna biblioteka pomiędzy aplikacjami a wtyczkami wizualizacji audio
Name:		libvisual
Version:	0.4.0
Release:	7
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libvisual/%{name}-%{version}.tar.bz2
# Source0-md5:	d0f987abd0845e725743605fd39ef73f
Patch0:		%{name}-link.patch
Patch1:		%{name}-NULL.patch
# original URL is defunct; use sf
#URL:		http://localhost.nl/~synap/libvisual/
URL:		http://libvisual.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-tools >= 0.14.1
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14
BuildRequires:	sed >= 4.0
Obsoletes:	libvisual-tools
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

mv -f po/{es_ES,es}.po
# es_AR is a copy of es
%{__rm} po/{es_AR.po,stamp-po}
sed -i -e 's|es_ES es_AR|es|' po/LINGUAS
# hack for newer gettext
sed -i -e 's/DOMAIN = .*/DOMAIN = libvisual-0.4/' po/Makevars

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
%{_libdir}/libvisual-0.4.la
%{_includedir}/libvisual-0.4
%{_pkgconfigdir}/libvisual-0.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvisual-0.4.a
