#!/bin/bash
# Papan teks di dalam Terminal, untuk direkam. Pakai: bash adegan.sh 3
declare -a T=(
""
"Scene 1  ·  This is our site, oldmoneypicks.com — privacy policy linked in the footer."
"Scene 2  ·  Our Pinterest app, with the redirect URI registered."
"Scene 3  ·  Full OAuth flow — consent, redirect to our local callback, code exchanged for a token."
"Scene 4  ·  Three live API calls: user account, boards, and pins on a board."
"Scene 5  ·  Pin creation works; production is closed to Trial apps. That is what we are requesting."
)
n="${1:-1}"; teks="${T[$n]}"
lebar=$(( ${#teks} + 4 ))
garis=$(printf '─%.0s' $(seq 1 $lebar))
clear
printf '\n  ╭%s╮\n' "$garis"
printf '  │  %s  │\n' "$teks"
printf '  ╰%s╯\n\n' "$garis"
