Summary:	Italian resources for SeaMonkey
Summary(pl):	Wloskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-it
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.it-IT.langpack.xpi
# Source0-md5:	aa4b87bf0e834740b8859b052c5b298d
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-it-IT-0.9x.xpi
# Source1-md5:	f7793ca6bdfae7d5913c8eb1b6f8a619
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Italian resources for SeaMonkey.

%description -l pl
Wloskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale chrome/{IT,it-IT,it-unix,enigmail-it-IT}.jar \
	> lang-it-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{IT,it-IT,it-unix,enigmail-it-IT}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-it-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults searchplugins $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/IT.jar
%{_chromedir}/it-IT.jar
%{_chromedir}/it-unix.jar
%{_chromedir}/enigmail-it-IT.jar
%{_chromedir}/lang-it-installed-chrome.txt
%{_datadir}/seamonkey/defaults/profile/it
%{_datadir}/seamonkey/searchplugins/*
