Summary:	PLD Linux release file with logo
Summary(de):	PLD Linux Release-Datei mit logo
Summary(pl):	Wersja Linuksa PLD z logiem
Name:		issue-logo
Version:	1.0
Release:	2
License:	free
Group:		Base
Group(de):	Gründsätzlich
Group(es):	Base
Group(pl):	Podstawowe
Group(pt_BR):	Base
BuildArch:	noarch
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
c
  _ 
 / )     PLD Linux 1.0 (Ra) \m, \r
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
 / )     PLD Linux 1.0 (Ra) %m, %r
/ /       Welcome to %h
 ( -.      
 \\\   \\\     
  \\\  \\\\\\\       
   \`| \\\\\\\        
    |  \`
    | 
 
EOF
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
