#!/bin/sh

KERNVER=$(linux-version list|linux-version sort|tail -n1)

[ -z "$KERNVER" ] && exit 0

echo "Creating ${KERNVER} dtb symlink for U-Boot EFI..."

ln -sf "dtbs/dtbs-${KERNVER}" /boot/dtb
