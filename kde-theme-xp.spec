
%define		_name	xp

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	0.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://digidownload.libero.it/speleoalex/download/kde_%{_name}_full.tar.gz
# Source0-md5:	630a8c06812b39c6c5410f931c1a9ae0
URL:		http://www.kde-look.org/content/show.php?content=1499
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

%prep
%setup -q -n kde_%{_name}_full

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_iconsdir},%{_datadir}/{wallpapers,apps/{kstyle,kwin/icewm-themes}}}
mv -f icons/kde_xp $RPM_BUILD_ROOT%{_iconsdir}
mv -f kde_xpStyle/wallpapers/* $RPM_BUILD_ROOT%{_datadir}/wallpapers
mv -f kde_xpStyle/pixmaps $RPM_BUILD_ROOT%{_datadir}/apps/kstyle
mv -f kde_xpStyle/themes $RPM_BUILD_ROOT%{_datadir}/apps/kstyle
mv -f kde_xpTheme/kde_xp $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes
sed -i -e "s,mdk-hicolor,crystalsvg," $RPM_BUILD_ROOT%{_iconsdir}/kde_xp/index.desktop

%post -n kde-style-%{_name}
/sbin/ldconfig
echo "You may have to run kinstalltheme for this theme to become available"
echo "in currently opened sessions."

%clean
rm -rf $RPM_BUILD_ROOT

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
