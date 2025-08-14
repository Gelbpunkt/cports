pkgname = "firmware-xiaomi-surya"
pkgver = "20250623"
pkgrel = 0
archs = ["aarch64"]
pkgdesc = "Nonfree firmware blobs for Xiaomi POCO X3 / POCO X3 NFC"
license = "custom:proprietary"
url = "https://github.com/sm7150-mainline/firmware-xiaomi-surya"
_commit = "26ecffbe095b05e396872c8e6bb9e0fff09e25aa"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "85b7bb1e26479631c457442af8cc648778e2734bf9a3e728ddd1f6263f20cb9a"
options = ["!distlicense", "!strip", "execstack", "foreignelf"]


def post_extract(self):
    self.mv("lib", "usr/lib")
    # The files are in usr/share, we want them in usr/lib/firmware/hexagonfs
    self.mv("usr/share", "usr/lib/firmware/hexagonfs")

def install(self):
    for f in self.cwd.rglob("*"):
        if f.is_file():
            self.install_file(f, f.relative_to(self.cwd).parent)
