pkgname = "mobile-config-firefox"
pkgver = "4.6.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["FIREFOX_DIR=/usr/lib/firefox"]
depends = ["firefox"]
pkgdesc = "Firefox tweaks for mobile and privacy"
license = "GPL-3.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/mobile-config-firefox"
source = f"{url}/-/archive/{pkgver}/mobile-config-firefox-{pkgver}.tar.gz"
sha256 = "3bf2f2db0de74a0e4a5a38c22128788799ba5ad3e5deed167a4b37b13cd05795"
# no tests
options = ["!check"]
