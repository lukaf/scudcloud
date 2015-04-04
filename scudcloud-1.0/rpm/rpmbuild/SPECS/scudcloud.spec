%define scudcloud_prefix /opt/scudcloud

Name:   scudcloud
Version:    %{SCUDCLOUD_VERSION}
Release:	1%{?dist}
Summary:	ScudCloud is a non official desktop client for Slack

Group:		utils
License:    MIT
URL:        https://github.com/raelgc/%{name}
Source0:    https://github.com/raelgc/%{name}/archive/v%{version}.tar.gz

Requires:   python3
Requires:   python3-PyQt4
Requires:   python3-dbus

%description
ScudCloud is a non official desktop client for Slack.
Slack (http://slack.com) is a platform for team communication.

%prep
%setup -q

%build
# nothing to build

%install
%{__rm} -rf %{buildroot}

%{__mkdir} -p %{buildroot}%{scudcloud_prefix}/lib
%{__mkdir} -p %{buildroot}%{scudcloud_prefix}/resources
%{__mkdir} -p %{buildroot}%{_datadir}/application
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
%{__mkdir} -p %{buildroot}%{_bindir}

%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/lib/*.py %{buildroot}%{scudcloud_prefix}/lib
%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/resources/* %{buildroot}%{scudcloud_prefix}/resources

%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/LICENSE %{buildroot}%{scudcloud_prefix}
%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/scudcloud.desktop %{buildroot}%{_datadir}/application
%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/systray/hicolor/* %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

%{__install} -m 755 %{_builddir}/%{name}-%{version}/scudcloud-1.0/scudcloud %{buildroot}%{_bindir}

find %{buildroot} -type f -printf "%y %%%%attr(0%m,-,-) %p\n" | \
sed -e 's/^d /%%dir /' \
    -e "s#%{buildroot}##" \
    -e 's/^[^d] //' > %{_tmppath}/%{name}-%{version}-%{release}.f

%files -f %{_tmppath}/%{name}-%{version}-%{release}.f
%dir %{scudcloud_prefix}
%dir %{scudcloud_prefix}/lib
%dir %{scudcloud_prefix}/resources
%ghost %{scudcloud_prefix}/lib/*.py?

%clean
%{__rm} -rf %{buildroot}
%{__rm} -r %{_tmppath}/%{name}-%{version}-%{release}.f

%changelog
