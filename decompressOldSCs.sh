find ../cr-sc-dump/old/ -name "*.png" | sed 's/.*\/\([^\/]*\.\)png$/\1sc/g' | xargs -I ^ find ../Sc-Assets-Downloader/ -name ^ | xargs python3 Main.py -lzma
