pkgname = "tqftpserv"
pkgver = "1.1_git20251224"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "qrtr-devel",
    "zstd-devel",
]
pkgdesc = "Trivial File Transfer Protocol server over AF_QIPCRTR"
license = "BSD-3-Clause"
url = "https://github.com/linux-msm/tqftpserv"
_commit = "0ed681362b6f7ac7381e0320501823be6d843006"
source = f"https://github.com/linux-msm/tqftpserv/archive/{_commit}.tar.gz"
sha256 = "b2bdc576489ac0cbbc76b9f1b1aa0abe2cbcb992625f88a49564d45572327d61"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "tqftpserv")
