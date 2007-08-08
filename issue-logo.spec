
%define	distname	Th
%define	distversion	2.99
%define	distrelease	"%{distversion} PLD Linux (%{distname})"

Summary:	PLD Linux release file with logo
Summary(de.UTF-8):	PLD Linux Release-Datei mit logo
Summary(pl.UTF-8):	Wersja Linuksa PLD z logiem
Name:		issue-logo
Version:	%{distversion}
Release:	3
License:	GPL
Group:		Base
Provides:	issue
Obsoletes:	mandrake-release
Obsoletes:	redhat-release
Conflicts:	issue-alpha < 2.99-2
Conflicts:	issue-fancy < 2.99-2
Conflicts:	issue-pure < 2.99-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file with logo.

%description -l de.UTF-8
PLD Linux Release-Datei mit logo.

%description -l pl.UTF-8
Wersja Linuksa PLD z logiem.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
  _
 / )     PLD Linux %{distversion} (%{distname}) \m, \r
/ /       Welcome to \n
 ( -.      \u user(s)
 \\\\   \\\\
  \\\\  \\\\\\\\
   \\\`| \\\\\\\\
    |  \\\`
    |

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
  _
 / )     PLD Linux %{distversion} (%{distname}) %m, %r
/ /       Welcome to %h
 ( -.
 \\\\   \\\\
  \\\\  \\\\\\\\
   \\\`| \\\\\\\\
    |  \\\`
    |

EOF
echo %{distrelease} > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
