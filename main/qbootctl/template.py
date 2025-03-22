pkgname = "qbootctl"
pkgver = "0.2.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
pkgdesc = "Tool for interacting with Android A/B slots"
license = "GPL-3.0-or-later"
url = "https://github.com/linux-msm/qbootctl"
source = f"https://github.com/linux-msm/qbootctl/archive/{pkgver}.tar.gz"
sha256 = "e66b361f86fac413f6a96974b4045a1fbc385f9eb6cee7fa8a26e0ca77c74a51"


def post_install(self):
    self.install_service(self.files_path / "qbootctl")
