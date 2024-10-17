Name:		deutex
Version:	4.4.0
Release:	5
Summary:	Summary	A utility for modifying the graphics of Doom IWAD and PWAD files
Source0:	http://www.teaser.fr/~amajorel/deutex/%{name}-%{version}.tar.bz2
# this patch s needed otherwise we cannot see fatal error on start, used
# to fix a segfault on start, as code was not 64 bits clean
Patch0:     deutex-4.4.0-fix-error-on-startup.diff
Patch1:     deutex-4.4.0-fix-error-on-64b.diff
URL:		https://www.deutex.com/
Group:		Games/Arcade
License:	GPLv2
BuildRequires:	SDL-devel smpeg-devel SDL_mixer-devel SDL_net-devel

%description
DeuTex is a wad composer for Doom, Heretic, Hexen and Strife. It can be used
to extract the lumps of a wad and save them as individual files. Conversely,
it can also build a wad from separate files.  When extracting a lump to a file,
it does not just copy the raw data, it converts it to an appropriate format
(such as PPM for graphics, Sun audio for samples, etc.). Conversely, when it
reads files for inclusion in pwads, it does the necessary conversions (for
example, from PPM to Doom picture format). In addition, DeuTex has functions
such as merging wads, etc.

%prep 
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
%make CFLAGS="%optflags" LDFLAGS="%ldflags"

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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 4.4.0-3mdv2011.0
+ Revision: 610238
- rebuild

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 4.4.0-2mdv2010.1
+ Revision: 541253
- use flags

* Sun Mar 29 2009 Michael Scherer <misc@mandriva.org> 4.4.0-2mdv2009.1
+ Revision: 362134
- fix segfault on x86_64 on start, and also port it to 64 bits
- remove useless buildRequires
- update license
- fix installation of file ( bug 49263 )
- add doc and man page

* Tue Nov 18 2008 Zombie Ryushu <ryushu@mandriva.org> 4.4.0-1mdv2009.1
+ Revision: 304124
- import deutex



* Fri May 19 2006 Lenny Cartier <lenny@mandrakesoft.com> 4.4.0
- 4.4.0
