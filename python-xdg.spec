# NOTE: for versions >= 2 see python3-xdg.spec
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-xdg.spec)

Summary:	Variables defined by the XDG Base Directory Specification
Summary(pl.UTF-8):	Zmienne zdefiniowane w specyfikacji XDG Base Directory
Name:		python-xdg
# keep 1.x here for python2 support
Version:	1.0.7
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/xdg/
Source0:	https://files.pythonhosted.org/packages/source/x/xdg/xdg-%{version}.tar.gz
# Source0-md5:	5e67a1592905c461a743e72b6478511f
Patch0:		%{name}-rename.patch
URL:		https://pypi.org/project/xdg/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg is a tiny Python module which provides the variables defined by
the XDG Base Directory Specification, to save you from duplicating the
same snippet of logic in every Python utility you write that deals
with user cache, configuration, or data files. It has no external
dependencies.

%description -l pl.UTF-8
xdg to mały moduł Pythona, udostępniający zmienne zdefiniowane w
specyfikacji XDG Base Directory, aby oszczędzić duplikowania tej samej
logiki w każdym narzędziu pythonowym, które obsługuje pamięć
podręczną, konfigurację czy pliki danych użytkownika. Moduł nie ma
zewnętrznych zależności.

%package -n python3-xdg
Summary:	Variables defined by the XDG Base Directory Specification
Summary(pl.UTF-8):	Zmienne zdefiniowane w specyfikacji XDG Base Directory
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-xdg
xdg is a tiny Python module which provides the variables defined by
the XDG Base Directory Specification, to save you from duplicating the
same snippet of logic in every Python utility you write that deals
with user cache, configuration, or data files. It has no external
dependencies.

%description -n python3-xdg -l pl.UTF-8
xdg to mały moduł Pythona, udostępniający zmienne zdefiniowane w
specyfikacji XDG Base Directory, aby oszczędzić duplikowania tej samej
logiki w każdym narzędziu pythonowym, które obsługuje pamięć
podręczną, konfigurację czy pliki danych użytkownika. Moduł nie ma
zewnętrznych zależności.

%prep
%setup -q -n xdg-%{version}

# "xdg" name conflicts with older (but more comprehensive) pyxdg module,
# which uses xdg namespace; rename to allow using both in the same system.
%patch0 -p1
%{__mv} xdg.py xdgenv.py

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENCE README.rst
%{py_sitescriptdir}/xdgenv.py[co]
%{py_sitescriptdir}/xdg-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-xdg
%defattr(644,root,root,755)
%doc LICENCE README.rst
%{py3_sitescriptdir}/xdgenv.py
%{py3_sitescriptdir}/__pycache__/xdgenv.cpython-*.py[co]
%{py3_sitescriptdir}/xdg-%{version}-py*.egg-info
%endif
