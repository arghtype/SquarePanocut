SquarePanocut allows to cut panorama into squares (1x1) or portraits (4x5). This is helpful for creating Instagram swipeable posts.

####Requirements
  `brew install python3`
  
  `pip3 install pillow`

####Usage
  `python3 squarepanocut.py panorama.jpg` - default run, just slice pano into squares.
  
  `python3 squarepanocut.py panorama.jpg MODE` : MODE defines which part of original panorama will be covered by resulting parts. Possible values are `left`,`right`,`center`,  default  is `left`. Total loss will be less than 1 image height.
  
  `python3 squarepanocut.py panorama.jpg MODE p` : `p` flag is used to create portrait mode panorama - all resulting parts will be in 4x5 portrait format.
  
