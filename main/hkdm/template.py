pkgname = "hkdm"
pkgver = "0.2.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf"
]
makedepends = [
    "libevdev-devel",
    "rust-std"
]
pkgdesc = "Lighter-weight hotkey daemon"
license = "GPL-2.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/hkdm"
source = f"{url}/-/archive/{pkgver}/hkdm-{pkgver}.tar.gz"
sha256 = "0ae19ee83be1d843958dd2bcba07c17359abdf1e63f1862ca9ee8e979bafd9eb"


def post_install(self):
    self.install_file("hkdm.example.toml", "etc/hkdm/config.d/hkdm.toml.example")
    self.install_service(self.files_path / "hkdm")
