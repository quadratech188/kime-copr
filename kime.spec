Name: kime
Version: 0.0.1.0e846e1
Release: 0%{?dist}
License: GPLv3
Summary: Korean IME

URL: https://github.com/Riey/kime
Source0: %{url}/archive/0e846e1.tar.gz

BuildRequires: cargo
BuildRequires: clang-devel
BuildRequires: cmake
BuildRequires: gtk3-devel
BuildRequires: gtk4-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt6-qtbase-private-devel

%description
Copr for [kime](https://github.com/Riey/kime)

%prep
%autosetup -C

%build

cargo build --release
%cmake -S src \
	-DENABLE_GTK3=ON \
	-DENABLE_GTK4=ON \
	-DENABLE_QT5=ON \
	-DENABLE_QT6=ON

%cmake_build

%install
install -Dm755 \
	target/release/kime \
	target/release/kime-candidate-window \
	target/release/kime-check \
	target/release/kime-indicator \
	target/release/kime-wayland \
	target/release/kime-xim \
	-t %{buildroot}%{_bindir}

install -Dm755 target/release/libkime_engine.so -t %{buildroot}%{_libdir}

install -Dm755 %{_vpath_builddir}/lib/libkime-gtk3.so -t %{buildroot}%{_libdir}/gtk-3.0/immodules
install -Dm755 %{_vpath_builddir}/lib/libkime-gtk4.so -t %{buildroot}%{_libdir}/gtk-4.0/immodules

install -Dm755 %{_vpath_builddir}/lib/libkime-qt5.so %{buildroot}%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
install -Dm755 %{_vpath_builddir}/lib/libkime-qt6.so %{buildroot}%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

install -Dm644 res/kime.desktop -t %{buildroot}%{_datadir}/applications
install -Dm644 res/icons/64x64/* -t %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

%files

%license LICENSE
%doc README.md
%doc README.ko.md
%doc NOTICE.md
%doc docs/CONFIGURATION.md
%doc docs/CONFIGURATION.ko.md
%doc docs/CHANGELOG.md
%doc res/default_config.yaml

%{_bindir}/kime
%{_bindir}/kime-candidate-window
%{_bindir}/kime-check
%{_bindir}/kime-indicator
%{_bindir}/kime-wayland
%{_bindir}/kime-xim

%{_libdir}/libkime_engine.so

%{_libdir}/gtk-3.0/immodules/libkime-gtk3.so
%{_libdir}/gtk-4.0/immodules/libkime-gtk4.so

%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
%{_datadir}/applications/kime.desktop
%{_datadir}/icons/hicolor/64x64/apps/*

%changelog
* Fri Jan 30 2026 Quadratech188 <quadratech188@gmail.com> 0.0.0.0179318-1
- new package built with tito

%autochangelog
