
%define	distname	Ac
%define	distversion	1.99
%define	distrelease	"%{distversion} PLD Linux (%{distname})"

Summary:	PLD Linux release file with logo
Summary(de):	PLD Linux Release-Datei mit logo
Summary(pl):	Wersja Linuksa PLD z logiem
Name:		issue-logo
Version:	%{distversion}
Release:	1
License:	GPL
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue
Obsoletes:	issue-alpha
Obsoletes:	issue-fancy
Obsoletes:	issue-pure
Obsoletes:	redhat-release
Obsoletes:	mandrake-release

%description
PLD Linux release file with logo.

%description -l de
PLD Linux Release-Datei mit logo.

%description -l pl
Wersja Linuksa PLD z logiem.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
  _
 / )     PLD Linux %{distversion} (%{distname}) \m, \r
/ /       Welcome to \n
 ( -.      \u user(s)
 \\\   \\\
  \\\  \\\\\\\
   \`| \\\\\\\
    |  \`
    |

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
  _
 / )     PLD Linux %{distversion} (%{distname}) %m, %r
/ /       Welcome to %h
 ( -.
 \\\   \\\
  \\\  \\\\\\\
   \`| \\\\\\\
    |  \`
    |

EOF
echo %{distrelease} > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
