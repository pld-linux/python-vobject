Summary:	Python module for parsing iCal data
Summary(pl.UTF-8):	Moduł języka Python analizujący dane iCal
Name:		python-vobject
Version:	0.8.1c
Release:	2
License:	Apache v1.1
Group:		Libraries/Python
Source0:	http://vobject.skyhouseconsulting.com/vobject-%{version}.tar.gz
# Source0-md5:	c9686dd74d39fdae140890d9c694c076
URL:		http://vobject.skyhouseconsulting.com/
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-setuptools >= 1:0.6-1.c9
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files. It is being developed in
concert with the Open Source Application Foundation's Chandler
project.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%description -l pl.UTF-8
Vobject w zamierzeniu ma być pakietem do analizy i tworzenia plików
vCard oraz vCalendar. Jest zaprojektowany zgodnie z projektem Fundacji
Wolnego Oprogramowania o nazwie Chandler.

Obecnie dobrze przetestowana jest obsługa plików iCalendar. Pliki
vCard 3.0 także są obsługiwane i wszystkie dane powinny być
importowane, jednakże tylko kilka komponentów jest zrozumiałych w
wyrafinowany sposób.

%prep
%setup -q -n vobject-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--install-purelib=%{py_sitedir} \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/change_tz
%attr(755,root,root) %{_bindir}/ics_diff
%dir %{py_sitedir}/vobject
%{py_sitedir}/vobject/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/vobject-*.egg-info
%endif
