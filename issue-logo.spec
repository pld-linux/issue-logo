
%bcond_with	snap	# include shapshot information in version,
			# should be used only in official Th spanhots

%define snapshot	2012

# CPE_NAME = cpe:/ {part} : {vendor} : {product} : {version} : {update} : {edition} : {language}
# http://cpe.mitre.org/specification/
# http://csrc.nist.gov/publications/nistir/ir7695/NISTIR-7695-CPE-Naming.pdf

%if %{with snap}
%define	distname	Th/%{snapshot}
%define cpename		cpe:/o:pld-linux:pld:%{distversion}:%{snapshot}
%else
%define	distname	Th
%define cpename		cpe:/o:pld-linux:pld:%{distversion}
%endif
%define	distversion	3.0
%define	distrelease	"%{distversion} PLD Linux (%{distname})"

Summary:	PLD Linux release file with logo
Summary(de.UTF-8):	PLD Linux Release-Datei mit logo
Summary(pl.UTF-8):	Wersja Linuksa PLD z logiem
Name:		issue-logo
Version:	%{distversion}
Release:	1%{?with_snap:.%{snapshot}}
License:	GPL
Group:		Base
Provides:	issue
Conflicts:	issue-alpha < 3.0
Conflicts:	issue-fancy < 3.0
Conflicts:	issue-nice < 3.0
Conflicts:	issue-pure < 3.0
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

# CPE_NAME = cpe:/ {part} : {vendor} : {product} : {version} : {update} : {edition} : {language}
# http://cpe.mitre.org/specification/
cat >$RPM_BUILD_ROOT%{_sysconfdir}/os-release <<EOF
NAME="PLD Linux"
VERSION="%{distversion} (%{distname})"
ID="pld"
VERSION_ID="%{distversion}"
PRETTY_NAME="PLD Linux %{distversion} (%{distname})"
ANSI_COLOR="0;32"
CPE_NAME="%{cpename}"
HOME_URL="http://www.pld-linux.org/"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/os-release
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
