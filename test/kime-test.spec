Name: kime-test
Version: 3.2.0
Release: 2%{?dist}
License: GPLv3
Summary: Korean IME

URL: https://github.com/Riey/kime
Source0: %{url}/archive/ec17f7279500b4024810c7083c5a67c3bd539894.tar.gz

BuildRequires: cargo
BuildRequires: clang-devel
BuildRequires: gtk3-devel
BuildRequires: gtk4-devel
BuildRequires: meson
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel

Requires: gtk3
Requires: glib2

%description
Copr for [kime](https://github.com/Riey/kime)

%prep
%autosetup -n kime-ec17f7279500b4024810c7083c5a67c3bd539894

%conf
%meson

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files

%{_bindir}/kime
%{_bindir}/kime-candidate-window
%{_bindir}/kime-check
%{_bindir}/kime-indicator
%{_bindir}/kime-wayland
%{_bindir}/kime-xdg-autostart
%{_bindir}/kime-xim

%{_includedir}/kime_engine.h
%{_includedir}/kime_engine.hpp

%{_docdir}/kime/*

%{_libdir}/gtk-3.0/3.0.0/immodules/libim-kime.so
%{_libdir}/gtk-4.0/4.0.0/immodules/libkime-gtk4.so
%{_libdir}/libkime_engine.so
%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%{_datadir}/applications/kime.desktop
%{_datadir}/icons/hicolor/64x64/apps/*
%{_sysconfdir}/xdg/autostart/kime.desktop

%post
gtk-query-immodules-3.0-64 --update-cache
gio-querymodules-64 %{_libdir}/gtk-4.0/4.0.0/immodules

%changelog
* Tue Jun 30 2026 Quadratech188 <quadratech188@gmail.com> 3.2.0-2
- fix: Use new build process (quadratech188@gmail.com)

* Tue Jun 30 2026 Quadratech188 <quadratech188@gmail.com> 3.2.0-1
- 

* Tue Jun 30 2026 Quadratech188 <quadratech188@gmail.com> 0.0.1.0e846e1-8
- chore: Bump to 3.2.0 (quadratech188@gmail.com)

* Mon May 18 2026 Quadratech188 <quadratech188@gmail.com> 0.0.1.0e846e1-7
- Bump Qt version

* Sat May 16 2026 Quadratech188 <quadratech188@gmail.com> 0.0.1.0e846e1-6
- fix: Use gtk3-query-immodules correctly (quadratech188@gmail.com)

* Sat May 16 2026 Quadratech188 <quadratech188@gmail.com> 0.0.1.0e846e1-5
- fix: Use gio-querymodules correctly (quadratech188@gmail.com)

* Sat May 16 2026 Quadratech188 <quadratech188@gmail.com> 0.0.1.0e846e1-4
- fix: Update GTK im cache (quadratech188@gmail.com)

* Fri May 15 2026 Quadratech188 <quadratech188@gmail.com> 0.0.1.0e846e1-3
- test: Bump tag? (quadratech188@gmail.com)

* Tue Feb 03 2026 Quadratech188 <quadratech188@gmail.com> 0.0.1.0e846e1-1
- chore: Bump to 0e846e1 (quadratech188@gmail.com)

* Fri Jan 30 2026 Quadratech188 <quadratech188@gmail.com> 0.0.0.0179318-1
- new package built with tito

%autochangelog
