#!/bin/bash
mv httpinglib/ /usr/local/lib/
echo "Installed libraries"
touch httping
echo python3 /usr/local/lib/httpinglib/main.py >> httping
echo "Created excecutable"
chmod +x httping
mv httping /usr/local/bin/
echo "Installed excecutable"
