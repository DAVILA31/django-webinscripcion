// con javaScript haremos la parte de la animación

// con esto estoy obteniendo todos los elelemntos que tenga la clase formulario__input
var inputs = document.getElementsByClassName('formulario__input');// en la variable input estamos obteniendo varios datos en una sola variable osea es un array


// para hacer el recorrido utilizamos un for
for(var i=0 ; i< inputs.length; i++){   // hará el recorrido de acuerdo a los elementos que aya
    inputs[i].addEventListener('keyup', function(){ // vamos a escuchar cunado dejamos terminemos de escribir
        if(this.value.length>=1){ // si almeos hay uno entonces 
            this.nextElementSibling.classList.add('fijar');  // seleccionar al siguiente elelmento y se le agregará una clase "fijar"
        }else{
            this.nextElementSibling.classList.remove('fijar'); // en caso contrario remuevo la clase fijar
        }
    });
}

// https://parzibyte.me/blog
const MAXIMO_TAMANIO_BYTES = 512000; // 1MB = 1 millón de bytes

// Obtener referencia al elemento
const $miInput = document.querySelector("#miInput");


$miInput.addEventListener("change", function () {
	// si no hay archivos, regresamos
	if (this.files.length <= 0) return;

	// Validamos el primer archivo únicamente
	const archivo = this.files[0];
	if (archivo.size > MAXIMO_TAMANIO_BYTES) {
		const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
		alert(`El tamaño máximo es ${tamanioEnMb} KB`);
		// Limpiar
		$miInput.value = "";
	} else {
		// Validación pasada. Envía el formulario o haz lo que tengas que hacer
	}
});


const $miInput2 = document.querySelector("#miInput2");


$miInput2.addEventListener("change", function () {
	// si no hay archivos, regresamos
	if (this.files.length <= 0) return;

	// Validamos el primer archivo únicamente
	const archivo = this.files[0];
	if (archivo.size > MAXIMO_TAMANIO_BYTES) {
		const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
		alert(`El tamaño máximo es ${tamanioEnMb} KB`);
		// Limpiar
		$miInput.value = "";
	} else {
		// Validación pasada. Envía el formulario o haz lo que tengas que hacer
	}
});

const $miInput3 = document.querySelector("#miInput3");


$miInput3.addEventListener("change", function () {
	// si no hay archivos, regresamos
	if (this.files.length <= 0) return;

	// Validamos el primer archivo únicamente
	const archivo = this.files[0];
	if (archivo.size > MAXIMO_TAMANIO_BYTES) {
		const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
		alert(`El tamaño máximo es ${tamanioEnMb} KB`);
		// Limpiar
		$miInput.value = "";
	} else {
		// Validación pasada. Envía el formulario o haz lo que tengas que hacer
	}
});

const $miInput4 = document.querySelector("#miInput4");


$miInput4.addEventListener("change", function () {
	// si no hay archivos, regresamos
	if (this.files.length <= 0) return;

	// Validamos el primer archivo únicamente
	const archivo = this.files[0];
	if (archivo.size > MAXIMO_TAMANIO_BYTES) {
		const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
		alert(`El tamaño máximo es ${tamanioEnMb} KB`);
		// Limpiar
		$miInput.value = "";
	} else {
		// Validación pasada. Envía el formulario o haz lo que tengas que hacer
	}
});

const $miInput5 = document.querySelector("#miInput5");


$miInput5.addEventListener("change", function () {
	// si no hay archivos, regresamos
	if (this.files.length <= 0) return;

	// Validamos el primer archivo únicamente
	const archivo = this.files[0];
	if (archivo.size > MAXIMO_TAMANIO_BYTES) {
		const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
		alert(`El tamaño máximo es ${tamanioEnMb} KB`);
		// Limpiar
		$miInput.value = "";
	} else {
		// Validación pasada. Envía el formulario o haz lo que tengas que hacer
	}
});

 const $miInput6 = document.querySelector("#miInput6");


$miInput6.addEventListener("change", function () {
	// si no hay archivos, regresamos
	if (this.files.length <= 0) return;

	// Validamos el primer archivo únicamente
	const archivo = this.files[0];
	if (archivo.size > MAXIMO_TAMANIO_BYTES) {
		const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
		alert(`El tamaño máximo es ${tamanioEnMb} KB`);
		// Limpiar
		$miInput.value = "";
	} else {
		// Validación pasada. Envía el formulario o haz lo que tengas que hacer
	}
});