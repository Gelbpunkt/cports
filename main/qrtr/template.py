pkgname = "qrtr"
pkgver = "1.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["linux-headers"]
pkgdesc = "Userspace reference for net/qrtr in the Linux kernel"
license = "BSD-3-Clause"
url = "https://github.com/linux-msm/qrtr"
source = f"https://github.com/linux-msm/qrtr/archive/v{pkgver}/qrtr-v{pkgver}.tar.gz"
sha256 = "7a82bf80246fe71287b13c66c0466208822e8337fcd4aaf302eee6c5fcb48a52"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("qrtr-devel")
def _(self):
    return self.default_devel()
