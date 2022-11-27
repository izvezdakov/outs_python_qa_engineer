import os
from subprocess import run
from enum import IntEnum
from datetime import datetime


class PsAuxRows(IntEnum):
        USER = 0
        PID = 1
        CPU = 2
        MEM = 3
        VSZ = 4
        RSS = 5
        TTY = 6
        STAT = 7
        START = 8
        TIME = 9
        COMMAND = 10


def parse_ps_aux_out(stdout: str):
    m = []
    for l in str.splitlines(stdout)[1:]:
        g = l.split()
        a = {}
        for t in range(11):
            if t == 10:  # last column could contain spaces
                s = ' '.join(g[t:])
            else:
                s = g[t]
            a.update(
                {
                    PsAuxRows(t).name : s
                }
            )
        m.append(a)
    return m


def calculate_statistic(info: list):
    out_str = 'Отчёт о состоянии системы:\n'
    users = set(el[PsAuxRows.USER.name] for el in info)
    out_str += f'Пользователи системы: {",".join(users)}\n'
    out_str += f'Процессов запущено: {len(info)}\n'
    out_str += 'Пользовательских процессов:\n'
    for u in users:
        out_str += f'{u}: {len(list(filter(lambda x: x[PsAuxRows.USER.name] == u, info)))}\n'
    out_str += f'Всего памяти используется: {sum(float(m[PsAuxRows.MEM.name]) for m in info)}%\n'
    out_str += f'Всего CPU используется: {sum(float(m[PsAuxRows.CPU.name]) for m in info)}%\n'
    out_str += f'Больше всего памяти использует: {str(sorted(info, key=lambda x: float(x[PsAuxRows.MEM.name]), reverse= True)[0][PsAuxRows.COMMAND.name])[:20]}\n'
    out_str += f'Больше всего CPU использует: {str(sorted(info, key=lambda x: float(x[PsAuxRows.CPU.name]), reverse=True)[0][PsAuxRows.COMMAND.name])[:20]}\n'
    return out_str

stat = calculate_statistic(parse_ps_aux_out(run(['ps', 'aux'], capture_output=True, text=True).stdout))
print(stat)
with open(f'{datetime.now()}-scan.txt', 'w') as f:
    f.write(stat)    
