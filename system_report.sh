#!/usr/bin/env bash
set -euo pipefail

threshold="${DISK_WARN_PERCENT:-80}"
echo "=== System Report ==="
echo "Date: $(date)"
echo "Host: $(hostname)"
echo "User: $(id -un)"
echo "Uptime: $(uptime -p 2>/dev/null || uptime)"
echo
if command -v df >/dev/null 2>&1; then
  df -h
  usage="$(df -P / | awk 'NR==2 {gsub(/%/, "", $5); print $5}')"
  if [[ "$usage" =~ ^[0-9]+$ ]] && (( usage >= threshold )); then
    echo "WARNING: root filesystem usage is ${usage}% (threshold ${threshold}%)." >&2
    exit 1
  fi
else
  echo "df command not available" >&2
  exit 2
fi
