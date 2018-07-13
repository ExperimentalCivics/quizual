extends Control

func _ready():
	$GUI/CenterContainer/VBoxContainer/Score.adjust(1)
	Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)

func _input(event):
	if event.is_action_pressed('button_1'):
		get_tree().change_scene("res://StartScreen.tscn")
	if event.is_action_pressed('button_2'):
		get_tree().change_scene("res://StartScreen.tscn")
	if event.is_action_pressed('button_3'):
		get_tree().change_scene("res://StartScreen.tscn")
	if event.is_action_pressed('button_enter'):
		get_tree().change_scene("res://StartScreen.tscn")