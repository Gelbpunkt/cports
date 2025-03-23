pkgname = "bootmac"
pkgver = "0.6.0"
pkgrel = 0
depends = ["bluez"]
pkgdesc = "Configure MAC addresses generated from serial numbers at boot"
license = "GPL-3.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/bootmac"
source = f"https://gitlab.postmarketos.org/postmarketOS/bootmac/-/archive/v{pkgver}/bootmac-v{pkgver}.tar.gz"
sha256 = "f37fa933e689a1a8914c18a19e46b0af4238f84ed0a4f38f04bcab857c8b602b"


def install(self):
    self.install_bin("bootmac")
    self.install_file(
        "bootmac-bluetooth.rules",
        "usr/lib/udev/rules.d",
        name="90-bootmac-bluetooth.rules",
    )
    self.install_file(
        "bootmac-wifi.rules",
        "usr/lib/udev/rules.d",
        name="90-bootmac-wifi.rules",
    )
