Summary:	Goggles Music Manager
Name:		gogglesmm
Version:	0.13.1
Release:	1
Group:		Sound
License:	GPLv3
URL:		http://gogglesmm.github.io/
Source0:        https://github.com/gogglesmm/gogglesmm/archive/%{name}-0.13.1.tar.gz
Source100:	%{name}.rpmlintrc

Patch0:		gogglesmm-taglib.patch

BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fox17)  >= 1.7.46
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib) 
BuildRequires:	pkgconfig(taglib-extras)
BuildRequires:	pkgconfig(glew)
BuildRequires:	libgap-devel
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glproto)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(flac)
BuildRequires:  mad-devel
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:  libfaad2-devel
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(smbclient)


Suggests:   gogglesmm-utils = %{EVRD}


%description
Goggles Music Manager is a music collection manager and player that 
automatically categorizes your music files based on genre, artist, album, and 
song. It supports gapless playback and features easy tag editing.

#----------
%define libname %mklibname %{name}

%package -n %{libname}

Group:		Sound
Summary:	Main libs for %{name}

%description -n %{libname}
Goggles Music Manager is a music collection manager and player that 
automatically categorizes your music files based on genre, artist, album, and 
song. It supports gapless playback and features easy tag editing.


%files -n %{libname}
%doc README ChangeLog AUTHORS COPYING
%{_libdir}/%{name}/libgap_*.so


#-------------------
%package -n %{name}-utils

Group:		Sound
Summary:	Utils for %{name}
Requires:   python

%description -n %{name}-utils
Goggles Music Manager is a music collection manager and player that 
automatically categorizes your music files based on genre, artist, album, and 
song. It supports gapless playback and features easy tag editing.

%files -n %{name}-utils
%doc README ChangeLog AUTHORS COPYING
%{_datadir}/%{name}/utils


%prep
%setup -q
%patch0 -p0

%build
export LDFLAGS="$LDFLAGS -ldl -lopusfile -Wl ,--as-needed"
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"

%ifarch x86_64
%configure2_5x --lib64
%else
%configure2_5x 
%endif

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*




%changelog
* Sat May 10 2014 SymbianFlo <symbianflo@mandrivausers.ro> 0.13.1-1
+ Revision: 991b40a
- Updated gogglesmm.spec


