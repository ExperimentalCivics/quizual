extends Timer

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass

func _on_Timer_timeout():
	get_tree().change_scene("res://StartScreen.tscn")