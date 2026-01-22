<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		@vite(['resources/css/style.css'])

        <link rel="stylesheet" media="screen" type="text/css" title="style" href="../static/style.css" \>
        <script src="https://cdn.jsdelivr.net/gh/kitao/pyxel/wasm/pyxel.js"></script>
		<title>@yield('title')</title>
	</head>
	<body>
		@section('description')
        @show
        <div class="jeu">
            <pyxel-run root= "/jeux" name=@yield('gameEmplacement')></pyxel-run>
        </div>
	</body>
</html>
