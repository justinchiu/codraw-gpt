#!/bin/bash

conda deactivate
tmux new-session -s "codraw" -n "root" "tmux source-file tmux/session"
