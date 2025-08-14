pkgname = "firmware-xiaomi-davinci"
pkgver = "20250623"
pkgrel = 0
archs = ["aarch64"]
pkgdesc = "Nonfree firmware blobs for Xiaomi Mi 9T / Redmi K20"
license = "custom:proprietary"
url = "https://github.com/sm7150-mainline/firmware-xiaomi-davinci"
_commit = "6532694920dd05ee7d930fe6d3ede74d2b9ea60d"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "c09aeca3d0a614e6f48b0fdf8f6d8f63be8f3719c8604a81edc5e8cebc0a5c0e"
options = ["!distlicense", "!strip", "execstack", "foreignelf"]


def post_extract(self):
    self.mv("lib", "usr/lib")
    # The files are in usr/share, we want them in usr/lib/firmware/hexagonfs
    self.mv("usr/share", "usr/lib/firmware/hexagonfs")

def install(self):
    for f in self.cwd.rglob("*"):
        if f.is_file():
            self.install_file(f, f.relative_to(self.cwd).parent)
