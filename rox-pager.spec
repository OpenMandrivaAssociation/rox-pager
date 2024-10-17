%define oname Pager
%define version 1.0.2
%define cvs 20050604
%define fname pager-%cvs
Name:		rox-pager
Version:	%version
Release:	%mkrel 0.%cvs.6
Summary:	Pager for the panel of the ROX-Filer
Group:		Graphical desktop/Other
License:	GPL
URL:		https://rox.sourceforge.net/phpwiki/index.php/Pager
Source0:	http://prdownloads.sourceforge.net/rox/%fname.tar.bz2
Requires:       rox
BuildRequires: libwnck-devel
BuildRequires: libxml2-devel
Buildroot: %_tmppath/%name-%version

%description
The pager is a panel applet that shows a miniature view of your
desktop. You can use it to bring hidden windows to the front, move
windows around or, if using multiple workspaces, see which one you're
on and change between them.

The pager will only work if your window manager supports the Extended
Window Manager Hints standard, defined at http://freedesktop.org.
Different window managers have different levels of support for this,
so if it doesn't work, it's probably a problem with the window manager
rather than with the pager.

%define _appsdir %{_libdir}/apps

%prep
%setup -q -n %oname

%build
export CFLAGS="$RPM_OPT_FLAGS"
./AppRun --compile

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT%{_appsdir}
cp -a ../%oname $RPM_BUILD_ROOT%{_appsdir}/%{oname}
rm -rf %buildroot%_appsdir/%oname/./src


%files
%defattr(-,root,root)
%doc %{_appsdir}/%oname/Help
%dir %{_appsdir}/%oname/
%{_appsdir}/%oname/Linux*
%{_appsdir}/%oname/App*
%{_appsdir}/%oname/Options.xml
%{_appsdir}/%oname/.DirIcon
%dir %_libdir/apps/Pager/Messages/
%lang(it) %_libdir/apps/Pager/Messages/it.gmo

%clean 
rm -rf %buildroot




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-0.20050604.6mdv2010.0
+ Revision: 433425
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.2-0.20050604.5mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jun 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-0.20050604.5mdv2008.0
+ Revision: 38209
- rebuild


* Fri Nov 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-0.20050604.4mdv2007.0
+ Revision: 76206
- Import rox-pager

* Fri Nov 03 2006 Götz Waschk <waschk@mandriva.org> 1.0.2-0.20050604.4mdv2007.1
- mkrel

* Thu Oct 13 2005 Götz Waschk <waschk@mandriva.org> 1.0.2-0.20050604.3mdk
- rebuild for new libwnck

* Fri Sep 02 2005 Götz Waschk <waschk@mandriva.org> 1.0.2-0.20050604.2mdk
- rebuild to remove glitz dep

* Tue Aug 23 2005 Götz Waschk <waschk@mandriva.org> 1.0.2-0.20050604.1mdk
- update to cvs snapshot

* Fri Feb 04 2005 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-1mdk
- update file list
- New release 1.0.1

* Mon Jan 12 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.0-3mdk
- fix buildrequires

* Mon Jan 12 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.0-2mdk
- fix description, thanks to Markus Überall

* Mon Jan 12 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.0-1mdk
- initial package

