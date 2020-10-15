#!/bin/bash

RATEFILE="exchange_rate.txt"

main() {
    cd "$(dirname "$0")"
    local rate=$(PYTHONIOENCODING=utf-8 .rate/bin/python exchange.py)
    echo "$(date "+%Y%m%d-%H%M%S") ${rate}" > "${RATEFILE}"
}

main $@
