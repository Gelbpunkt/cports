pkgname = "make-dynpart-mappings"
pkgver = "10.2.4"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = [
    "lvm2-devel",
    "openssl3-devel",
    "util-linux-blkid-devel",
]
pkgdesc = "Make block devices using the device mapper based on dynamic partitions"
license = "GPL-3.0-only"
url = "https://gitlab.com/flamingradian/make-dynpart-mappings"
source = f"https://gitlab.com/flamingradian/make-dynpart-mappings/-/archive/{pkgver}/make-dynpart-mappings-{pkgver}.tar.gz"
sha256 = "efda3dfc781cc3582e218a7b7d9618be599eb3b484c167e17873255ddf9ae527"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("make-dynpart-mappings")
    self.install_initramfs(self.files_path / "make_dynpart_mappings")
