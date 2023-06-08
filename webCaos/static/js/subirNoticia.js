function validarNoticia() {
    $("#subir-form").validate({
      rules: {
        txtTitulo : {
          required: true,
          maxlength: 100
        },
        txtDesc: {
          required: true,
          maxlength: 1000
        },
        txtFecha: {
          required: true,
        },
        cboCategoria: {
          required:true,
        },
        txtPeriodista:{
          required: true,
        },
        txtIMG:{
          required: true
        }
      },
      // Specify validation error messages
      messages: {
        txtTitulo:{
          required: "Por favor, introduzca un Titulo"
        },
        txtDesc:{
          required: "Por favor, introduzca una descripción"
        },
        txtFecha:{
          required: "Por favor, introduzca la fecha de hoy  ",
        },
        cboCategoria:{
          required: "Por favor, introduzca una categoria"
        },
        txtPeriodista:{
          required: "Por favor, introduzca su nombre"
        },
        txtIMG:{
          required: "Por favor, seleccione un archivo",
          min: "Por favor, seleccione un archivo"
        }
      }  
    });
  };