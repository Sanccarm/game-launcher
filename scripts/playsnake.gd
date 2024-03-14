extends Node

var downloads = "res://downloadedapps/"
var snake_game = "/main.exe"
var version = "/version.txt"

# Called when the node enters the scene tree for the first time.
func _ready():
	_process(5)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if is_version_and_snake_present():
		self.disabled = false
	else:
		self.disabled = true

# Function to check if both version and snake_game are present in downloads
func is_version_and_snake_present() -> bool:
	return version_exists() && snake_game_exists()

# Function to check if version file exists in downloads
func version_exists() -> bool:
	return File.new().file_exists(downloads + version)

# Function to check if snake_game file exists in downloads
func snake_game_exists() -> bool:
	return File.new().file_exists(downloads + snake_game)

# Function to launch the game
func _on_Button2_pressed():
	if is_version_and_snake_present():
		var process = OS.execute(downloads + snake_game, [])
		if process == OK:
			# Game launched successfully
			pass
		else:
			# Failed to launch game
			print("Failed to launch game.")
	else:
		print("Version and snake game files are not present.")
