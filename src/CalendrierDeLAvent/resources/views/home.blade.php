<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        @vite(['resources/css/style.css'])
        <title>Calendrier de l'avent</title>
    </head>
    <body>

    <h1 class="titre">Mon calendrier de l'avent</h1>

    
    @for ($i = 1; $i <= 24; $i++)
        <form method="GET" action="{{ route('jour', ['jour' => $i]) }}">
            <button type="submit" class="vert {{ $i == 24 ? 'jaune' : '' }}">
                Jour {{ $i }}
            </button>
        </form>
    @endfor
    </body>
</html>



