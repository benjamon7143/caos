function validarContacto() {
  $("#contact-form").validate({
    rules: {
      txtNombre : {
        required: true,
        minlength: 3
      },
      txtApellido: {
        required: true,
        minlength: 3
      },
      txtCorreo: {
        required: true,
        email: true
      },
      // txtNumero: {
      //   required:true,
      //   number: true,
      // },
      txtArchivo:{
        required: true,
        min: 1
      },
      txtdescrip:{
        required: true,
        minlength: 50,
        maxlength: 5000
      }
    },
    // Specify validation error messages
    messages: {
      txtNombre:{
        required: "Por favor, introduzca su nombre",
        minlength: "Su nombre debe tener al menos 3 caracteres."
      },
      txtApellido:{
        required: "Por favor, introduzca su apellido",
        minlength: "Su apellido debe tener al menos 3 caracteres."
      },
      txtCorreo:{
        required: "Por favor, introduzca su correo electrónico",
        email: "Por favor, introduzca un correo electrónico válido."
      },
      // txtNumero:{
      //   required: "Por favor, introduzca su número de teléfono",
      //   number: "Por favor, introduzca un número de teléfono válido.",
      // },
      txtArchivo:{
        required: "Por favor, seleccione un archivo",
        min: "Por favor, seleccione un archivo"
      },
      txtdescrip:{
        required: "Por favor, introduzca una descripción",
        minlength: "La descripción debe tener al menos 50 caracteres.",
        maxlength: "La descripción debe tener un máximo de 5000 caracteres."
      }
    }  
  });
};


