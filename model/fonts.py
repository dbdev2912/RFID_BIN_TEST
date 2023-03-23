FAMILY = "UTM Avo"

class Fonts:
	def __init__( self ):
		self.x_small	= Font( FAMILY, 9 ).get_font()
		self.small 		= Font( FAMILY, 11 ).get_font()
		self.normal 	= Font( FAMILY, 13 ).get_font()
		self.medium 	= Font( FAMILY, 17 ).get_font()
		self.large 		= Font( FAMILY, 21 ).get_font()
		self.x_large 	= Font( FAMILY, 33 ).get_font()

		self.x_small_bold	= Font( FAMILY, 9, 'bold' ).get_font()
		self.small_bold	 	= Font( FAMILY, 11, 'bold' ).get_font()
		self.normal_bold	= Font( FAMILY, 13, 'bold' ).get_font()
		self.medium_bold	= Font( FAMILY, 17, 'bold' ).get_font()
		self.large_bold	 	= Font( FAMILY, 21, 'bold' ).get_font()
		self.x_large_bold	= Font( FAMILY, 33, 'bold' ).get_font()


class Font:
	def __init__(self, family, size, style=""):
		self.family = family
		self.size = size
		self.style = style

	def get_font(self):
		return ( self.family, self.size, self.style )


__all__ = [ 'Fonts' ]