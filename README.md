# Cooler Control — Raspberry Pi

Controle automatico do cooler da CPU do Raspberry Pi via GPIO, baseado na
temperatura do processador.

## Ligações

| Componente | Pino do Raspberry (BCM) | Observação |
|---|---|---|
| Cooler (via transistor/relé) | GPIO 17 | `active_high=True`: nível alto liga o cooler |

## Instalação

```bash
sudo apt update
sudo apt install -y python3-gpiozero python3-lgpio
```

```bash
git clone https://github.com/rtavares-g/cooler-control.git ~/cooler-control
cd ~/cooler-control
```

Se quiser ajustar as temperaturas de ligar/desligar, edite as constantes no
início de `cooler-control.py`:

```python
GPIO_COOLER = 17
TEMP_LIGAR = 55.0
TEMP_DESLIGAR = 45.0
INTERVALO = 5
```

Teste sem instalar como serviço:

```bash
python3 cooler-control.py
```

## Serviço automático

Use o script de instalação, que copia o `.service` para o systemd e ativa
o serviço:

```bash
./install.sh
```

Isso equivale a:

```bash
sudo cp cooler-control.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now cooler-control
```

## Comandos úteis

```bash
systemctl status cooler-control
journalctl -u cooler-control -f
sudo systemctl restart cooler-control
```

## Reinstalar (ex: cartão SD novo)

```bash
git clone https://github.com/rtavares-g/cooler-control.git ~/cooler-control
cd ~/cooler-control
./install.sh
```
