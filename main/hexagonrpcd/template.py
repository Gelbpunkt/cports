pkgname = "hexagonrpcd"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
pkgdesc = "Qualcomm HexagonFS daemon"
license = "GPL-3.0-or-later"
url = "https://github.com/linux-msm/hexagonrpc"
source = f"https://github.com/linux-msm/hexagonrpc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fe742549a2672902d59a90dafd741a9a0acbeca059e07ff5130e2b525a66574f"


def post_install(self):
    self.install_bin(self.files_path / "hexagonrpcd-wrapper")
    self.install_file(self.files_path / "10-fastrpc.rules", "usr/lib/udev/rules.d")
    self.install_service(self.files_path / "hexagonrpcd")
    self.install_sysusers(self.files_path / "sysusers.conf")
