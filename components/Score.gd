extends Label

export (int) var paddingLength = 8

func _ready():
	update()

func reset():
	update()

func adjust(adjustment):
	global.score += adjustment
	update()

func update():
	$Label.text = ("%0*d" % [paddingLength, global.score])