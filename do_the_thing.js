// Reading files through Javascript can create vulnerabilities -
// find out more about this

window.onload = function() {
    var fileInput = document.getElementById('fileInput');
	var fileDisplayArea = document.getElementById('fileDisplayArea');

	fileInput.addEventListener('change', function(e) {
		var file = fileInput.files[0];
        //var otherfile = fopen('C:\Users\Elizabeth\Desktop\rivulets\cake.txt', 0);
        window.alert(file);
		var textType = /text.*/;

		if (file.type.match(textType)) {
			var reader = new FileReader();

			reader.onload = function(e) {
				fileDisplayArea.innerText = reader.result;
                window.alert(reader.result);
	
			}

			reader.readAsText(file);	
		} else {
			fileDisplayArea.innerText = "File not supported!";
		}
	});
}
