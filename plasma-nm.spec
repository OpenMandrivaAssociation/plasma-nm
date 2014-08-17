Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm
Version:	0.9.3.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/network/%{name}
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{name}-%{version}.tar.xz
Source1:	01-plasma-nm.js
Source10:	ru.tar.gz
Patch0:		plasma-nm-0.9.3.4-i18n-ru.patch
BuildRequires:	mobile-broadband-provider-info
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(ModemManagerQt)
BuildRequires:	pkgconfig(NetworkManagerQt)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:	pkgconfig(openconnect) >= 3.99
Requires:	mobile-broadband-provider-info
Requires:	modemmanager
Requires:	networkmanager
Conflicts:	plasma-applet-networkmanagement
Conflicts:	knetworkmanager-common
Obsoletes:	plasma-applet-networkmanagement <= 0.9.0.9-2

%description
Plasma applet and editor for managing your network connections in KDE4 using
the default NetworkManager service.

%files -f %{name}.lang
%{_kde_bindir}/kde-nm-connection-editor
%{_kde_libdir}/kde4/imports/org/kde/networkmanagement/
%{_kde_libdir}/kde4/kded_networkmanagement.so
%{_kde_libdir}/kde4/networkmanagement_notifications.so
%{_kde_libdir}/kde4/plasmanetworkmanagement_l2tpui.so
%{_kde_libdir}/kde4/plasmanetworkmanagement_openconnectui.so
%{_kde_libdir}/kde4/plasmanetworkmanagement_openswanui.so
%{_kde_libdir}/kde4/plasmanetworkmanagement_openvpnui.so
%{_kde_libdir}/kde4/plasmanetworkmanagement_pptpui.so
%{_kde_libdir}/kde4/plasmanetworkmanagement_strongswanui.so
%{_kde_libdir}/kde4/plasmanetworkmanagement_vpncui.so
%{_kde_libdir}/kde4/plugins/designer/plasmanetworkmanagementwidgets.so
%{_kde_libdir}/libplasmanetworkmanagement-editor.so
%{_kde_libdir}/libplasmanetworkmanagement-internal.so
%{_kde_applicationsdir}/kde-nm-connection-editor.desktop
%{_kde_appsdir}/plasma-desktop/updates/01-plasma-nm.js
%{_kde_appsdir}/plasma/plasmoids/org.kde.networkmanagement
%{_kde_appsdir}/desktoptheme/default/icons/plasma-networkmanagement2.svgz
%{_kde_appsdir}/kde-nm-connection-editor
%{_kde_appsdir}/networkmanagement
%{_kde_iconsdir}/oxygen/*/devices/network-defaultroute.png
%{_kde_services}/kded/networkmanagement.desktop
%{_kde_services}/plasma-applet-networkmanagement.desktop
%{_kde_services}/networkmanagement_notifications.desktop
%{_kde_services}/plasmanetworkmanagement_l2tpui.desktop
%{_kde_services}/plasmanetworkmanagement_openconnectui.desktop
%{_kde_services}/plasmanetworkmanagement_openswanui.desktop
%{_kde_services}/plasmanetworkmanagement_openvpnui.desktop
%{_kde_services}/plasmanetworkmanagement_pptpui.desktop
%{_kde_services}/plasmanetworkmanagement_strongswanui.desktop
%{_kde_services}/plasmanetworkmanagement_vpncui.desktop
%{_kde_servicetypes}/plasma-networkmanagement-vpnuiplugin.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

# Use better russian translations (must be re-checked in 0.9.3.1+)
pushd po
tar -xvzf %{SOURCE10}
popd

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_kde_appsdir}/plasma-desktop/updates/
install -m 0644 %{SOURCE1} %{buildroot}%{_kde_appsdir}/plasma-desktop/updates/01-plasma-nm.js

%find_lang kde-nm-connection-editor \
	plasma_applet_org.kde.networkmanagement \
	libplasmanetworkmanagement-editor \
	plasmanetworkmanagement-kded \
	plasmanetworkmanagement_l2tpui \
	plasmanetworkmanagement_openconnectui \
	plasmanetworkmanagement_openswanui \
	plasmanetworkmanagement_openvpnui \
	plasmanetworkmanagement_pptpui \
	plasmanetworkmanagement_strongswanui \
	plasmanetworkmanagement_vpncui \
	%{name}.lang

