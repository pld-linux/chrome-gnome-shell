Summary:	GNOME Shell integration for Chrome
Summary(pl.UTF-8):	Integracja GNOME Shell dla Chrome'a
Name:		chrome-gnome-shell
Version:	10.1
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/chrome-gnome-shell/10.1/%{name}-%{version}.tar.xz
# Source0-md5:	11dd4c539fefff7153b4f0af8e6e4a71
URL:		https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
BuildRequires:	cmake >= 2.8
# base64, sha256sum
BuildRequires:	coreutils >= 6.0
BuildRequires:	gettext-tools
BuildRequires:	jq
BuildRequires:	p7zip
BuildRequires:	python3 >= 1:3.2
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gnome-shell >= 3.22
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
This package contains Browser extension for Google Chrome/Chromium,
Firefox, Vivaldi, Opera (and other Browser Extension, Chrome Extension
or WebExtensions capable browsers) and native host messaging connector
that provides integration with GNOME Shell and the corresponding
extensions repository (https://extensions.gnome.org/).

%description -l pl.UTF-8
Ten pakiet zawiera rozszerzenie dla przeglądarek Google
Chrome/Chromium, Firefox, Vivaldi, Opera (i innych przeglądarek
obsługujących rozszerzenia Chrome lub WebExtension) oraz natywny
łącznik komunikacyjny, zapewniający integrację z powłoką GNOME Shell
oraz jej repozytorium rozszerzeń (https://extensions.gnome.org/).

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DPYTHON_EXECUTABLE=%{__python3}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_iconsdir}/{gnome,hicolor}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/chrome-gnome-shell
%{py3_sitedir}/chrome_gnome_shell-0.0.0-py*.egg-info
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{_desktopdir}/org.gnome.ChromeGnomeShell.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.ChromeGnomeShell.png
# -chromium
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%{_sysconfdir}/chromium/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
# -chrome
%dir /etc/opt/chrome
%dir /etc/opt/chrome/native-messaging-hosts
/etc/opt/chrome/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
# -firefox
%dir %{_libdir}/mozilla/native-messaging-hosts
%{_libdir}/mozilla/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
