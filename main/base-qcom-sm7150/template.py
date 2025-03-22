pkgname = "base-qcom-sm7150"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
depends = [
    "!base-full-firmware",  # We only want QCOM firmware files
    "base-softkeyboard",
    "bootmac",
    "firmware-google-sunfish",
    "firmware-linux-qca",
    "firmware-linux-qcom",
    "firmware-qcom-sm7150-ath10k",
    "firmware-xiaomi-davinci",
    "firmware-xiaomi-surya",
    "hexagonrpcd",
    "initramfs-tools-growrootfs",
    "linux-qcom-sm7150",
    "msm-modem",
    "qbootctl",
    "systemd-boot",
    "tqftpserv",
]
pkgdesc = "Chimera base package for Qualcomm SM7150"
license = "custom:none"
url = "https://chimera-linux.org"
broken_symlinks = ["usr/lib/dinit.d/boot.d/*"]
options = ["!autosplit"]


def install(self):
    self.install_file(
        self.files_path / "51-disable-suspension.conf",
        "usr/share/wireplumber/wireplumber.conf.d",
    )
    self.install_file(
        self.files_path / "81-libssc-180-degrees.rules", "usr/lib/udev/rules.d"
    )
    self.install_file(self.files_path / "cmdline", "usr/lib/systemd/boot")
    (self.destdir / "usr/lib/systemd/boot/relax-esp").touch()
    self.install_initramfs(self.files_path / "gpu_firmware")
    self.install_dir("usr/lib/dinit.d/boot.d")
    # TODO: We can have the bootmac udev rules trigger a bootmac service instead of using RUN
    # and perhaps then have that depend on bluetoothd? Not entirely sure.
    self.install_link(
        "usr/lib/dinit.d/boot.d/bluetoothd",
        "../bluetoothd",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/hkdm",
        "../hkdm",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/iio-sensor-proxy",
        "../iio-sensor-proxy",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/msm-modem-uim-selection",
        "../msm-modem-uim-selection",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/qbootctl",
        "../qbootctl",
    )
    self.install_link(
        "usr/lib/dinit.d/boot.d/tqftpserv",
        "../tqftpserv",
    )
    self.install_file(
        self.files_path / "60-dtb-symlink.sh", "usr/lib/kernel.d", mode=0o755
    )
