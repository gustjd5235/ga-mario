import retro
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

# https://datacrystal.romhacking.net/wiki/Super_Mario_Bros.:RAM_map
# 0x0500-0x069F	Current tile (Does not effect graphics)
full_screen_tiles = ram[0x0500:0x069F+1]

full_screen_tile_count = full_screen_tiles.shape[0]

full_screen_page1_tile = full_screen_tiles[:full_screen_tile_count//2].reshape((13, 16))
full_screen_page2_tile = full_screen_tiles[full_screen_tile_count//2:].reshape((13, 16))

full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

print(full_screen_tiles)

current_screen_page = ram[0x071A]

screen_position = ram[0x071C]

screen_offset = (256 * current_screen_page + screen_position) % 512

screen_tile_offset = screen_offset // 16

screen_tiles = np.concatenate((full_screen_tiles, full_screen_tiles), axis=1)[:, screen_tile_offset:screen_tile_offset+16]

print(screen_tiles)