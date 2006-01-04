
%define		_name	xp

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	0.9
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.speleoalex.altervista.org/download/kde_%{_name}_full-%{version}.tar.gz
# Source0-md5:	24b8ec815c95c04e5e7c53f08d3109fe
URL:		http://www.speleoalex.altervista.org/kde.php
Requires:	kde-style-%{_name}
Requires:	kde-icons-%{_name}
Requires:	kde-decoration-icewm-%{_name}
Requires:	kde-wallpaper-%{_name}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains data for making KDE look like Windows XP Luna
(Blue).

%description -l pl
Ten pakiet zawiera dane do upodobnienia KDE do Windows XP Luna
(niebieskiego).

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
This package contains Windows XP Luna (Blue) style for KDE.

%description -n kde-style-%{_name} -l pl
Ten pakiet zawiera styl Windows XP Luna (niebieski) dla KDE.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl):	Motyw ikon do kde - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
This package contains the standard Windows XP icon theme.

%description -n kde-icons-%{_name} -l pl
Ten pakiet zawiera motyw ikon z Windows XP.

%package -n kde-wallpaper-%{_name}
Summary:	KDE wallpaper - %{_name}
Summary(pl):	Tapeta do KDE - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdelibs

%description -n kde-wallpaper-%{_name}
This package contains two wallpapers similar to the ones distributed
with Windows XP.

%description -n kde-wallpaper-%{_name} -l pl
Ten pakiet zawiera dwie tapety podobne do rozprowadzanych z Windows
XP.

%package -n kde-decoration-icewm-%{_name}
Summary:	Icewm window decoration for kwin - %{_name}
Summary(pl):	Dekoracja icewm dla kwin - %{_name}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
A kwin decoration that resembles Windows XP Luna (Blue).

%description -n kde-decoration-icewm-%{_name} -l pl
Dekoracja kwin podobna do Windows XP Luna (niebieskiego).

%package -n superkaramba-theme-%{_name}
Summary:	superkaramba theme - %{_name}
Summary(pl):	motyw superkaramba - %{_name}
Group:		Themes
Requires:	superkaramba

%description -n superkaramba-theme-%{_name}
Superkaramba theme with Windows XP start menu and taskbar.

%description -n superkaramba-theme-%{_name} -l pl
Motyw superkaramba z menu start i paskiem zadañ z Windowsa XP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_iconsdir},%{_datadir}/{wallpapers,apps/{kstyle,kwin/icewm-themes},themes/superkaramba/xp}}
mv -f icons/kde_xp $RPM_BUILD_ROOT%{_iconsdir}
mv -f kde_xpStyle/wallpapers/* $RPM_BUILD_ROOT%{_datadir}/wallpapers
mv -f kde_xpStyle/pixmaps $RPM_BUILD_ROOT%{_datadir}/apps/kstyle
mv -f kde_xpStyle/themes $RPM_BUILD_ROOT%{_datadir}/apps/kstyle
mv -f kde_xpTheme/kde_xp $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes
mv -f winbar/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xp
sed -i -e "s,mdk-hicolor,crystalsvg," $RPM_BUILD_ROOT%{_iconsdir}/kde_xp/index.desktop
rm -f $RPM_BUILD_ROOT%{_iconsdir}/kde_xp/index.desktop~
rm -f $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/default.theme~
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xp/{README,COPYING,Changelog,theme.pyc}
%py_comp $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xp
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xp

%post -n kde-style-%{_name}
/sbin/ldconfig
echo "You may have to run kinstalltheme for this theme to become available"
echo "in currently opened sessions."

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kstyle/themes/*.themerc
%{_datadir}/apps/kstyle/pixmaps/*

%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%{_iconsdir}/*

%files -n kde-decoration-icewm-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes/*

%files -n kde-wallpaper-%{_name}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n superkaramba-theme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/xp/*
