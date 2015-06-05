# rivulets

This project is intended to simulate how droplets of water might wear down
tracks into a dirt slope.

I think Pygame could be useful for this.

Represent the slope as a grid with the top of the slope as the top of the
screen.

When sending a drop down the slope, randomly select the start position. The
drop can go west, east, southwest, south, or southeast. In other words, it can
go anywhere but back up the slope.

x x x
o d o
o o o

The grid will be represented by numbers where a tile's number represents how
likely the drop would be to choose that tile next. The higher the number, the
more likely the drop would choose that tile next.

Idea: weight southwest, south, and southeast higher than west and east