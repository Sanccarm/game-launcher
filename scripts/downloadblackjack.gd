extends Button

var server_url = "http://127.0.0.1:8080/" #Url that poitns towards server serving the files
var files_to_download = ["BJVersion.txt", "BlackJack.exe"] # The game file and version file
var download_folder = "res://downloadedapps/" # static path to install files

func _ready():
	connect("pressed", self, "_on_button_pressed")

func _on_button_pressed():
	for file_name in files_to_download:
		download_file(file_name)

func download_file(file_name):
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed", [file_name])
	http_request.request(server_url + file_name)
	self.text = "Downloading: BlackJack.exe"  # Add debugging output"


func _on_request_completed(result, response_code, headers, body, file_name):
	if response_code == 200:
		var file_path = download_folder + file_name
		var file = File.new()
		file.open(file_path, File.WRITE)
		# Write binary data
		file.store_buffer(body)
		file.close()
		self.text = "Downloaded!"
	else:
		print("Error downloading file:", file_name, "Response code:", response_code)
	self.disabled = true # disables the button 


