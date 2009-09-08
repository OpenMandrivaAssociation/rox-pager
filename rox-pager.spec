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
URL:		http://rox.sourceforge.net/phpwiki/index.php/Pager
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


