window.location.href = "http://127.0.0.1:8000/"
document.getElementById("reg_search_feild").style.display = "none";
document.getElementById("display_msg").style.display = "none";

let msg = document.getElementById("display_msg");
let disp_msg = document.getElementById("disp_msg");
let disp_msg_bk = document.getElementById("display_msg_bk");


function Register_click(){
	document.getElementById("reg_search_feild").style.display = "block";
	document.getElementById("msg").innerHTML = "Register By Name";
	document.getElementById('register_but').style.background="grey";
	document.getElementById('Search_but').style.background="white";
	document.getElementById("ser_name").style.display="none";
	document.getElementById("reg_name").style.display="block";
	msg.style.display = "none";
	disp_msg_bk.style.display = "none";
}

function Search_click(){
	document.getElementById("reg_search_feild").style.display = "block";
	document.getElementById("msg").innerHTML = "Search By Name";
	document.getElementById('Search_but').style.background="grey";
	document.getElementById('register_but').style.background="white";
	document.getElementById("reg_name").style.display="none";
	document.getElementById("ser_name").style.display="block";
	msg.style.display = "none";
	disp_msg_bk.style.display = "none";
}


function validate(){
	document.getElementById("reg_search_feild").style.display = "none";
	document.getElementById('register_but').style.background="white";
	document.getElementById('Search_but').style.background="white";
	id = document.getElementById("id").value;
	name = document.getElementById("name").value;
	if (id == "" && name == ""){
		disp_msg_bk.style.display = "none";
		msg.style.display = "block";
		disp_msg.innerHTML = "Please Enter Id and Name";
	
	}

	if (id == "" && name != ""){
		disp_msg_bk.style.display = "none";
		msg.style.display = "block";
		disp_msg.innerHTML = "Please Enter Id";
		
	}

	if (id != "" && name == ""){
		disp_msg_bk.style.display = "none";
		msg.style.display = "block";
		disp_msg.innerHTML = "Please Enter Name";
		
	}

	if (id != "" && name != ""){
		disp_msg_bk.style.display = "none";
		msg.style.display = "none";
		
		return true
	}
 return false
}

// function ser_reg_validate(){
// 	let sr_name = document.getElementsByClassName("ser_reg_name").value;
// 	console.log(sr_name)
// 	if(sr_name == ""){
// 		msg.style.display = "block";
// 		disp_msg.innerHTML = "Please Enter Name";
// 		disp_msg_bk.style.display = "none";
// 		return false
// 	}else{
// 		disp_msg.innerHTML = "Name Entered";
// 		msg.style.display = "none";
// 		disp_msg_bk.style.display = "none";
// 		return true
// 	}

// }