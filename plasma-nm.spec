Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm
Version:	0.9.3.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/network/%{name}
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{name}-%{version}.tar.xz
Source10:	kde-nm-connection-editor-ru.po
Source11:	plasma_applet_org.kde.plasma-nm-ru.po
Patch0:		plasma-nm-0.9.3.0-i18n-ru.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(ModemManagerQt)
BuildRequires:	pkgconfig(NetworkManagerQt)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8
Requires:	modemmanager
Requires:	networkmanager

%description
Plasma applet and editor for managing your network connections in KDE 4 using
the default NetworkManager service.

%files -f %{name}.lang
%{_kde_bindir}/kde-nm-connection-editor
%{_kde_libdir}/kde4/imports/org/kde/plasmanm/
%{_kde_libdir}/kde4/kded_plasmanm.so
%{_kde_libdir}/kde4/plasma_nm_notifications.so
%{_kde_libdir}/kde4/plasmanm_l2tpui.so
%{_kde_libdir}/kde4/plasmanm_openswanui.so
%{_kde_libdir}/kde4/plasmanm_openvpnui.so
%{_kde_libdir}/kde4/plasmanm_pptpui.so
%{_kde_libdir}/kde4/plasmanm_vpncui.so
%{_kde_libdir}/kde4/plugins/designer/plasmanmwidgets.so
%{_kde_libdir}/libplasmanm-editor.so
%{_kde_libdir}/libplasmanm-internal.so
%{_kde_applicationsdir}/kde-nm-connection-editor.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.plasma-nm
%{_kde_appsdir}/desktoptheme/default/icons/plasma-nm.svgz
%{_kde_appsdir}/kde-nm-connection-editor
%{_kde_appsdir}/plasma-nm
%{_kde_services}/kded/plasmanm.desktop
%{_kde_services}/plasma-applet-nm.desktop
%{_kde_services}/plasma_nm_notifications.desktop
%{_kde_services}/plasmanm_l2tpui.desktop
%{_kde_services}/plasmanm_openswanui.desktop
%{_kde_services}/plasmanm_openvpnui.desktop
%{_kde_services}/plasmanm_pptpui.desktop
%{_kde_services}/plasmanm_vpncui.desktop
%{_kde_servicetypes}/plasma-nm-vpnuiplugin.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

# Use better russian translations (must be re-checked in 0.9.3.0+)
rm -rf po/ru/*.po
cp %{SOURCE10} po/ru/kde-nm-connection-editor.po
cp %{SOURCE11} po/ru/plasma_applet_org.kde.plasma-nm.po

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang kde-nm-connection-editor \
	plasma_applet_org.kde.plasma-nm \
	kcm_network libplasmanm-editor \
	plasmanm-kded \
	plasmanm_l2tpui \
	plasmanm_openconnectui \
	plasmanm_openswanui \
	plasmanm_openvpnui \
	plasmanm_pptpui \
	plasmanm_vpncui \
	%{name}.lang

