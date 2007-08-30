#
Summary:	Python module for parsing iCal data
Summary(pl.UTF-8):	Moduł języka Python analizujący dane iCal
Name:		python-vobject
Version:	0.4.8
Release:	1
License:	GPLv2
Group:		Libraries/Python
Source0:	http://vobject.skyhouseconsulting.com/vobject-%{version}.tar.gz
# Source0-md5:	d681436476e2b1d7265412df30a02c96
URL:		http://vobject.skyhouseconsulting.com/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for parsing iCal data.

%description -l pl.UTF-8
Moduł języka Python analizujący dane iCal.

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
%{py_sitedir}/vobject-0.4.8-py2.5.egg-info
%{py_sitedir}/vobject/*.py[co]
