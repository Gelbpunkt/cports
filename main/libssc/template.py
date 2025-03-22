pkgname = "libssc"
pkgver = "0.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "protobuf-c-devel",
]
makedepends = [
    "glib-devel",
    "libqmi-devel",
    "protobuf-c-devel",
    "python-devel",
    "python-gobject",
]
pkgdesc = "Library to expose Qualcomm Sensor Core sensors"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/DylanVanAssche/libssc"
source = f"https://codeberg.org/DylanVanAssche/libssc/archive/v{pkgver}.tar.gz"
sha256 = "e6758330b7ba48019092aacf909a189977956fe96a0b767ab32da6773c479ef6"
# tests require running on-device or starting a mock server before
options = ["!check"]

@subpackage("libssc-devel")
def _(self):
    return self.default_devel()
