$(function () {
	var error_name = true;
	var error_pwd = true;
	var error_repwd = true;
	var error_email = true;
	var error_allow = true;


	$('#user_name').blur(function () {
		check_name();

	})

	$('#user_name').focus(function () {
		$(this).next().hide();

	})


	var pwd = $('#pwd');

	pwd.blur(function () {
		check_pwd();
	})

	pwd.focus(function () {
		$(this).next().hide();
	})

	var cpwd = $('#cpwd');

	cpwd.blur(function () {
		check_repwd();
	})

	cpwd.focus(function () {
		$(this).next().hide();
	})

	var email = $('#email')

	email.blur(function () {
		check_email();

	})

	email.focus(function () {
		$(this).next().hide();
	})







	function check_name() {

		var username_val = $('#user_name').val()
		var re = /^[a-z0-9_]{6,15}$/i

		if (username_val=='') {
			$('#user_name').next().html("用户名不能为空！");
			$('#user_name').next().show();
			error_name = true;
			return;
		}

		if (re.test(username_val)) {
			error_name = false;
		}
		else{
			error_name = true;
			$('#user_name').next().html("用户名只能是字母、数字、下划线的6到15位！");
			$('#user_name').next().show();
		}
	}

	function check_pwd() {
		var val = pwd.val();
		var re = /^[a-z0-9_*&]{6,20}$/i
		if (val == '') {
			pwd.next().html('密码不能为空！');
			pwd.next().show();
			error_pwd = true;
			return;
		}

		if (re.test(val)) {
			error_pwd = false;

		}
		else{
			error_pwd = true;
			pwd.next().html("密码只能是字母、数字、符号（_*&）的6到20位!");
			pwd.next().show();
		}

	}

	function check_repwd() {
		pwd_val = $('#pwd').val();
		repwd = $('#cpwd');

		if (pwd_val=='') {

			repwd.next().html("您未输入密码！请先完成密码输入！");
			repwd.next().show();
			return;
		}

		if (repwd.val()=='') {
			repwd.next().html("确认密码不能为空！");
			repwd.next().show();
			return;
		}


		if (repwd.val() == pwd_val) {
			repwd.next().hide();
			error_repwd = false;
			return;
		}
		else{
			repwd.next().html("确认密码与密码不一致，请重新输入！");
			repwd.next().show();
			error_repwd = true;
		}


	}


	function check_email() {
		var val = email.val();
		var re = /^\w+@(\d{2,3}|[a-zA-Z]{2,3}).[a-zA-Z]{2,3}$/
		if (val == '') {
			email.next().html('邮箱不能为空！');
			email.next().show();
			error_email = true;
			return;
		}

		if (re.test(val)) {
			error_email = false;

		}
		else{
			error_email = true;
			email.next().html("邮箱格式为xxxxxx@（qq、163、126）.com");
			email.next().show();
		}
		
	}



	
})