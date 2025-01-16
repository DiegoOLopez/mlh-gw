const button = document.getElementById('uselessButton');
const message = document.getElementById('message');
const animations = document.getElementById('animations');

// Mensajes aleatorios
const mensajes = [
  "¡Te lo advertí!",
  "¿Por qué lo hiciste?",
  "Ahora el mundo está en peligro.",
  "Esto es completamente inútil.",
  "¡Hackeado!",
  "¡Error 404: Tu autocontrol no se encuentra!"
];

// GIFs inútiles
const gifs = [
  "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", // Gato
  "https://media.giphy.com/media/26n6WywJyh39n1pBu/giphy.gif", // Hackeado
  "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", // Explosión
  "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif"  // Bailando
];

// Acción del botón
button.addEventListener('click', () => {
  // Mostrar un mensaje aleatorio
  const randomMessage = mensajes[Math.floor(Math.random() * mensajes.length)];
  message.textContent = randomMessage;

  // Cambiar el color de fondo a algo aleatorio
  document.body.style.backgroundColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;

  // Agregar un GIF aleatorio
  const randomGif = gifs[Math.floor(Math.random() * gifs.length)];
  const img = document.createElement('img');
  img.src = randomGif;
  animations.appendChild(img);

  // Quitar el GIF después de 5 segundos
  setTimeout(() => {
    animations.removeChild(img);
  }, 5000);
});
