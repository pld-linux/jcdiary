Summary:	jClimber's Diary
Summary(pl):	jClimber's Diary - dziennik wspinaczkowy
Name:		jcdiary
Version:	2.0
Release:	0.1
Group:		X11/Applications
License:	GPL v2
Source0:	http://www.saring.de/jcd/download/%{name}-%{version}-src.zip
URL:		http://www.saring.de/jcd/
BuildRequires:	jdk
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jClimber's Diary is a Java application for writing down climbing
routes in something like a diary. The entries are stored
hierarchically, so it's easy to navigate and search through the tree.
You can add comments for each entry or tally routes. The data is
stored in XML format and can be exported to HTML.

%description -l pl
jClimber's Diary to aplikacja w Javie do zapisywania tras
wspinaczkowych w czym¶ w rodzaju dziennika. Wpisy s± zapisywane
hierarchicznie, wiêc ³atwo jest nawigowaæ i wyszukiwaæ w drzewie.
Mo¿na dodawaæ komentarze do ka¿dego wpisu lub odpowiednich tras. Dane
s± zapisywane w formacie XML i mog± byæ wyeksportowane do HTML.

%prep
%setup -q -n %{name}

%build
# I don't have any idea how to build it - sources are in package....

#chmod 755 configure
#chmod 755 mkinstalldirs
#%configure2_13 				\
#        --with-jdk=/usr/lib/java	\
#	--enable-jpty
#%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc text/{CHANGES.txt,README*,TODO.txt}
#%attr (755,root,root) %{_bindir}/*
#%dir %{_datadir}/j
#%{_datadir}/j/themes
#%{_datadir}/j/j.jar
