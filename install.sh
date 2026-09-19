#!/bin/bash
# Instala/reinstala o controle automatico do cooler como servico systemd.
# Uso: ./install.sh   (rodar de dentro da pasta clonada do repositorio)

set -e

REPO_URL="https://github.com/rtavares-g/cooler-control.git"
INSTALL_DIR="$HOME/cooler-control"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$SCRIPT_DIR" != "$INSTALL_DIR" ]; then
    if [ ! -d "$INSTALL_DIR" ]; then
        git clone "$REPO_URL" "$INSTALL_DIR"
    fi
    cd "$INSTALL_DIR"
else
    cd "$SCRIPT_DIR"
fi

sudo cp cooler-control.service /etc/systemd/system/cooler-control.service
sudo systemctl daemon-reload
sudo systemctl enable --now cooler-control

systemctl status cooler-control --no-pager
