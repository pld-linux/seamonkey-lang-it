%define	_lang	it
%define	_reg	IT
%define	_lare	%{_lang}-%{_reg}
Summary:	Italian resources for SeaMonkey
Summary(pl.UTF-8):	Włoskie pliki językowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.1.6
Release:	2
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	bf0a7b55e23e4a822fc326cd38ec4125
Source1:	http://www.mozilla-enigmail.org/download/release/0.95/enigmail-%{_lare}-0.95.xpi
# Source1-md5:	613bba3e4d5586b8d02fe6882e0066f1
Source2:	gen-installed-chrome.sh
URL:		http://www.seamonkey-project.org/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Italian resources for SeaMonkey.

%description -l pl.UTF-8
Włoskie pliki językowe dla SeaMonkeya.

%prep
%setup -q -c
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
	> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults searchplugins $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_lare}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/seamonkey/defaults/profile/%{_lang}
%{_datadir}/seamonkey/searchplugins/*
