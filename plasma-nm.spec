%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%ifarch aarch64
%global optflags %{optflags} -fuse-ld=bfd
%endif

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$

Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm
Version:	5.19.4
Release:	2
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
%{_libdir}/libplasmanm_editor.so
%{_libdir}/libplasmanm_internal.so
%{_libdir}/qt5/plugins/kcm_networkmanagement.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_fortisslvpnui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_iodineui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_l2tpui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_openconnectui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_openswanui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_openvpnui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_pptpui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_sshui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_sstpui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_strongswanui.so
%{_libdir}/qt5/plugins/libplasmanetworkmanagement_vpncui.so
%{_libdir}/qt5/plugins/kf5/kded/networkmanagement.so
%{_libdir}/qt5/qml/org/kde/plasma/networkmanagement
%{_datadir}/metainfo/org.kde.plasma.networkmanagement.appdata.xml
%{_datadir}/knotifications5/networkmanagement.notifyrc
%{_datadir}/kservices5/kcm_networkmanagement.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.networkmanagement.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_fortisslvpnui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_iodineui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_l2tpui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openconnect_globalprotectui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openconnect_juniperui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openconnectui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openswanui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openvpnui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_pptpui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_sshui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_sstpui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_strongswanui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_vpncui.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement
%{_datadir}/kcm_networkmanagement
%{_datadir}/kservicetypes5/plasma-networkmanagement-vpnuiplugin.desktop

#----------------------------------------------------------------------------

%package mobile
Summary:	Plasma Mobile interface to NetworkManager
Group:		Graphical desktop/KDE

%description mobile
Plasma Mobile interface to NetworkManager

%files mobile -f %{name}-mobile.lang
%{_libdir}/qt5/plugins/kcms/kcm_mobile_*.so
%{_datadir}/kpackage/kcms/kcm_mobile_broadband
%{_datadir}/kpackage/kcms/kcm_mobile_hotspot
%{_datadir}/kpackage/kcms/kcm_mobile_wifi
%{_datadir}/kservices5/hotspotsettings.desktop
%{_datadir}/kservices5/mobilebroadbandsettings.desktop
%{_datadir}/kservices5/wifisettings.desktop

%prep
%autosetup -p1
%cmake_kde5 -DBUILD_MOBILE:BOOL=ON

%build
%ninja -C build

%install
%ninja_install -C build

for i in plasma_applet_org.kde.plasma.networkmanagement \
		plasmanetworkmanagement-kcm plasmanetworkmanagement-kded \
		plasmanetworkmanagement-libs plasmanetworkmanagement_fortisslvpnui \
		plasmanetworkmanagement_iodineui plasmanetworkmanagement_l2tpui \
		plasmanetworkmanagement_openconnectui plasmanetworkmanagement_openswanui \
		plasmanetworkmanagement_openvpnui plasmanetworkmanagement_pptpui \
		plasmanetworkmanagement_sshui plasmanetworkmanagement_sstpui \
		plasmanetworkmanagement_strongswanui plasmanetworkmanagement_vpncui; do
	%find_lang $i --with-html --with-man
	cat $i.lang >>%{name}.lang
done

for i in kcm_mobile_broadband kcm_mobile_hotspot kcm_mobile_wifi; do
	%find_lang $i --with-html --with-man
	cat $i.lang >>%{name}-mobile.lang
done
