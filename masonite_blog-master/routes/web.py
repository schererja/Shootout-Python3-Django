"""Web Routes."""

from masonite.routes import Get, Post, Delete, Put, Patch

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    Get('/blog', 'BlogController@show'),
    Post('/blog/create', 'BlogController@store'),
    Get('/posts','PostController@show'),
    Get('/post/@id','PostController@single'),
    Get('/post/@id/update','PostController@update'),
    Post('/post/@id/update', 'PostController@store'),
    Get('/post/@id/delete', 'PostController@delete'),
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show').name('login'),
    Get().route('/logout', 'LoginController@logout').name('logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show').name('register'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show').name('home'),
    Get().route('/email/verify', 'ConfirmController@verify_show').name('verify'),
    Get().route('/email/verify/send', 'ConfirmController@send_verify_email'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/password', 'PasswordController@forget').name('forgot.password'),
    Post().route('/password', 'PasswordController@send'),
    Get().route('/password/@token/reset', 'PasswordController@reset').name('password.reset'),
    Post().route('/password/@token/reset', 'PasswordController@update'),
]
