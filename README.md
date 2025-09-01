# Qubes Auto Credit2

[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html) 

## Description

This script is designed for QubesOS. It makes use of the `credit2-weight` feature to automatically set [credit2 scheduler weight](https://wiki.xenproject.org/wiki/Credit2_Scheduler) (scheduling priority) for VMs.

## Usage

1. Download `auto-credit2.service` and `auto_credit2.py` and copy it over to `dom0`
2. Inside `dom0` copy the service file to `/etc/systemd/system` and the Python script to `/usr/local/bin`
3. Also inside `dom0`, execute `sudo chmod +x /usr/local/bin/auto_credit2.py; sudo systemctl daemon-reload && sudo systemctl
   enable --now auto-credit2`.
4. For each VM whose scheduling priority you want to modify, execute (in `dom0`): `qvm-features VMNAME credit2-weight WEIGHT`

The default `WEIGHT` is 256. Setting `WEIGHT` higher, e.g. to 512, will make the VM scheduled for execution 2x more often (if the CPU is completely busy and there's contention for resources). Setting `WEIGHT` lower makes the VM less likely to be scheduled.

The script also sets `dom0`'s weight to `1024`, for improved performance.

Weight recommendations:
- `dom0`: 512 or 1024
- `sys-audio`: 4096 or 8192
- `gaming`: 2048
- Any Qubes with video/audio calling: 2048 or 4096
- Qubes running low-priority background processes: `64` or lower

## Credits

Most of the structure of the script is inspired by @noskb and @renehoj's CPU pinning script.

## Other Utilities

See [the qubes-utils repo](https://github.com/Atrate/qubes-utils) for links to other utilities I've written for Qubes.

## License
This project is licensed under the [AGPL-3.0-or-later](https://www.gnu.org/licenses/agpl-3.0.html).

[![License: AGPLv3](https://www.gnu.org/graphics/agplv3-with-text-162x68.png)](https://www.gnu.org/licenses/agpl-3.0.html)
