# $Revision: 1.11 $ $Date: 2003-05-25 05:50:36 $
Summary:	Mixmaster anonymous remailer
Summary(pl):	Anonimowy remailer typu Mixmaster
Name:		mixmaster
Version:	2.0.3
Release:	1
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.hacktic.nl/pub/replay/pub/remailer/%{name}-%{version}.tar.gz
Patch0:		%{name}-2.0.3-1-linux.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixmaster is a remailer, allowing you to send an anonymous email.
Mixmaster is type II remailer, which is improved version of old
,,cypherpunks'' remailers.

%description -l pl
Mixmaster jest remailerem, pozwalaj±cym na wysy³anie anonimowej poczty
elektronicznej. Mixmaster to remailer typu II, stanowi±cy ulepszon±
wersjê remailerów ,,cypherpunk''.

%prep
%setup -q
%setup -q -T -D -a 0
tar -xvf mix-%{version}.tar
%patch -p0

%build
cd ./Mix/Src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_sysconfdir}}/mixmaster

cd ./Mix
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
%config %{_sysconfdir}/mixmaster/mixmaster.conf
%doc Mix/README* Mix/mix.help*
%attr(755,root,root) %{_bindir}/mixmaster
%dir %{_datadir}/mixmaster
%{_datadir}/mixmaster/destination.block
%{_datadir}/mixmaster/mix.key
%{_datadir}/mixmaster/pubring.mix
%{_datadir}/mixmaster/source.block
%{_datadir}/mixmaster/type2.list
%{_mandir}/man1/*
