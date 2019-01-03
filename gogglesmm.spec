%define _disable_lto 1
%define _disable_ld_no_undefined 1

Summary:	Goggles Music Manager
Name:		gogglesmm
Version:	1.2.1
Release:	1
Group:		Sound
License:	GPLv3
URL:		https://gogglesmm.github.io/
Source0:	http://code.google.com/p/gogglesmm/%{name}-%{version}.tar.gz

BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fox17)
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
BuildRequires:  faad2-devel
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(smbclient)
Requires:       xine-pulse
Requires:       xine-plugins
Suggests:       xine-flac
Suggests:       xine-aa
Suggests:       xine-caca



%description
Goggles Music Manager is a music collection manager and player that 
automatically categorizes your music files based on genre, artist, album, and 
song. It supports gapless playback and features easy tag editing.

%prep
%setup -q

%build
%cmake	-DCMAKE_INSTALL_LIBDIR="%{_libdir}" \
        -DCMAKE_BUILD_TYPE="Release"
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_libdir}/%{name}
%{_datadir}/%{name}

