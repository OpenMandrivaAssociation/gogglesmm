Summary:	Goggles Music Manager
Name:		gogglesmm
Version:	0.12.6
Release:	4
Group:		Sound
License:	GPLv3
URL:		http://code.google.com/p/gogglesmm/
Source0:	http://code.google.com/p/gogglesmm/%{name}-%{version}.tar.xz

BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fox)
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



%description
Goggles Music Manager is a music collection manager and player that 
automatically categorizes your music files based on genre, artist, album, and 
song. It supports gapless playback and features easy tag editing.

%prep
%setup -q

%build
%configure2_5x

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



