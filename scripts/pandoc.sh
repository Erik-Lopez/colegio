#!/bin/sh

printf '%s' "$1" | pandoc -f markdown -t html
