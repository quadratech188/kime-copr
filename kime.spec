Name: kime
Version: 3.1.1
Release: 0%{?dist}
License: GPLv3
Summary: Korean IME

URL: https://github.com/Riey/kime
Source0: https://github.com/Riey/kime/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo

%description
Copr repo for [kime](https://github.com/Riey/kime)

%prep
%autosetup

%build
scripts/build.sh -ar

%install
scripts/install.sh /

%changelog
