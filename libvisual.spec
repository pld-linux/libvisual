Summary:	Abstraction library that comes between applications and audio visualisation plugins
Summary(pl):	Abstrakcyjna biblioteka pomiêdzy aplikacjami a wtyczkami wizualizacji audio
Name:		libvisual
Version:	0.2.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libvisual/%{name}-%{version}.tar.gz
# Source0-md5:	668236dcbd252c70f1beff551f36b8b3
URL:		http://libvisual.sourceforge.net/
Patch0:		%{name}-ppc.patch
Buildrequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstraction library that comes between applications and audio
visualisation plugins.

%description -l pl
Abstrakcyjna biblioteka pomiêdzy aplikacjami a wtyczkami wizualizacji
audio.

%package devel
Summary:	Header files for libvisual library
Summary(pl):	Pliki nag³ówkowe biblioteki libvisual
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvisual library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libvisual.

%package static
Summary:	Static libvisual library
Summary(pl):	Statyczna biblioteka libvisual
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvisual library.

%description static -l pl
Statyczna biblioteka libvisual.

#%package tools
#Summary:	Utilities for libvisual library
#Summary(pl):	Narzêdzia dla biblioteki libvisual
#Group:		Development/Libraries
#Requires:	%{name}-devel = %{version}-%{release}
#
#%description tools
#Utilities for libvisual library.
#
#%description static -l pl
#Narzêdzia dla biblioteki libvisual.

%prep
%setup -q
%ifarch ppc ppc64
%patch0 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
#cp -f lvconfig.h libvisual
%{__make} \
	LDFLAGS="%{rpmldflags} -L../libvisual"

#%{__make} -C tools \
#	LDFLAGS="%{rpmldflags} -L../libvisual"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#%{__make} -C tools install \
#	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
#%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

#%files tools
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/*
