%define version 4.4.0
%define name	deutex
%define release	%mkrel 1

%define	Summary	A utility for modifying the graphics of Doom IWAD and PWAD files

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.teaser.fr/~amajorel/deutex/%{name}-%{version}.tar.bz2
URL:		http://www.deutex.com/
Group:		Games/Arcade
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel smpeg-devel SDL_mixer-devel SDL_net-devel
BuildRequires:	automake sed

%description
DeuTex is a wad composer for Doom, Heretic, Hexen and Strife. It can be used to extract the lumps
of a wad and save them as individual files. Conversely, it can also build a wad from separate files. 
When extracting a lump to a file, it does not just copy the raw data, it converts it to an 
appropriate format (such as PPM for graphics, Sun audio for samples, etc.). Conversely, when it 
reads files for inclusion in pwads, it does the necessary conversions (for example, from PPM to Doom 
picture format). In addition, DeuTex has functions such as merging wads, etc.

%prep 
%setup -q -n %{name}-%{version}
%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_bindir}/deutex
install -d %{buildroot}/%{_bindir}/deusf

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
# no %doc ?
%defattr (-,root,root)
%{_bindir}/deutex
%{_bindir}/deusf

