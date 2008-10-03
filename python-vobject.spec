Summary:	Python module for parsing iCal data
Summary(pl.UTF-8):	Moduł języka Python analizujący dane iCal
Name:		python-vobject
Version:	0.4.8
Release:	2
License:	Apache v1.1
Group:		Libraries/Python
Source0:	http://vobject.skyhouseconsulting.com/vobject-%{version}.tar.gz
# Source0-md5:	d681436476e2b1d7265412df30a02c96
URL:		http://vobject.skyhouseconsulting.com/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
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
vCard oraz vCalendar. Jest zaprojektowany zgodnie z projektem
Fundacji Wolnego Oprogramowania o nazwie Chandler.

Obecnie dobrze przetestowana jest obsługa plików iCalendar. Pliki
vCard 3.0 także są obsługiwane i wszystkie dane powinny być
importowane, jednakże tylko kilka komponentów jest zrozumiałych w
wyrafinowany sposób.

%prep
%setup -q -n vobject-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ics_diff
%dir %{py_sitedir}/vobject
%{py_sitedir}/vobject/*.py[co]
%{py_sitedir}/vobject-*.egg-info
