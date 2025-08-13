pkgname = "ttyescape"
pkgver = "1.0.2"
pkgrel = 0
depends = ["hkdm", "buffyboard"]
pkgdesc = "Collection of tools for allowing mobile users to switch to a TTY"
license = "GPL-2.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/ttyescape"
source = f"{url}/-/archive/{pkgver}/ttyescape-{pkgver}.tar.gz"
sha256 = "01115a78e3abcd19846f3591a5facf8a14e204d694a69e62468f32d3381537a7"


def install(self):
    self.install_bin("togglevt.sh")
    self.install_file(
        "ttyescape-hkdm.toml", "etc/hkdm/config.d", name="ttyescape.toml"
    )
