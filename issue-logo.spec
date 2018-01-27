%define	distversion	%(. /etc/os-release 2>/dev/null ; echo $VERSION)

Summary:	PLD Linux prelogin message and identification file with logo
Summary(de.UTF-8):	PLD Linux Systemidentifikationsdatei mit logo
Summary(pl.UTF-8):	Plik z logiem identyfikujący system PLD Linux, wyświetlany przed zalogowaniem
Name:		issue-logo
Version:	3.0
Release:	10
License:	GPL
Group:		Base
BuildRequires:	pld-release >= 3.0
%requires_eq	pld-release
Provides:	issue = %{version}-%{release}
Conflicts:	issue-alpha < 3.0-1
Conflicts:	issue-fancy < 3.0-1
Conflicts:	issue-nice < 3.0-1
Conflicts:	issue-pure < 3.0-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux prelogin message and identification file with logo.

%description -l de.UTF-8
PLD Linux Systemidentifikationsdatei mit logo.

%description -l pl.UTF-8
Plik z logiem identyfikujący system PLD Linux,
wyświetlany przed zalogowaniem.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
  _
 / )     PLD Linux %{distversion} \m, \r
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
 / )     PLD Linux %{distversion} %m, %r
/ /       Welcome to %h
 ( -.
 \\\\   \\\\
  \\\\  \\\\\\\\
   \\\`| \\\\\\\\
    |  \\\`
    |

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/issue*
