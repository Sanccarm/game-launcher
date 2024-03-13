extends Button

var server_url = "http://127.0.0.1:8080/"
var files_to_download = ["version.txt", "main.exe"]
var download_folder = "res://downloadedapps/"

func _ready():
	connect("pressed", self, "_on_button_pressed")
	set_text("Check Download")  # Set initial button text

func _on_button_pressed():
	var all_files_downloaded = true
	var version_match = true

	for file_name in files_to_download:
		if not file_exists(file_name):
			all_files_downloaded = false
			break

	if all_files_downloaded:
		version_match = check_version_match()
	else:
		set_text("Downloading... Please wait")  # Update button text while downloading

	if all_files_downloaded and version_match:
		set_text("Start Game")
		# Connect button press to launch game function
		connect("pressed", self, "_launch_game")
	elif all_files_downloaded and not version_match:
		set_text("Version Mismatch")

func check_version_match():
	# Read the local version file
	var local_version = load_version()
	# Request the remote version file
	var remote_version = get_remote_version()

	return local_version == remote_version

func load_version():
	var version_path = download_folder + "version.txt"
	var file = File.new()
	if file.open(version_path, File.READ) == OK:
		var version = file.get_line().strip()  # Assuming version.txt contains only one line
		file.close()
		return version
	else:
		return ""

func get_remote_version():
	var http_request = HTTPRequest.new()
	http_request.wait_for_response = true
	http_request.request(server_url + "version.txt")
	if http_request.get_response_code() == 200:
		return http_request.get_response_body_as_text().strip()
	else:
		return ""

func _launch_game():
	var file_path = download_folder + "main.exe"
	OS.execute(file_path, [])

func file_exists(file_name):
	var file = File.new()
	var exists = file.file_exists(download_folder + file_name)
	file.close()
	return exists
