Summary:	Goggles Music Manager
Name:		gogglesmm
Version:	0.12.6
Release:	1
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



%changelog
* Wed May 30 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.12.0-1
+ Revision: 801374
- imported package gogglesmm

