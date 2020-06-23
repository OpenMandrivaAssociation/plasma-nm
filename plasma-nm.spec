%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%ifarch aarch64
%global optflags %{optflags} -fuse-ld=bfd
%endif

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$

Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm
Version:	5.19.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/network/plasma-nm
Source0:	http://download.kde.org/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	pkgconfig(openconnect) >= 3.99
BuildRequires:	pkgconfig(mobile-broadband-provider-info)
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5UiTools)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(qca2-qt5)
Requires:	kirigami
Requires:	mobile-broadband-provider-info
Requires:	modemmanager
Requires:	networkmanager
Conflicts:	plasma-applet-networkmanagement
Conflicts:	knetworkmanager-common
Conflicts:	plasma-nm < 0.9.3.7
Obsoletes:	plasma-applet-networkmanagement <= 0.9.0.9-2
%rename	plasma-nm5

%description
Plasma applet and editor for managing your network connections in KDE5 using
the default NetworkManager service.

%files -f %{name}.lang
%{_libdir}/libplasmanm_*.so
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kded/networkmanagement.so
%{_libdir}/qt5/qml/org/kde/plasma/networkmanagement
%{_datadir}/metainfo/*.xml
%{_datadir}/knotifications5/networkmanagement.notifyrc
%{_datadir}/kservices5/*.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement
%{_datadir}/kcm_networkmanagement
%{_datadir}/kservicetypes5/plasma-networkmanagement*.desktop

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html --with-man
