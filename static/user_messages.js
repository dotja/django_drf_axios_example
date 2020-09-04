function read(msg_id) {
	let elem = document.getElementById(msg_id);
	elem.style.color = '#9e9e9e';
	let data = {msg_id: msg_id, action: 'read'};
	console.log(data);
	edit_msg(data);
}

function unread(msg_id) {
	let elem = document.getElementById(msg_id);
	elem.style.color = 'black';
	let data = {msg_id: msg_id, action: 'unread'};
	edit_msg(data);
}

function edit_msg(data) {
	let req = axios({
		method: 'post',
		url: '/api/edit_message/',
		xstfCookieName: 'csrftoken',
		xsrfHeaderName: 'X-CSRFToken',
		data: data,
		headers: {
			'X-CSRFToken': 'csrftoken'
		}
	}).then((response) => {
		this.msg = response.data;
		console.log('response');
	});
	return;
}

