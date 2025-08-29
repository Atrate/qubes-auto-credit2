#!/usr/bin/env python3

import asyncio
import subprocess

import qubesadmin
import qubesadmin.events

feat_sched = "credit2-weight"

def _sched_credit2(name, weight):
    cmd = ['xl', 'sched-credit2', '-d', name, '-w', weight]
    subprocess.run(cmd).check_returncode()

def sched_by_feat(vm, event, **kwargs):
    vm = app.domains[str(vm)]
    if feat_sched in list(vm.features):
        try:
            weight = int(vm.features["credit2-weight"])
            _sched_credit2(vm.name, str(weight))
            print(f'Set {vm.name}\'s credit2 weight to {weight}')
        except:
            pass

_sched_credit2("Domain-0", "1024")
app = qubesadmin.Qubes()
dispatcher = qubesadmin.events.EventsDispatcher(app)
dispatcher.add_handler('domain-start', sched_by_feat)
asyncio.run(dispatcher.listen_for_events())
