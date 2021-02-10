class Tile:
    """
    A tile on a map. It may or may not be passable, and may or may not block sight.
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # By default, if a tile is not passable, it also blocks vision
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
