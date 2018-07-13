extends Control

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)

func _input(event):
	if event.is_action_pressed('button_1'):
		get_tree().change_scene("res://wrong.tscn")
	if event.is_action_pressed('button_2'):
		get_tree().change_scene("res://wrong.tscn")
	if event.is_action_pressed('button_3'):
		get_tree().change_scene("res://correct.tscn")
