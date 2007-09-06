Summary:	Abstraction library that comes between applications and audio visualisation plugins
Summary(pl.UTF-8):	Abstrakcyjna biblioteka pomiędzy aplikacjami a wtyczkami wizualizacji audio
Name:		libvisual
Version:	0.4.0
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libvisual/%{name}-%{version}.tar.bz2
# Source0-md5:	d0f987abd0845e725743605fd39ef73f
URL:		http://localhost.nl/~synap/libvisual/
Patch0:		%{name}-link.patch
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14
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

mv -f po/{es_ES,es}.po
# es_AR is a copy of es
rm -f po/{es_AR.po,stamp-po}
sed -i -e 's|es_ES es_AR|es|' po/LINGUAS

%build
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
%attr(755,root,root) %{_libdir}/libvisual-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*.so
%{_libdir}/libvisual-*.la
%{_includedir}/libvisual-*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvisual-*.a
