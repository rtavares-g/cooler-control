#!/usr/bin/env python3

import time
import signal
import sys
from pathlib import Path
from gpiozero import OutputDevice  # type: ignore[import-untyped]


# =========================
# CONFIGURACAO
# =========================

GPIO_COOLER = 17

TEMP_LIGAR = 55.0
TEMP_DESLIGAR = 45.0

INTERVALO = 5

TEMP_FILE = Path(
    "/sys/class/thermal/thermal_zone0/temp"
)


# =========================
# GPIO
# =========================

cooler = OutputDevice(
    GPIO_COOLER,
    active_high=True,
    initial_value=False
)

cooler_ligado = False


# =========================
# FUNCOES
# =========================

def ler_temperatura():
    valor = TEMP_FILE.read_text().strip()
    return int(valor) / 1000.0


def encerrar(signum=None, frame=None):
    print(
        "Encerrando controle do cooler...",
        flush=True
    )

    cooler.off()
    cooler.close()

    sys.exit(0)


signal.signal(
    signal.SIGTERM,
    encerrar
)

signal.signal(
    signal.SIGINT,
    encerrar
)


# =========================
# INICIO
# =========================

print(
    "Controle automatico do cooler iniciado",
    flush=True
)

print(
    f"Liga em >= {TEMP_LIGAR:.1f} C",
    flush=True
)

print(
    f"Desliga em <= {TEMP_DESLIGAR:.1f} C",
    flush=True
)


# =========================
# LOOP
# =========================

while True:

    try:

        temperatura = ler_temperatura()

        print(
            f"CPU: {temperatura:.1f} C | "
            f"Cooler: {'ON' if cooler_ligado else 'OFF'}",
            flush=True
        )

        if (
            temperatura >= TEMP_LIGAR
            and not cooler_ligado
        ):

            cooler.on()
            cooler_ligado = True

            print(
                f"{temperatura:.1f} C - COOLER LIGADO",
                flush=True
            )

        elif (
            temperatura <= TEMP_DESLIGAR
            and cooler_ligado
        ):

            cooler.off()
            cooler_ligado = False

            print(
                f"{temperatura:.1f} C - COOLER DESLIGADO",
                flush=True
            )

        time.sleep(
            INTERVALO
        )

    except Exception as erro:

        print(
            f"Erro: {erro}",
            flush=True
        )

        time.sleep(
            INTERVALO
        )
