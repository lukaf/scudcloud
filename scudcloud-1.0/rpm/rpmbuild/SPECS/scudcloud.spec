%define scudcloud_prefix /opt/scudcloud

Name:       scudcloud
Version:    %{SCUDCLOUD_VERSION}
Release:    1%{?dist}
Summary:    ScudCloud is a non official desktop client for Slack

Group:      utils
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
%{__mkdir} -p %{buildroot}%{_datadir}/applications
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
%{__mkdir} -p %{buildroot}%{_bindir}

%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/lib/*.py %{buildroot}%{scudcloud_prefix}/lib
%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/resources/* %{buildroot}%{scudcloud_prefix}/resources

%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/LICENSE %{buildroot}%{scudcloud_prefix}
%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/scudcloud.desktop %{buildroot}%{_datadir}/applications
%{__install} -m 664 %{_builddir}/%{name}-%{version}/scudcloud-1.0/systray/hicolor/* %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

%{__install} -m 755 %{_builddir}/%{name}-%{version}/scudcloud-1.0/scudcloud %{buildroot}%{_bindir}
# For desktop app to work.
%{__install} -m 755 %{_builddir}/%{name}-%{version}/scudcloud-1.0/scudcloud %{buildroot}%{scudcloud_prefix}

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
* Sat Apr 4 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (e548672) Merge pull request #49 from raelgc/49-remember-last-window-settings

* Sat Apr 4 2015 Rael <rael.gc@gmail.com>
- (735bc86) Saving window settings (#49)

* Fri Apr 3 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (369446e) Updating manual install info

* Wed Apr 1 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (eeba51a) Merge pull request #44 from raelgc/44-saml-support

* Wed Apr 1 2015 Rael <rael.gc@gmail.com>
- (449eaea) SAML auth support (#44)

* Tue Mar 31 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (f9fda40) Adding more info about packages and manual install

* Tue Mar 31 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (2ff47fe) Adding more info about Arch

* Tue Mar 31 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (3967a5f) Merge pull request #48 from michaelherold/add-arch-to-readme

* Tue Mar 31 2015 Michael Herold <michael.j.herold@gmail.com>
- (574ba4c) Add installation instructions for Arch Linux

* Tue Mar 31 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (cad4214) Merge pull request #43 from raelgc/43-switch-team-at-ctrl

* Mon Mar 30 2015 Rael <rael.gc@gmail.com>
- (d4c9182) Enabling team switch at ctrl (#43)

* Mon Mar 23 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (a30e373) Merge pull request #41 from raelgc/41-stopAlert-crashing-app

* Mon Mar 23 2015 Rael <rael.gc@gmail.com>
- (18493af) Fixing stopAlert crashing (#41)

* Fri Mar 20 2015 Rael <rael.gc@gmail.com>
- (9f45969) New package

* Fri Mar 20 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (22fb553) Merge pull request #38 from immerrr/append-notifications

* Fri Mar 20 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (c573981) Merge pull request #40 from raelgc/40-mention-notification-for-team-switcher

* Fri Mar 20 2015 Rael <rael.gc@gmail.com>
- (838e3c6) Mention notification for team switcher (#40)

* Fri Mar 20 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (f34ce44) Adding manual instructions

* Fri Mar 20 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (4948c7f) Merge pull request #39 from raelgc/39-fixed-width-font

* Fri Mar 20 2015 Rael <rael.gc@gmail.com>
- (23989cb) Suggesting Courier New as fixed width font (#39)

* Fri Mar 20 2015 Rael <rael.gc@gmail.com>
- (6aa04df) If local socket failed, try just once removing pid

* Fri Mar 20 2015 Rael <rael.gc@gmail.com>
- (020e06b) Better handling of local socket

* Fri Mar 20 2015 Rael <rael.gc@gmail.com>
- (ae45fb1) Removing direction text in context menu

* Thu Mar 19 2015 immerrr <immerrr@gmail.com>
- (4f1fc34) Append messages to existing notification bubbles

* Wed Mar 18 2015 Rael <rael.gc@gmail.com>
- (8d66770) New package

* Wed Mar 18 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (4958d08) Merge pull request #30 from raelgc/30-zoom-support

* Tue Mar 17 2015 Rael <rael.gc@gmail.com>
- (69ac2fb) Saving/restoring zoom state (#30)

* Tue Mar 17 2015 Rael <rael.gc@gmail.com>
- (3787b72) Simple Zoom (#30)

* Tue Mar 17 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (8e0f670) Merge pull request #34 from raelgc/34-do-proper-cleanup

* Tue Mar 17 2015 Rael <rael.gc@gmail.com>
- (004eff3) Proper package cleanup (#34)

* Tue Mar 17 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (fb3033c) Merge pull request #35 from immerrr/add-appswitcher-icon

* Tue Mar 17 2015 immerrr <immerrr@gmail.com>
- (2e4e47e) Encapsulate INSTALL_DIR in resources module

* Tue Mar 17 2015 immerrr <immerrr@gmail.com>
- (c5aa3a7) Add application icon to show in application switcher

* Tue Mar 17 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (0afb5dc) Better description for 12.04

* Tue Mar 17 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (4ccfb7a) Just some ponctuaction (grammar)

* Tue Mar 17 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (cbcbb1e) Merge pull request #32 from immerrr/add-qtwebkit-and-xdg-utils-deps

* Tue Mar 17 2015 immerrr <immerrr@gmail.com>
- (36e7b0d) Add xdg-utils dependency (required for for xdg-open command)

* Tue Mar 17 2015 immerrr <immerrr@gmail.com>
- (39f6d7c) Update README.md a bit

* Tue Mar 17 2015 immerrr <immerrr@gmail.com>
- (a46e58c) Run wrap-and-sort script

* Tue Mar 17 2015 immerrr <immerrr@gmail.com>
- (6be0ffb) Update package control files

* Mon Mar 16 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (3987c63) Merge pull request #33 from raelgc/33-notifications-not-starting

* Mon Mar 16 2015 Rael <rael.gc@gmail.com>
- (0f93e4b) Fixing notifications (#33)

* Sun Mar 15 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (a87ae51) Update README.md

* Sun Mar 15 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (81dc0a8) Missing char.

* Sun Mar 15 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (ee4c7e8) Adding info about Debian and Precise

* Sun Mar 15 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (171aba2) Merge pull request #28 from StenSoft/master

* Sun Mar 15 2015 Jan Sten Adámek <sten@stensoft.com>
- (6f4a3ca) GObject introspection in Recommends (#27)

* Sat Mar 14 2015 Jan Sten Adámek <sten@stensoft.com>
- (872729e) Use auto-detection for Unity and Dbusmenu (#27)

* Sat Mar 14 2015 Jan Sten Adámek <sten@stensoft.com>
- (c2870ae) Moved packages that are not really required to Recommends (#27)

* Sat Mar 14 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (fd4a8f2) Merge pull request #26 from raelgc/26-trying-faster-javascript

* Sat Mar 14 2015 Rael <rael.gc@gmail.com>
- (bfad72e) Fixing startup error after minify JS (#26)

* Thu Mar 12 2015 Rael <rael.gc@gmail.com>
- (83377d3) Trying to speedup JS loading (#26)

* Thu Mar 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (856ef49) Merge pull request #16 from raelgc/16-count-in-systray

* Thu Mar 12 2015 Rael <rael.gc@gmail.com>
- (b268c9b) Removing some dark edges

* Thu Mar 12 2015 Rael <rael.gc@gmail.com>
- (7abc992) Merge branch 'master' of github.com:raelgc/scudcloud

* Thu Mar 12 2015 Rael <rael.gc@gmail.com>
- (2ec4854) Screenshot with systray

* Thu Mar 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (4798511) Updating with last systray features

* Thu Mar 12 2015 Rael <rael.gc@gmail.com>
- (6c335e4) Adding count to systray (#16)

* Thu Mar 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (d56dba0) More detailed description of message counter

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (931ef2e) New package release

* Wed Mar 11 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (3693c85) Merge pull request #24 from raelgc/24-add-gir1.2-unity-5.0-as-dependency

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (2aee5b3) Adding gir1.2-unity-5.0 as dependency (#24)

* Wed Mar 11 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (2dc770e) Adding some "Unity only" to features list.

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (e14f8ac) New package version

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (e54cba5) Fixing filterEvent (#23)

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (72bff0e) New package version

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (78d1555) Fixing alert (#23)

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (16065c7) New package version

* Wed Mar 11 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (790fde7) Merge pull request #23 from raelgc/23-alert-on-new-notifications

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (f98c8f1) Alert on new notifications (#23)

* Wed Mar 11 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (e2e98d9) Merge pull request #22 from raelgc/22-remove-qapplication.alert

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (d9785d2) Removing QApplication::alert (#22)

* Wed Mar 11 2015 Rael <rael.gc@gmail.com>
- (810e979) Trying to improve Notifications override

* Tue Mar 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (e82c672) Adding info about multiple teams

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (579fefa) Publishing changes to new package

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (751b531) Improving systray clicking (#17)

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (2396d0a) New package version

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (6e284bd) Simplifying Debian install file

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (6407c06) Fixing copyright

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (d7de938) Adding python3-dbus to control file (#20)

* Tue Mar 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (2b3afe5) Merge pull request #6 from raelgc/6-team-switch

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (a209ebe) Preventing other instances (#6)

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (c3c8bfc) Simple mark at current team (#6)

* Tue Mar 10 2015 Rael <rael.gc@gmail.com>
- (9ade82b) A simple left pane with team switcher (#6)

* Sun Mar 8 2015 Rael <rael.gc@gmail.com>
- (a6f6a07) Merge branch 'master' into 6-team-switch

* Sun Mar 8 2015 Rael <rael.gc@gmail.com>
- (734c00d) New package version

* Fri Mar 6 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (b227c60) Merge pull request #19 from syphernl/feature/fix_trayicon_cinnamon

* Fri Mar 6 2015 Frank Klaassen <frank@cloudright.nl>
- (23c9913) Fixes #17 - Support for leftclicks to restore/hide the tray icon

* Thu Mar 5 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (51982d3) Adding info about Kubuntu and Mint

* Thu Mar 5 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (e1f7423) Merge pull request #14 from raelgc/14-close-to-tray

* Thu Mar 5 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (759460b) Adding info about "Close to Tray" (#14)

* Thu Mar 5 2015 Rael <rael.gc@gmail.com>
- (e0ab967) Close to Tray (#14)

* Wed Mar 4 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (f5933e6) Merge pull request #13 from raelgc/13-dont-use-pyc

* Wed Mar 4 2015 Rael <rael.gc@gmail.com>
- (2acc63f) Generating compiled files during install (#13)

* Wed Mar 4 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (e4dab63) Merge pull request #12 from raelgc/12-add-support-to-other-des

* Wed Mar 4 2015 Rael <rael.gc@gmail.com>
- (6ef6e49) Adding support to other DEs (#12)

* Tue Mar 3 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (f103c18) Updating README with version and systray feature

* Tue Mar 3 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (674dd34) Merge pull request #8 from raelgc/8-tray-icon

* Tue Mar 3 2015 Rael <rael.gc@gmail.com>
- (ec2fe02) Fixing icon paths (#8)

* Tue Mar 3 2015 Rael <rael.gc@gmail.com>
- (d004868) Adding optional systray icon (#8)

* Sun Mar 1 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (e96eb71) Merge pull request #11 from raelgc/11-add-lato-font

* Sun Mar 1 2015 Rael <rael.gc@gmail.com>
- (78e0a27) Adding lato fonts (#11)

* Fri Feb 27 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (22042bb) Merge pull request #9 from raelgc/9-add-spell-checking

* Fri Feb 27 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (ce101ef) Better grammar on README (#9)

* Fri Feb 27 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (0b1b06a) Adding spell checking install instructions on README (#9)

* Fri Feb 27 2015 Rael <rael.gc@gmail.com>
- (ed280c9) Adding spell checking (#9)

* Fri Feb 27 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (dc7c654) Merge pull request #10 from raelgc/10-oauth-auth

* Fri Feb 27 2015 Rael <rael.gc@gmail.com>
- (53c3f3f) Adding support to google auth (#10)

* Wed Feb 25 2015 Rael <rael.gc@gmail.com>
- (fb9ab25) Fixing menus not enabled after change channel

* Wed Feb 25 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (0a5914d) Merge pull request #7 from raelgc/7-window-menus

* Wed Feb 25 2015 Rael <rael.gc@gmail.com>
- (d4c6554) Releasing new package (#7)

* Wed Feb 25 2015 Rael <rael.gc@gmail.com>
- (2218dfd) Sensitive menus (#7)

* Wed Feb 25 2015 Rael <rael.gc@gmail.com>
- (1419e5d) Sensitive menus (#7)

* Wed Feb 25 2015 Rael <rael.gc@gmail.com>
- (e6cad3a) Missing JS (#7)

* Wed Feb 25 2015 Rael <rael.gc@gmail.com>
- (1993d35) Adding menus (#7)

* Tue Feb 24 2015 Rael <rael.gc@gmail.com>
- (0741c73) Separating mainWindow from webView (#7)

* Tue Feb 24 2015 Rael <rael.gc@gmail.com>
- (3aa5808) New package

* Thu Feb 19 2015 Rael <rael.gc@gmail.com>
- (b0a3e46) Simple team switcher (#6)

* Wed Feb 18 2015 Rael <rael.gc@gmail.com>
- (f2ca659) New package

* Wed Feb 18 2015 Rael <rael.gc@gmail.com>
- (87dc279) Removing 'New message in ' from notification

* Wed Feb 18 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (97f00f4) Merge pull request #5 from raelgc/5-fix-quicklist

* Wed Feb 18 2015 Rael <rael.gc@gmail.com>
- (f8910c4) Fixing quicklist (#5)

* Wed Feb 18 2015 Rael <rael.gc@gmail.com>
- (6b9bca4) Releasing package

* Wed Feb 18 2015 Rael <rael.gc@gmail.com>
- (0548cf8) Some refactoring

* Wed Feb 18 2015 Rael <rael.gc@gmail.com>
- (4cdb2f6) Changing signin CSS to match OSX client

* Wed Feb 18 2015 Rael <rael.gc@gmail.com>
- (271d44c) Adding webkit debug console option

* Tue Feb 17 2015 Rael <rael.gc@gmail.com>
- (7ea7de5) Fixing package building after file renaming

* Tue Feb 17 2015 Rael <rael.gc@gmail.com>
- (d52ee5f) Some simple internal changes

* Tue Feb 17 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (0a56506) Merge pull request #4 from raelgc/4-copy-paste-images-like-chrome

* Tue Feb 17 2015 Rael <rael.gc@gmail.com>
- (fbd35b2) Copy and paste images (#4)

* Sun Feb 15 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (f5eaa30) Merge pull request #3 from raelgc/3-improve-first-signin

* Sun Feb 15 2015 Rael <rael.gc@gmail.com>
- (aad2b86) Improving first signin (#3)

* Sat Feb 14 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (d59cfe6) Some formatting.

* Sat Feb 14 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (068c99b) Adding info about the First Run

* Fri Feb 13 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (db5c40a) Fixing Slack name

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (3deaf98) Moving some code to proper place

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (477b8fa) Better screenshot

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (6a19c53) Some cleanup

* Thu Feb 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (c61b51d) Moving stuff

* Thu Feb 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (378cccb) Adding a screenshot with all

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (232b1e3) Merge branch 'master' of github.com:raelgc/scudcloud

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (ca8b81e) Adding a screenshot with all

* Thu Feb 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (605d9b2) Adding link to screenshots

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (e83f2f4) Adding logo to screenshots

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (8fb9b67) Adding screenshots

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (a06c58f) Adding # before channel in quicklist

* Thu Feb 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (91a08bb) Merge pull request #2 from raelgc/2-add-quicklist-for-channels

* Thu Feb 12 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (11a7e17) Adding channels quicklist as feature

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (3929680) New deb package (#2)

* Thu Feb 12 2015 Rael <rael.gc@gmail.com>
- (7ddded3) Adding quicklist for channels (#2)

* Wed Feb 11 2015 Rael <rael.gc@gmail.com>
- (fc9f492) Merge branch 'master' of github.com:raelgc/scudcloud

* Wed Feb 11 2015 Rael <rael.gc@gmail.com>
- (56c4d08) Improving .desktop file

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (01659f4) Linking MIT License to the one at this repo.

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (36e58ce) Removing placeholder title from icon.

* Tue Feb 10 2015 Rael <rael.gc@gmail.com>
- (8049e41) New .deb package with improvements

* Tue Feb 10 2015 Rael <rael.gc@gmail.com>
- (6092463) More deb files to .gitignore

* Tue Feb 10 2015 Rael <rael.gc@gmail.com>
- (76ced59) Adding deb package output files to .gitignore

* Tue Feb 10 2015 Rael <rael.gc@gmail.com>
- (9c6b319) Enable clipboard access by JS; Remove "New message from" at desktop notifications

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (d42d712) Merge pull request #1 from raelgc/1-open-links-in-default-system-program

* Tue Feb 10 2015 Rael <rael.gc@gmail.com>
- (bc96bec) Adding linkClicked handler (#1)

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (5d20c4c) Removing useless return statement

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (f55fc6a) Update README.md

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (2862ebe) Keep the same title as PPA

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (a53fd1c) Keep a pattern!

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (5f3dc8e) Adding License info.

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (e464c35) Fixing typo

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (9a9752d) Short title, pretty title

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (0fb79e7) Short title

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (acfd7b1) Adding clarification

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (ebde198) Adding description and instructions

* Tue Feb 10 2015 Rael <rael.gc@gmail.com>
- (6b559d5) Adding MainWindow source and debian package source

* Tue Feb 10 2015 Rael Gugelmin Cunha <rael.gc@gmail.com>
- (f7db7eb) Initial commit
