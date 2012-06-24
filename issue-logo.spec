Summary:	PLD Linux release file with logo
Summary(de):	PLD Linux Release-Datei mit logo
Summary(pl):	Wersja Linuksa PLD z logiem
Name:		issue-logo
Version:	1.0
Release:	5
License:	GPL
Group:		Base
Group(de):	Gr�nds�tzlich
Group(es):	Base
Group(pl):	Podstawowe
Group(pt_BR):	Base
BuildArch:	noarch
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue
Obsoletes:	issue-pure
Obsoletes:	issue-fancy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file with logo.

%description -l de
PLD Linux Release-Datei mit logo.

%description -l pl
Wersja Linuksa PLD z logiem.

%prep

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
