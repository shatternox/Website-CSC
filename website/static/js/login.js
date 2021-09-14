function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

async function init(){
	document.body.scrollIntoView()
	document.getElementsByClassName("login-prompt")[0].style = "width: 51% !important; height: 51% !important;"
	await sleep(200);
	document.getElementsByClassName("website-footer")[0].scrollIntoView();
}

init();