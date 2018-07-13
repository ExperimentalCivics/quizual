extends Control

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)

func _input(event):
	if event.is_action_pressed('answer_2'):
		get_tree().change_scene("res://Quiz-correct-1.tscn")
	if event.is_action_pressed('answer_1'):
		get_tree().change_scene("res://Quiz-false-1.tscn")