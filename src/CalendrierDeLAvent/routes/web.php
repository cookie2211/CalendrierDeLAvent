<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CalendrierController;

Route::view('/', 'home')->name('home');
Route::get('/jour/{jour}', [CalendrierController::class, 'show'])->name('jour');

