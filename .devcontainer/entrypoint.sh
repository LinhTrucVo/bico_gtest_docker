#!/bin/bash

# Unset git proxy configurations
git config --global --unset http.proxy || true
git config --global --unset https.proxy || true