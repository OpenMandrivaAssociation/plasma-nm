%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm
Version:	6.4.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/plasma-nm
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-nm/-/archive/%{gitbranch}/plasma-nm-%{gitbranchd}.tar.bz2#/plasma-nm-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{major}/plasma-nm-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6ModemManagerQt)
BuildRequires:	cmake(KF6NetworkManagerQt)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	pkgconfig(openconnect) >= 3.99
BuildRequires:	pkgconfig(mobile-broadband-provider-info)
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6UiTools)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	pkgconfig(libnm)
Requires:	mobile-broadband-provider-info
Requires:	modemmanager
Requires:	networkmanager
Requires:	networkmanager-wifi
Requires:	networkmanager-ppp
Conflicts:	plasma-applet-networkmanagement
Conflicts:	knetworkmanager-common
Conflicts:	plasma-nm < 0.9.3.7
Obsoletes:	plasma-applet-networkmanagement <= 0.9.0.9-2
# Renamed 2025-05-02 after 6.0
%rename plasma6-nm

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Plasma applet and editor for managing your network connections in KDE5 using
the default NetworkManager service.

%files -f %{name}.lang
%{_libdir}/libplasmanm_editor.so
%{_libdir}/libplasmanm_internal.so
%dir %{_qtdir}/plugins/plasma/network
%dir %{_qtdir}/plugins/plasma/network/vpn
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_pptpui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_sshui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_sstpui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_vpncui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_arrayui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_f5ui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_fortinetui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
%{_qtdir}/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so
%{_qtdir}/plugins/kf6/kded/networkmanagement.so
%{_qtdir}/qml/org/kde/plasma/networkmanagement
%{_datadir}/metainfo/org.kde.plasma.networkmanagement.appdata.xml
%{_datadir}/knotifications6/networkmanagement.notifyrc
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement
%{_datadir}/kcm_networkmanagement
%{_datadir}/qlogging-categories6/plasma-nm.categories
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_networkmanagement.so
%{_datadir}/applications/kcm_networkmanagement.desktop
%{_datadir}/applications/org.kde.vpnimport.desktop
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_cellular_network.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_hotspot.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_wifi.so
%{_datadir}/applications/kcm_cellular_network.desktop
%{_datadir}/applications/kcm_mobile_hotspot.desktop
%{_datadir}/applications/kcm_mobile_wifi.desktop
