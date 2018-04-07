SquarePanocut allows to cut panorama into squares. This is helpful for creating Instagram swipeable posts.

Requirements:

  brew install python3
  pip3 install pillow

Usage:
  python3 squarepanocut.py panorama.jpg
  python3 squarepanocut.py panorama.jpg left|right|center

Last parameter defines which part of original panorama will be covered by resulting parts. Default value is 'left'. Total loss will be less than 1 image height.")
