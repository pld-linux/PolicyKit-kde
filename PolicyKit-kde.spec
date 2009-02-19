#
# Conditional build:
#
%define		qt_ver		4.4.3
%define		kdever		4.2.0
%define		snap		928657

Summary:	PolicyKit-kde
Summary(pl.UTF-8):	PolicyKit-kde
Name:		PolicyKit-kde
Version:	0
Release:	0.%{snap}.2
License:	GPL v2
Group:		X11/Applications
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/extragear/base/PolicyKit-kde
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	78e56e43ae330be8b99050a78f035ca7
BuildRequires:	PolicyKit-devel
BuildRequires:	Qt3Support-devel >= %{qt_ver}
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PolicyKit-kde provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

#%description -l pl.UTF-8

%prep
%setup -q -n %{name}

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/polkit-kde-authorization
%attr(755,root,root) %ghost %{_libdir}/libpolkitkdeprivate.so.4
%attr(755,root,root) %{_libdir}/libpolkitkdeprivate.so.4.2.0
%attr(755,root,root) %{_libdir}/kde4/kcm_pkk_authorization.so
%attr(755,root,root) %{_libdir}/kde4/libexec/polkit-kde-manager
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt.so.0
%attr(755,root,root) %{_libdir}/libpolkit-qt.so.0.9.0
%{_datadir}/kde4/services/kcm_pkk_authorization.desktop
%{_datadir}/dbus-1/services/kde-org.freedesktop.PolicyKit.AuthenticationAgent.service
%{_datadir}/dbus-1/services/org.kde.PolicyKit.service
