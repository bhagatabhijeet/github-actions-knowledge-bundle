#!/usr/bin/env bash
# Chapter 4 companion script.
# Walkthrough: 04-github-actions-core-components/07-executing-shell-scripts.md
#
# Installs cowsay, draws a dragon, checks the file and shows it.
set -euo pipefail

echo "::group::Install cowsay"
sudo apt-get install -y -qq cowsay
echo "::endgroup::"

cowsay -f dragon "Run for cover, I am a DRAGON....RAWR" > dragon.txt

grep -i "dragon" dragon.txt > /dev/null
echo "✅ dragon.txt contains a dragon"

cat dragon.txt
ls -ltra
