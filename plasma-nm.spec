%define snapshot 20130703

Summary:	Plasma applet written in QML for managing network connections
Name:		plasma-nm
Version:	0.9.3.0
Release:	0.%{snapshot}.1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/network/%{name}
Source0:	%{name}-%{version}-%{snapshot}.tar.bz2
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

%prep
%setup -q -n %{name}-%{version}-%{snapshot}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%{_kde_bindir}/kde-nm-connection-editor
%{_kde_libdir}/kde4/imports/org/kde/plasmanm/
%{_kde_libdir}/kde4/kcm_network.so
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
%{_kde_services}/kcm_network.desktop
%{_kde_services}/kded/plasmanm.desktop
%{_kde_services}/plasma-applet-nm.desktop
%{_kde_services}/plasma_nm_notifications.desktop
%{_kde_services}/plasmanm_l2tpui.desktop
%{_kde_services}/plasmanm_openswanui.desktop
%{_kde_services}/plasmanm_openvpnui.desktop
%{_kde_services}/plasmanm_pptpui.desktop
%{_kde_services}/plasmanm_vpncui.desktop
%{_kde_servicetypes}/plasma-nm-vpnuiplugin.desktop

