Summary:	Mixmaster anonymous remailer
Summary(pl.UTF-8):	Anonimowy remailer typu Mixmaster
Name:		mixmaster
Version:	2.9.0
Release:	1
License:	GPL v1
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c10d1f7c35177748d947aab64143494a
URL:		http://mixmaster.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixmaster is a remailer, allowing you to send an anonymous email.
Mixmaster is type II remailer, which is improved version of old
,,cypherpunks'' remailers.

%description -l pl.UTF-8
Mixmaster jest remailerem, pozwalającym na wysyłanie anonimowej poczty
elektronicznej. Mixmaster to remailer typu II, stanowiący ulepszoną
wersję remailerów ,,cypherpunk''.

%prep
%setup -q

%build
./Install
#%%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_sysconfdir}}/mixmaster

install mixmaster $RPM_BUILD_ROOT%{_bindir}
install	mixmaster.conf $RPM_BUILD_ROOT%{_sysconfdir}
install destination.block \
		mix.key \
		pubring.mix	\
		source.block \
		type2.list \
		$RPM_BUILD_ROOT%{_datadir}/mixmaster
install mixmaster.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/mixmaster
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mixmaster/mixmaster.conf
%doc README* mix.help*
%attr(755,root,root) %{_bindir}/mixmaster
%dir %{_datadir}/mixmaster
%{_datadir}/mixmaster/destination.block
%{_datadir}/mixmaster/mix.key
%{_datadir}/mixmaster/pubring.mix
%{_datadir}/mixmaster/source.block
%{_datadir}/mixmaster/type2.list
%{_mandir}/man1/*
