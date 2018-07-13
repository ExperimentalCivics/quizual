extends Control

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	#var my_rand = randi()%11+1
	var my_rand = randi()%11+1
	if my_rand < 5:
		get_tree().change_scene("res://quiz-1.tscn")
	elif my_rand > 4:
		get_tree().change_scene("res://quiz-2.tscn")