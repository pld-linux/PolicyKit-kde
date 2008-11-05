#
# Conditional build:
#
%define		qt_ver		4.4.1
%define		snap		880532

Summary:	PolicyKit-kde
Summary(pl.UTF-8):	PolicyKit-kde
Name:		PolicyKit-kde
Version:	0
Release:	0.%{snap}.1
License:	GPL v2
Group:		X11/Applications
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/playground/base/PolicyKit-kde
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	dc40e0659cb2152eb3d2278948804af5
BuildRequires:	Qt3Support-devel >= %{qt_ver}
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PolicyKit-kde provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

#%description -l pl.UTF-8

%prep
%setup -q -n %{name}-%{snap}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)	%{_bindir}/policykit-kde
%{_datadir}/autostart/policykit-kde.desktop
