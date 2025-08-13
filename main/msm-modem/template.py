pkgname = "msm-modem"
pkgver = "8"
pkgrel = 0
depends = ["libqmi", "rmtfs"]
pkgdesc = "Common support for Qualcomm MSM modems"
license = "GPL-3.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/pmaports/-/tree/master/modem/msm-modem"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        self.files_path / "msm-modem-uim-selection.sh",
        name="msm-modem-uim-selection",
    )
    self.install_service(self.files_path / "msm-modem-uim-selection")
    self.install_sysusers(self.files_path / "sysusers.conf")
