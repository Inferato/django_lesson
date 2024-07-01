$(document).ready(function () {
    $('#id_username').blur(function () {
        checkUserExists();
    });

    $('#id_email').blur(function () {
        checkUserExists();
    });

    $('#id_password1').blur(function () {
        validatePasswords();
    });

    $('#id_password2').blur(function () {
        validatePasswords();
    });

    function checkUserExists() {
        var username = $('#id_username').val();
        var email = $('#id_email').val();
        var user_data = {'username': username, 'email': email};

        $.ajax({
            url: '/check_user_exists/',
            data: user_data,
            dataType: 'json',
            success: function (data) {
                if (data.username_exists) {
                    $('#usernameError').text('This username is already taken')
                } else {
                    $('#usernameError').text('')
                }

                if (data.email_exists) {
                    $('#emailError').text('This email is already in use')
                } else {
                    $('#emailError').text('')
                }

                if (data.user_check_errors) {
                    $('#registerButton').prop('disabled', true)
                } else {
                    $('#registerButton').prop('disabled', false)
                }
            }
        });
    }

    function validatePasswords() {
        var password =  $('#id_password1').val();
        var confirmPassword =  $('#id_password2').val()
        var password_is_empty = password.length < 1
        if (!password_is_empty) {
            if (password !== confirmPassword) {
                $('#confirmPasswordError').text('Passwords didnt match');
                $('#registerButton').prop('disabled', true);
            } else {
                $('#confirmPasswordError').text('');
                $('#registerButton').prop('disabled', false);
            }
        } else {
            $('#confirmPasswordError').text('Password cant be empty');
            $('#registerButton').prop('disabled', true);
        }
    }
})