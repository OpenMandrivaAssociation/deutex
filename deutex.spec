%define version 4.4.0
%define name	deutex
%define release	%mkrel 2

%define	Summary	A utility for modifying the graphics of Doom IWAD and PWAD files

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.teaser.fr/~amajorel/deutex/%{name}-%{version}.tar.bz2
# this patch s needed otherwise we cannot see fatal error on start, used
# to fix a segfault on start, as code was not 64 bits clean
Patch0:     deutex-4.4.0-fix-error-on-startup.diff
Patch1:     deutex-4.4.0-fix-error-on-64b.diff
URL:		http://www.deutex.com/
Group:		Games/Arcade
License:	GPLv2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel smpeg-devel SDL_mixer-devel SDL_net-devel

%description
DeuTex is a wad composer for Doom, Heretic, Hexen and Strife. It can be used to extract the lumps
of a wad and save them as individual files. Conversely, it can also build a wad from separate files. 
When extracting a lump to a file, it does not just copy the raw data, it converts it to an 
appropriate format (such as PPM for graphics, Sun audio for samples, etc.). Conversely, when it 
reads files for inclusion in pwads, it does the necessary conversions (for example, from PPM to Doom 
picture format). In addition, DeuTex has functions such as merging wads, etc.

%prep 
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_prefix}/man/man6/
mkdir -p %{buildroot}/%_mandir/

make install PREFIX=%{buildroot}/%{_prefix}

mv %{buildroot}/%{_prefix}/man/man6/ %{buildroot}/%_mandir/man6/

%clean
rm -rf %{buildroot}

%files
%doc CHANGES LICENSE README COPYING TODO COPYING.LIB VERSION
%defattr (-,root,root)
%{_bindir}/deutex
%{_bindir}/deusf
%_mandir/man6/*
