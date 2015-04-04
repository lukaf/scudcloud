SCUDCLOUD_VERSION = 1.0.21

default: fetch package

fetch:
	curl -s -L -o rpmbuild/SOURCES/v$(SCUDCLOUD_VERSION).tar.gz https://github.com/raelgc/scudcloud/archive/v$(SCUDCLOUD_VERSION).tar.gz

package:
	rpmbuild --define '_topdir $(pwd)' --define "SCUDCLOUD_VERSION $(SCUDCLOUD_VERSION)" -bb rpmbuild/SPECS/scudcloud.spec
