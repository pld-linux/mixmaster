# $Revision: 1.4 $ $Date: 2000-05-28 10:05:36 $
Summary:	Mixmaster anonymous remailer
Summary(pl):	Anonimowy remailer typu Mixmaster
Name:		mixmaster
Version:	2.0.3
Release:	1
License:	BSD
Group:		Applications/Networking
Group(pl):	Narzêdzia/Sieciowe
Source0:	ftp://ftp.hacktic.nl/pub/replay/pub/remailer/%{name}-%{version}.tar.gz
Patch0:		mixmaster-2.0.3-1-linux.patch
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
make

%install
rm -rf $RPM_BUILD_ROOT
if [ ! -d %{_datadir}/mixmaster ]; then
	install -d %{_datadir}/mixmaster
fi
if [ ! -d %{_sysconfdir}/mixmaster ]; then
	install -d %{_sysconfdir}/mixmaster
fi
cd ./Mix
install mixmaster {%_bindir}
install	mixmaster.conf %{_sysconfdir}
install destination.block \
		mix.key \
		pubring.mix	\
		source.block \
		type2.list \
		%{_datadir}/mixmaster
install mixmaster.1 %{_mandir}/man1
cp ./mixmaster.1 %{_prefix}/man/man1

gzip -9nf Mix/README Mix/mix.help ${_mandir}/man1/* || :

%files
%defattr(644,root,root,755)
%dir %{_datadir}/mixmaster
%dir %{_sysconfdir}/mixmaster
%config %{_sysconfdir}/mixmaster/mixmaster.conf
%doc ./Mix/README*
%doc ./Mix/mix.help
%attr(755,root,root) %{_bindir}/mixmaster
%{_datadir}/mixmaster/destination.block
%{_datadir}/mixmaster/mix.key
%{_datadir}/mixmaster/pubring.mix
%{_datadir}/mixmaster/source.block
%{_datadir}/mixmaster/type2.list
%{_mandir}/man1/*
