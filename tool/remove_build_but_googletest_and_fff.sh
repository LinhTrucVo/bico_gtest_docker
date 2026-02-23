# remove whole _build folder but googletest folder -> do not build googletest again
echo "=== Remove build folder but googletest and fff==="
cd /workspaces/bico_gtest_docker && \
mv _build/googletest /tmp/googletest_backup 2>/dev/null || true && \
mv _build/fff /tmp/fff_backup 2>/dev/null || true && \
rm -rf _build && \
mkdir -p _build && \
mv /tmp/googletest_backup _build/googletest 2>/dev/null || true
mv /tmp/fff_backup _build/fff 2>/dev/null || true
